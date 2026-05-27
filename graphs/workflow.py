from langgraph.graph import StateGraph

# =========================
# STATE
# =========================

from graphs.state import AgentState


# =========================
# AGENTS
# =========================

from agents.query_agent import query_agent

from agents.schema_agent import schema_agent

from agents.analysis_agent import analysis_agent

from agents.advanced_analysis_agent import (
    advanced_analysis_agent
)

from agents.insight_agent import insight_agent


# =========================
# GRAPH BUILDER
# =========================

builder = StateGraph(AgentState)


# =========================
# NODES
# =========================

builder.add_node(

    "query_agent",

    query_agent
)

builder.add_node(

    "schema_agent",

    schema_agent
)

builder.add_node(

    "analysis_agent",

    analysis_agent
)

builder.add_node(

    "advanced_analysis_agent",

    advanced_analysis_agent
)

builder.add_node(

    "insight_agent",

    insight_agent
)


# =========================
# ENTRY POINT
# =========================

builder.set_entry_point(

    "query_agent"
)


# =========================
# FLOW
# =========================

# Query → Schema
builder.add_edge(

    "query_agent",

    "schema_agent"
)

# Schema → Analysis
builder.add_edge(

    "schema_agent",

    "analysis_agent"
)

# Analysis → Advanced Analysis
builder.add_edge(

    "analysis_agent",

    "advanced_analysis_agent"
)

# Advanced Analysis → Insight
builder.add_edge(

    "advanced_analysis_agent",

    "insight_agent"
)


# =========================
# FINAL NODE
# =========================

builder.set_finish_point(

    "insight_agent"
)


# =========================
# COMPILE GRAPH
# =========================

graph = builder.compile()