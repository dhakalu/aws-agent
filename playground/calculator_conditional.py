from typing import Literal, TypedDict

from langgraph.graph import StateGraph


class AgentState(TypedDict):
    """
    Represents the state of the agent.
    """

    name: str
    message: str
    numbers: list[int]
    operation: Literal["+", "-", "*", "/"]


def greeting(state: AgentState) -> AgentState:
    """
    A simple greeting function that modifies the state.
    """
    if state["name"]:
        state["message"] = f"Hello {state['name']} from aws-agent!"
    else:
        state["message"] = "Hello from aws-agent!"
    return state


def adder(state: AgentState) -> AgentState:
    """
    A function that adds numbers and modifies the state accordingly.
    """
    total = sum(state["numbers"])
    state["message"] += f" The sum of {state['numbers']} is {total}."
    return state


def subtractor(state: AgentState) -> AgentState:
    """
    A function that subtracts numbers and modifies the state accordingly.
    """
    result = state["numbers"][0]
    for n in state["numbers"][1:]:
        result -= n
    state["message"] += f" The subtraction of {state['numbers']} is {result}."
    return state


def router(state: AgentState) -> str:
    """
    A function that routes the state to the appropriate operation.
    """
    if state["operation"] == "+":
        return "adder"
    elif state["operation"] == "-":
        return "subtractor"
    return "unknown"


graph = StateGraph(AgentState)
graph.add_node("greet", greeting)
graph.add_node("add", adder)
graph.add_node("subtract", subtractor)
graph.set_entry_point("greet")

graph.add_conditional_edges(
    "greet",
    [
        ("add", lambda s: s["operation"] == "+"),
        ("subtract", lambda s: s["operation"] == "-"),
    ],
)
