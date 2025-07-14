from typing import TypedDict

from langgraph.graph import StateGraph


class AgentState(TypedDict):
    """
    Represents the state of the agent.
    """

    name: str
    message: str


def greeting(state: AgentState) -> AgentState:
    """
    A simple greeting function that modifies the state.
    """
    if state["name"]:
        state["message"] = f"Hello {state['name']} from aws-agent!"
    else:
        state["message"] = "Hello from aws-agent!"
    return state


graph = StateGraph(AgentState)
graph.add_node("start", greeting)
graph.set_entry_point("start")


app = graph.compile()

initial_state = AgentState(name="Benjamin", message="")

result = app.invoke(initial_state)

print(result["message"])  # Output: Hello Benjamin from aws-agent!
