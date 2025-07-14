from typing import TypedDict

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import StateGraph

from .openai import get_response


class AgentState(TypedDict):
    """
    Represents the state of the agent.
    """

    messages: list[HumanMessage | AIMessage | SystemMessage]


def process(state: AgentState) -> AgentState:
    """Node that responds to the user query with a appropriate response."""

    if not state["messages"]:
        raise ValueError("No messages in the state to process.")

    response = get_response(state["messages"])
    state["messages"].append(AIMessage(content=response))
    return state


graph = StateGraph(AgentState)

graph.add_node("process", process)
graph.set_entry_point("process")

agent = graph.compile()
