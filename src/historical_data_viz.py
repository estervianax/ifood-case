import matplotlib.pyplot as plt
import seaborn as sns


class HistoricalDataVisualizer:
    def __init__(self, df_proceed,df_model):
        self.df_proceed = df_proceed
        self.df_model = df_model

    def plot_historical_data(self):
        self.__plot_client_statistics(self.df_proceed)
        self.__plot_transactions_vs_credit_limit(self.df_proceed)
        self.__plot_analyze_offer_status(self.df_proceed)
        self.__plot_target_balance(self.df_model)


    def __plot_client_statistics(self,df_proceed):
        df_cliente_stats = df_proceed.groupby('account_id').agg(
            mean_age=('age', 'mean'),
            mean_credit=('credit_card_limit', 'mean'),
            gender=('gender', 'first')
        ).reset_index()

        plt.figure(figsize=(10, 6))
        sns.histplot(df_cliente_stats['mean_age'], color='#d52221', bins=15)
        plt.title('Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Number of Clients')
        plt.show()

        plt.figure(figsize=(8, 6))
        sns.countplot(x='gender', data=df_cliente_stats, palette='Reds')
        plt.title('Gender Distribution')
        plt.xlabel('Gender')
        plt.ylabel('Number of Clients')
        plt.show()

        plt.figure(figsize=(10, 6))
        sns.histplot(df_cliente_stats['mean_credit'], color='#aa1016', bins=15)
        plt.title('Credit Card Limit Distribution')
        plt.xlabel('Credit Card Limit')
        plt.ylabel('Number of Clients')
        plt.show()

    def __plot_transactions_vs_credit_limit(self,df_proceed):
        df_transacoes = df_proceed[df_proceed['event'] == 'transaction']
        df_transacoes_count = df_transacoes.groupby('account_id').agg(
            total_transactions=('amount', 'count'),
            limite_cartao=('credit_card_limit', 'first')
        ).reset_index()

        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='limite_cartao', y='total_transactions', data=df_transacoes_count, color='#fc8161')
        plt.title('Number of Transactions vs. Credit Card Limit')
        plt.xlabel('Credit Card Limit')
        plt.ylabel('Number of Transactions')
        plt.show()

    def __plot_analyze_offer_status(self,df_proceed):
        df_proceed['is_received'] = (df_proceed['event'] == 'offer received').astype(int)
        df_proceed['is_completed'] = (df_proceed['event'] == 'offer completed').astype(int)

        df_status_oferta = df_proceed.groupby(['account_id', 'offer_id']).agg(
            qtd_received=('is_received', 'sum'),
            qtd_completed=('is_completed', 'sum')
        ).reset_index()

        df_status_oferta = df_status_oferta[
            (df_status_oferta['qtd_received'] > 1) &
            (df_status_oferta['qtd_completed'] > 0) &
            ((df_status_oferta['qtd_received'] - df_status_oferta['qtd_completed']) > 0)
        ]

        df_status_oferta = df_status_oferta.sort_values(by='qtd_received', ascending=False)
        df_plot = df_status_oferta[0:3]
        df_plot['id'] = df_plot['account_id'].astype(str) + "/" + df_plot['offer_id'].astype(str)
        df_plot = df_plot.melt(
            id_vars=['id'],
            value_vars=['qtd_received', 'qtd_completed'],
            var_name='Status',
            value_name='Quantidade'
        )
        plt.figure(figsize=(14, 7))
        sns.barplot(data=df_plot, x='id', y='Quantidade', hue='Status', palette='Reds')

        for p in plt.gca().patches:
            plt.gca().annotate(format(p.get_height(), '.0f'),
                            (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha = 'center', va = 'center',
                            xytext = (0, 5),
                            textcoords = 'offset points')
            
        plt.title('Number of Offers Received vs Completed')
        plt.xlabel('Offer ID')
        plt.ylabel('Quantity')
        plt.xticks(rotation=45)
        plt.legend(title='Status')
        plt.tight_layout()
        plt.show()

    def __plot_target_balance(self,df_modelo):
        offer_counts = df_modelo['offer_completed'].value_counts()  

        plt.figure(figsize=(10,6))
        sns.barplot(x=offer_counts.index, y=offer_counts.values, palette='Reds')

        for p in plt.gca().patches:
            plt.gca().annotate(format(p.get_height(), '.0f'),
                            (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha = 'center', va = 'center',
                            xytext = (0, 5),
                            textcoords = 'offset points')

        plt.title('Distribution of Completed vs. Not Completed Offers', fontsize=16)
        plt.xlabel('Offer Completed?', fontsize=12)
        plt.ylabel('Quantity', fontsize=12)
        plt.xticks(rotation=45) 
        plt.tight_layout()  
        plt.show()


