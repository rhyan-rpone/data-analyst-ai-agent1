# Agent responsável por entender
# o tipo de análise solicitado


def query_agent(state):

    # Pergunta do usuário
    question = state["question"].lower()

    # Tipo padrão
    analysis_type = "general"

    # Detecta intenção

    if "correlação" in question:
        analysis_type = "correlation"

    elif "categoria" in question:
        analysis_type = "categorical"

    elif "tendência" in question:
        analysis_type = "trend"

    elif "nulos" in question:
        analysis_type = "missing_values"

    # Retorna pro state
    return {
        "analysis_type": analysis_type
    }