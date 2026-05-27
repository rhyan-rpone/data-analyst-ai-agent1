import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =========================
# IMPORTS DO PROJETO
# =========================

from graphs.workflow import graph
from tools.chart_generator import get_chart_by_analysis_type


# =========================
# CONFIG DA PÁGINA
# =========================

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================
# CHAT MEMORY
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================
# CSS CUSTOMIZADO
# =========================

st.markdown("""
<style>
.main { padding-top: 2rem; }
.block-container { padding-top: 2rem; }

.stMetric {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #1f2937;
}

h1, h2, h3 { font-weight: 700; }

.chat-container {
    border-radius: 12px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)


# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.title("🤖 AI Data Analyst")

    st.markdown("""
    Plataforma inteligente de análise de dados
    baseada em arquitetura multi-agent.
    """)

    st.divider()

    st.subheader("⚙️ Recursos")

    st.markdown("""
    ✅ Insights com IA  
    ✅ Chat com memória  
    ✅ Classificação de intenção  
    ✅ Gráficos inteligentes  
    ✅ Visualizações interativas  
    ✅ Multi-Agent com LangGraph  
    ✅ Análise estatística  
    """)

    st.divider()

    st.caption("Powered by LangGraph + OpenAI + Streamlit")


# =========================
# HEADER
# =========================

st.title("📊 AI Data Analyst Assistant")

st.markdown("""
Faça upload de um dataset CSV e converse com os dados utilizando IA.
""")


# =========================
# UPLOAD CSV
# =========================

uploaded_file = st.file_uploader(
    "📁 Envie seu arquivo CSV",
    type=["csv"]
)


# =========================
# EXECUÇÃO PRINCIPAL
# =========================

if uploaded_file is not None:

    try:

        # =========================
        # LEITURA DATAFRAME
        # =========================

        df = pd.read_csv(uploaded_file, encoding="latin1")

        # =========================
        # MÉTRICAS
        # =========================

        st.subheader("📌 Informações Gerais")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Linhas", f"{df.shape[0]:,}")

        with col2:
            st.metric("Colunas", df.shape[1])

        with col3:
            st.metric("Valores Nulos", int(df.isnull().sum().sum()))

        with col4:
            st.metric(
                "Colunas Numéricas",
                len(df.select_dtypes(include=["number"]).columns)
            )

        # =========================
        # PREVIEW DATASET
        # =========================

        with st.expander("📁 Preview do Dataset", expanded=True):
            st.dataframe(df.head(20), use_container_width=True)

        # =========================
        # HISTÓRICO CHAT
        # =========================

        st.subheader("💬 Conversa")

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # =========================
        # INPUT USUÁRIO
        # =========================

        question = st.chat_input("Faça uma pergunta sobre o dataset...")

        if question:

            st.session_state.messages.append({
                "role": "user",
                "content": question
            })

            with st.chat_message("user"):
                st.markdown(question)

            with st.spinner("🧠 Os agentes estão analisando os dados..."):

                dataset = {
                    "dataframe": df,
                    "shape": df.shape,
                    "columns": list(df.columns),
                    "dtypes": df.dtypes.astype(str).to_dict(),
                    "nulls": df.isnull().sum().to_dict()
                }

                result = graph.invoke({
                    "question": question,
                    "dataset_info": dataset
                })

                final_response = result["final_response"]
                analysis_type = result["analysis_type"]

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": final_response
                })

                with st.chat_message("assistant"):
                    st.markdown(final_response)

                # =========================
                # GRÁFICOS INTELIGENTES
                # =========================

                st.subheader("📈 Visualizações Inteligentes")

                charts = get_chart_by_analysis_type(
                    analysis_type,
                    df
                )

                if charts:
                    for chart in charts:
                        if isinstance(chart, go.Figure):
                            st.plotly_chart(chart, use_container_width=True)

    except Exception as e:
        st.error(f"Erro ao processar dataset: {e}")


# =========================
# TELA INICIAL
# =========================

else:
    st.info("📁 Faça upload de um dataset CSV para começar.")