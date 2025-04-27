from pyspark.sql.functions import col, coalesce, to_date, floor, datediff, current_date, when, count, sum , desc, first, max
from pyspark.sql.window import Window

class DataPreprocessor(object):
    def __init__(self, df_profile, df_transactions):
        self.profile = df_profile
        self.transactions = df_transactions

    def transform(self):
        df_transactions_processed = self.__transform_transactions_value_to_columns(self.transactions)
        df_profile_processed = self.__edit_create_time_since_registere_column(self.profile)
        df_profile_processed = self.__filter_inconsistent_age(df_profile_processed)
        df_procesed = self.__merge_profile_transactions(df_transactions_processed,df_profile_processed)
        df_procesed = self.__create_account_agregated_columns(df_procesed)
        df_procesed = self.__create_last_completed_offer_id_column(df_procesed)
        df_model = self.__create_account_offer_granularity_df(df_procesed)
        return df_procesed, df_model


    def __transform_transactions_value_to_columns(self,df_transactions):
        df_transactions = df_transactions \
        .withColumn("amount", col("value.amount")) \
        .withColumn("offer id", col("value.offer id")) \
        .withColumn("offer_id", col("value.offer_id")) \
        .withColumn("reward", col("value.reward")) 

        df_transactions = df_transactions.withColumn("offer_id", coalesce(col("offer_id"), col("offer id"))).drop('offer id','value')
        return df_transactions

    def __edit_create_time_since_registere_column(self,df_profile):
        df_profile = df_profile.withColumn("registered_on", to_date(col("registered_on"), "yyyyMMdd"))
        df_profile = df_profile.withColumn("time_since_registered", floor(datediff(current_date(), col("registered_on")))).drop('registered_on')
        return df_profile
    
    def __filter_inconsistent_age(self,df_profile):
        df_profile = df_profile.withColumn("age", col("age").cast("int"))
        df_profile = df_profile.filter(col('age')!=118)
        return df_profile

    def __merge_profile_transactions(self,df_transactions, df_profile):
        df_merged = df_transactions.join(df_profile,df_transactions.account_id == df_profile.id,'right').drop('id') 
        return df_merged

    def __create_account_agregated_columns(self,df_merged):
        window_spec = Window.partitionBy("account_id")

        df_merged = df_merged.withColumn("total_orders", count("amount").over(window_spec)) \
                    .withColumn("average_transaction_value", 
                                sum("amount").over(window_spec) / col("total_orders")) \
                    .withColumn("n_viewed", 
                                sum(when(col("event") == "offer viewed", 1).otherwise(0)).over(window_spec)) \
                    .withColumn("n_completed", 
                                sum(when(col("event") == "offer completed", 1).otherwise(0)).over(window_spec)) \
                    .withColumn("completion_rate", 
                                when(col("n_viewed") > 0, col("n_completed") / col("n_viewed")).otherwise(None))

        return df_merged

    def __create_last_completed_offer_id_column(self,df_merged):
        df_completed = df_merged.filter(col("event") == "offer completed")

        w = Window.partitionBy("account_id").orderBy(desc("time_since_test_start"))

        df_completed = df_completed.withColumn(
            "last_completed_offer_id",
            first("offer_id").over(w)
        )

        df_last_offer = df_completed.select("account_id", "last_completed_offer_id").dropDuplicates(["account_id"])

        df_merged = df_merged.join(df_last_offer, on="account_id", how="left")
        return df_merged
    

    def __create_account_offer_granularity_df(self,df_merged):
        w = Window.partitionBy("account_id", "offer_id")

        df_account_offer_granularity = df_merged.withColumn("offer_completed",
                                    max(when(col("event") == "offer completed", 1).otherwise(0)).over(w)) \
                                        .filter((col("event")!="transaction") & (col("event")!="offer viewed")) \
                        .withColumn("reward", max(col("reward")).over(w)) \
                        .withColumn("time_since_test_start", max(col("time_since_test_start")).over(w)) \
                        .drop("event","amount","time_since_test_start","n_completed") \
                            .dropDuplicates(["account_id", "offer_id"])
        return df_account_offer_granularity
