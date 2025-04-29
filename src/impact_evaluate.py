from pyspark.sql import functions as F

# Mémoria de calculo para impacto do modelo na conversão

# Definindo a taxa de conversão, obtida a partir da saida da classe ModelEvaluator
nova_taxa_conversao = 1.046

# Calculando o ticket médio geral da base
ticket_medio_geral = df_all.agg(
    (F.sum("amount") / F.count("amount")).alias("ticket_medio_geral")
).collect()[0]["ticket_medio_geral"]

# Calculando o número de contas distintas
distinct_account_ids = df_all.select("account_id").distinct().count()

# Calculando o impacto financeiro da nova taxa de conversão do modelo
impacto_financeiro_nova_taxa_conversao = ((distinct_account_ids * ticket_medio_geral) * nova_taxa_conversao) - (distinct_account_ids * ticket_medio_geral)


# Contando o número de ofertas completas 
quantidade_ofertas_completas = df_all.filter(F.col('offer_completed') == 1).count()

# Calculando o impacto no numero de conversões da nova taxa de conversão do modelo
impacto_qnt_conversoes_nova_taxa_conversao = (quantidade_ofertas_completas * nova_taxa_conversao) - quantidade_ofertas_completas