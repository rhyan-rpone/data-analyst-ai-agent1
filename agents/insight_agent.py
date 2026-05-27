from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()


# =========================
# MODELO LLM
# =========================

llm = ChatOpenAI(

    model="gpt-4.1-mini",

    temperature=0.3
)


# =========================
# INSIGHT AGENT
# =========================

def insight_agent(state):

    # =========================
    # DADOS DO STATE
    # =========================

    # Estrutura do dataset
    schema = state["schema_result"]

    # Estatísticas descritivas
    analysis = state["analysis_result"]

    # Análises avançadas
    advanced_analysis = state["advanced_analysis"]

    # Tipo de análise detectado
    analysis_type = state["analysis_type"]

    # Pergunta do usuário
    question = state["question"]


    # =========================
    # CONTEXTO POR INTENÇÃO
    # =========================

    focus_context = """

    Faça uma análise geral do dataset.
    """

    # Correlação
    if analysis_type == "correlation":

        focus_context = """
        Foque principalmente em:

        - correlações entre variáveis
        - relações entre colunas
        - possíveis dependências
        - padrões estatísticos relevantes
        """

    # Categorias
    elif analysis_type == "categorical":

        focus_context = """
        Foque principalmente em:

        - categorias mais frequentes
        - distribuições
        - padrões categóricos
        - grupos predominantes
        """

    # Tendências
    elif analysis_type == "trend":

        focus_context = """
        Foque principalmente em:

        - tendências temporais
        - crescimento ou queda
        - evolução dos dados
        - mudanças ao longo do tempo
        """

    # Valores nulos
    elif analysis_type == "missing_values":

        focus_context = """
        Foque principalmente em:

        - qualidade dos dados
        - valores ausentes
        - possíveis impactos dos dados faltantes
        - confiabilidade do dataset
        """


    # =========================
    # PROMPT
    # =========================

    prompt = f"""
    Você é um analista de dados sênior.

    Sua função é interpretar datasets
    e gerar insights profissionais.

    Pergunta do usuário:
    {question}

    Tipo de análise solicitado:
    {analysis_type}

    Direcionamento da análise:
    {focus_context}

    Considere:
    - estrutura dos dados
    - tipos das colunas
    - estatísticas
    - correlações
    - valores nulos
    - padrões relevantes

    Gere insights:
    - claros
    - profissionais
    - objetivos
    - em português brasileiro
    - bem formatados
    - com linguagem executiva

    ============================
    ESTRUTURA DO DATASET
    ============================

    {schema}

    ============================
    ANÁLISE ESTATÍSTICA
    ============================

    {analysis}

    ============================
    ANÁLISE AVANÇADA
    ============================

    {advanced_analysis}
    """


    # =========================
    # CHAMADA DO LLM
    # =========================

    response = llm.invoke([

        HumanMessage(content=prompt)
    ])


    # =========================
    # RETORNO FINAL
    # =========================

    return {

    "final_response": response.content,

    "analysis_type": state["analysis_type"]
}