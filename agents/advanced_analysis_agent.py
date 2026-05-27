# Agent responsável por análises avançadas

def advanced_analysis_agent(state):

    # Pega dataset
    dataset = state["dataset_info"]

    # DataFrame
    df = dataset["dataframe"]

    # Texto final
    advanced = "\n📈 ANÁLISE AVANÇADA\n"

    # =========================
    # CORRELAÇÕES
    # =========================

    try:

        corr = df.corr(numeric_only=True)

        advanced += "\n━━━━━━━━━━━━━━━━━━\n"
        advanced += "📌 Correlações\n"
        advanced += "━━━━━━━━━━━━━━━━━━\n"

        advanced += corr.to_string()

    except:
        advanced += "\nNão foi possível calcular correlações.\n"

    # =========================
    # VALORES NULOS
    # =========================

    advanced += "\n\n━━━━━━━━━━━━━━━━━━\n"
    advanced += "📌 Valores Nulos\n"
    advanced += "━━━━━━━━━━━━━━━━━━\n"

    nulls = df.isnull().sum()

    for coluna, total in nulls.items():

        if total > 0:
            advanced += f"\n{coluna}: {total} valores nulos"

    # =========================
    # COLUNAS CATEGÓRICAS
    # =========================

    advanced += "\n\n━━━━━━━━━━━━━━━━━━\n"
    advanced += "📌 Colunas Categóricas\n"
    advanced += "━━━━━━━━━━━━━━━━━━\n"

    categorical_cols = df.select_dtypes(include="object").columns

    for col in categorical_cols:

        advanced += f"\n\n🔹 {col}"

        top_values = df[col].value_counts().head(3)

        for valor, qtd in top_values.items():

            advanced += f"\n- {valor}: {qtd}"

    # Retorna resultado
    return {
        "advanced_analysis": advanced
    }