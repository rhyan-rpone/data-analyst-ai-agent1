import plotly.express as px
import plotly.graph_objects as go


# =========================
# CONFIG PADRÃO
# =========================

PLOT_TEMPLATE = "plotly_dark"

CHART_HEIGHT = 600


# =========================
# SELEÇÃO INTELIGENTE
# DE COLUNAS NUMÉRICAS
# =========================

def get_best_numeric_columns(df):

    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns

    valid_cols = []

    for col in numeric_cols:

        # Remove colunas constantes
        if df[col].nunique() <= 1:
            continue

        # Remove colunas quase vazias
        if df[col].isnull().mean() > 0.7:
            continue

        valid_cols.append(col)

    return valid_cols


# =========================
# SELEÇÃO INTELIGENTE
# DE COLUNAS CATEGÓRICAS
# =========================

def get_best_categorical_columns(df):

    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns

    valid_cols = []

    for col in categorical_cols:

        # Evita IDs únicos
        if df[col].nunique() > 50:
            continue

        valid_cols.append(col)

    return valid_cols


# =========================
# HEATMAP DE CORRELAÇÃO
# =========================

def generate_correlation_chart(df):

    numeric_cols = get_best_numeric_columns(df)

    if len(numeric_cols) < 3:
        return None

    numeric_df = df[numeric_cols]

    corr = numeric_df.corr()

    fig = px.imshow(

        corr,

        text_auto=".2f",

        aspect="auto",

        color_continuous_scale="RdBu",

        zmin=-1,

        zmax=1
    )

    fig.update_layout(

        title="🔥 Correlação entre Variáveis",

        template=PLOT_TEMPLATE,

        height=CHART_HEIGHT,

        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        ),

        font=dict(
            size=14
        )
    )

    return fig


# =========================
# HISTOGRAMA
# =========================

def generate_histogram(df):

    numeric_cols = get_best_numeric_columns(df)

    if len(numeric_cols) == 0:
        return None

    # Escolhe coluna com maior variabilidade
    col = max(

        numeric_cols,

        key=lambda x: df[x].std()
    )

    fig = px.histogram(

        df,

        x=col,

        nbins=30,

        title=f"📈 Distribuição de {col}",

        template=PLOT_TEMPLATE,

        opacity=0.85
    )

    fig.update_layout(

        height=CHART_HEIGHT,

        bargap=0.05,

        xaxis_title=col,

        yaxis_title="Frequência"
    )

    return fig


# =========================
# SCATTERPLOT
# =========================

def generate_scatterplot(df):

    numeric_cols = get_best_numeric_columns(df)

    if len(numeric_cols) < 2:
        return None

    x_col = numeric_cols[0]
    y_col = numeric_cols[1]

    fig = px.scatter(

        df,

        x=x_col,

        y=y_col,

        trendline="ols",

        title=f"📊 Relação entre {x_col} e {y_col}",

        template=PLOT_TEMPLATE,

        opacity=0.75
    )

    fig.update_layout(

        height=CHART_HEIGHT,

        xaxis_title=x_col,

        yaxis_title=y_col
    )

    return fig


# =========================
# LINE CHART
# =========================

def generate_line_chart(df):

    numeric_cols = get_best_numeric_columns(df)

    if len(numeric_cols) == 0:
        return None

    col = numeric_cols[0]

    fig = px.line(

        df,

        y=col,

        title=f"📈 Tendência de {col}",

        template=PLOT_TEMPLATE
    )

    fig.update_layout(

        height=CHART_HEIGHT,

        xaxis_title="Índice",

        yaxis_title=col
    )

    return fig


# =========================
# BAR CHART
# =========================

def generate_bar_chart(df):

    categorical_cols = get_best_categorical_columns(df)

    if len(categorical_cols) == 0:
        return None

    col = categorical_cols[0]

    counts = df[col].value_counts().head(10)

    fig = px.bar(

        x=counts.index,

        y=counts.values,

        text=counts.values,

        title=f"📊 Categorias mais frequentes em {col}",

        template=PLOT_TEMPLATE
    )

    fig.update_layout(

        height=CHART_HEIGHT,

        xaxis_title=col,

        yaxis_title="Quantidade"
    )

    return fig


# =========================
# BOXPLOT
# =========================

def generate_boxplot(df):

    numeric_cols = get_best_numeric_columns(df)

    if len(numeric_cols) == 0:
        return None

    col = numeric_cols[0]

    fig = px.box(

        df,

        y=col,

        title=f"📦 Distribuição e Outliers de {col}",

        template=PLOT_TEMPLATE
    )

    fig.update_layout(

        height=CHART_HEIGHT,

        yaxis_title=col
    )

    return fig


# =========================
# ROUTER INTELIGENTE
# =========================

def get_chart_by_analysis_type(

    analysis_type,

    df
):

    charts = []

    # =========================
    # CORRELAÇÃO
    # =========================

    if analysis_type == "correlation":

        charts.append(
            generate_correlation_chart(df)
        )

        charts.append(
            generate_scatterplot(df)
        )

        charts.append(
            generate_boxplot(df)
        )

    # =========================
    # TENDÊNCIA
    # =========================

    elif analysis_type == "trend":

        charts.append(
            generate_line_chart(df)
        )

        charts.append(
            generate_histogram(df)
        )

    # =========================
    # CATEGÓRICO
    # =========================

    elif analysis_type == "categorical":

        charts.append(
            generate_bar_chart(df)
        )

    # =========================
    # VALORES NULOS
    # =========================

    elif analysis_type == "missing_values":

        charts.append(
            generate_bar_chart(df)
        )

    # =========================
    # GERAL
    # =========================

    else:

        charts.append(
            generate_histogram(df)
        )

        charts.append(
            generate_scatterplot(df)
        )

        charts.append(
            generate_boxplot(df)
        )

    # Remove gráficos inválidos
    charts = [

        chart for chart in charts

        if chart is not None
    ]

    return charts