# Agent responsável por analisar o dataset

def analysis_agent(state):

    # Pega o dataset do state
    dataset = state["dataset_info"]

    # Pega o DataFrame
    df = dataset["dataframe"]

    # Gera estatísticas numéricas
    stats = df.describe()

    # Traduz nomes das métricas
    metricas_ptbr = {
        "count": "Total",
        "mean": "Média",
        "std": "Desvio Padrão",
        "min": "Mínimo",
        "25%": "1º Quartil",
        "50%": "Mediana",
        "75%": "3º Quartil",
        "max": "Máximo"
    }

    # Renomeia os índices
    stats.rename(index=metricas_ptbr, inplace=True)

    # Cria texto formatado
    analysis = "\n📊 ANÁLISE ESTATÍSTICA DO DATASET\n"

    # Percorre cada coluna numérica
    for coluna in stats.columns:

        analysis += f"\n━━━━━━━━━━━━━━━━━━\n"
        analysis += f"📌 Coluna: {coluna}\n"
        analysis += f"━━━━━━━━━━━━━━━━━━\n"

        # Percorre cada métrica
        for metrica, valor in stats[coluna].items():

            # Limita casas decimais
            analysis += f"{metrica}: {valor:.2f}\n"

    # Retorna resultado
    return {
        "analysis_result": analysis
    }