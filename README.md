# 📊 AI Data Analyst Assistant

Um assistente inteligente de análise de dados desenvolvido com LangGraph, Streamlit e OpenAI.

O objetivo do projeto é transformar datasets CSV em análises compreensíveis, insights acionáveis e visualizações modernas através de uma arquitetura multi-agent simples, mas bem estruturada.

---

# 🚀 Sobre o Projeto

Esse projeto surgiu como uma forma de explorar aplicações reais de IA generativa em análise de dados.

A ideia principal foi construir um sistema capaz de:

- interpretar perguntas em linguagem natural
- entender o contexto da análise desejada
- processar datasets automaticamente
- gerar insights com IA
- criar visualizações interativas
- organizar tudo em uma arquitetura modular

Ao invés de criar um único script enorme, o sistema foi dividido em agentes especializados, cada um responsável por uma parte do processo analítico.

---

# 🧠 Como Funciona

O fluxo do sistema segue uma arquitetura multi-agent utilizando LangGraph.

```text
Usuário
   ↓
Query Agent
   ↓
Schema Agent
   ↓
Analysis Agent
   ↓
Advanced Analysis Agent
   ↓
Insight Agent
   ↓
Resposta Final + Visualizações
```

---

# 🤖 Agents do Sistema

## Query Agent

Responsável por entender a intenção da pergunta do usuário.

Exemplo:

```text
"Existe correlação entre as variáveis?"
```

O agent identifica que o foco da análise deve ser correlação.

---

## Schema Agent

Analisa a estrutura do dataset:

- quantidade de linhas
- quantidade de colunas
- tipos de dados
- nomes das colunas

---

## Analysis Agent

Executa análises estatísticas básicas:

- média
- mediana
- quartis
- desvio padrão
- valores mínimos e máximos

---

## Advanced Analysis Agent

Realiza análises complementares:

- valores nulos
- padrões
- distribuições
- possíveis anomalias

---

## Insight Agent

Responsável por transformar todas as análises em uma resposta clara e contextualizada utilizando LLM.

É ele quem gera os insights finais exibidos para o usuário.

---

# 🛠️ Tecnologias Utilizadas

## Backend e IA

- Python
- LangGraph
- LangChain
- OpenAI API

## Processamento de Dados

- Pandas
- NumPy

## Interface e Visualização

- Streamlit
- Plotly

## Outros

- python-dotenv

---

# 📁 Estrutura do Projeto

```text
data-analyst-ai-agent/

├── agents/
├── graphs/
├── tools/
├── datasets/

├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
```

---

## 2. Acesse a pasta do projeto

```bash
cd data-analyst-ai-agent
```

---

## 3. Crie um ambiente virtual

### Windows

```bash
python -m venv venv
```

---

## 4. Ative o ambiente virtual

### PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

---

## 5. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuração da OpenAI

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

---

# ▶️ Executando a Aplicação

```bash
streamlit run app.py
```

---

# 📊 Funcionalidades

Atualmente o sistema consegue:

✅ Fazer upload de datasets CSV  
✅ Interpretar perguntas em linguagem natural  
✅ Detectar intenção da análise  
✅ Gerar insights com IA  
✅ Criar visualizações interativas  
✅ Detectar correlações  
✅ Gerar análises estatísticas automáticas  

---

# 📈 Visualizações

A aplicação gera gráficos automaticamente utilizando Plotly:

- Heatmaps de correlação
- Histogramas
- Scatterplots
- Distribuições estatísticas

Todos os gráficos são interativos e responsivos.

---

# 💬 Exemplos de Perguntas

```text
Existe correlação entre as variáveis?
```

```text
Quais categorias aparecem com mais frequência?
```

```text
Existe alguma tendência temporal?
```

```text
Faça uma análise geral do dataset
```

---

# 🎯 Objetivo do Projeto

Além do aprendizado técnico, o projeto foi pensado para servir como:

- estudo de arquitetura multi-agent
- demonstração prática de IA aplicada a dados
- projeto de portfólio
- base para futuras aplicações SaaS

---

# 🚀 Próximos Passos

Algumas melhorias planejadas:

- memória de conversa
- exportação de relatórios
- suporte para Excel
- gráficos dinâmicos por intenção
- profiling automático de datasets
- deploy em cloud

---

# 📸 Screenshots

_(adicione screenshots futuramente)_

---

# 🌐 Deploy

O projeto pode ser facilmente publicado utilizando:

- Streamlit Cloud
- Render
- HuggingFace Spaces

---

# 👨‍💻 Autor

Desenvolvido por Rhyan Pablo.

---