from typing import Literal, TypedDict

from langgraph.graph import StateGraph


class AgentState(TypedDict):
    """
    Represents the state of the agent.
    """

    name: str
    numbers: list[int]
    operation: Literal["+", "-", "*", "/"]
    result: str


def process(state: AgentState) -> AgentState:
    """
    A simple processing function that modifies the state.
    """
    result = (0, "sum")
    if state["operation"] == "+":
        result = (sum(state["numbers"]), "sum")
    elif state["operation"] == "-":
        s = state["numbers"][0]
        for n in state["numbers"][1:]:
            s -= n
        result = (s, "subtraction")
    elif state["operation"] == "*":
        m = 1
        for n in state["numbers"]:
            m *= n
        result = (m, "multiplication")
    elif state["operation"] == "/":
        d = state["numbers"][0]
        for n in state["numbers"][1:]:
            d /= n
        result = (d, "division")
    state["result"] = f"The {result[1]} of {state['numbers']} is {result[0]}"
    return state


graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.set_entry_point("process")


app = graph.compile()

initial_state = AgentState(name="Benjamin", numbers=[1, 2, 3, 4], operation="-", result="")

result = app.invoke(initial_state)

print(result["result"])  # Output: The subtraction of [1, 2, 3, 4] is -8
