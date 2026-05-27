def schema_agent(state):

    dataset = state["dataset_info"]

    summary = f"""
    📁 Estrutura do Dataset

    • Total de linhas: {dataset['shape'][0]}
    • Total de colunas: {dataset['shape'][1]}

    📌 Colunas disponíveis:

    {dataset['columns']}

    📌 Tipos das colunas:

    {dataset['dtypes']}

    📌 Valores nulos:

    {dataset['nulls']}
    """

    return {

        # Agora salva em schema_result
        "schema_result": summary
    }