from typing import TypedDict

from langgraph.graph import StateGraph


class AgentState(TypedDict):
    """
    Represents the state of the agent.
    """

    name: str
    agr: int
    skills: list[str]
    message: str


def greeter(state: AgentState) -> AgentState:
    """
    A simple greeting function that modifies the state.
    """
    if state["name"]:
        state["message"] = f"Hello {state['name']}!"
    else:
        state["message"] = "Hello there!"
    return state


def age_checker(state: AgentState) -> AgentState:
    """
    A function that checks the age and modifies the state accordingly.
    """
    if state["agr"] < 18:
        state["message"] += " You are a minor."
    else:
        state["message"] += " You are an adult."
    return state


def skills_checker(state: AgentState) -> AgentState:
    """
    A function that checks the skills and modifies the state accordingly.
    """
    if state["skills"]:
        state["message"] += f" Your skills are: {', '.join(state['skills'])}."
    else:
        state["message"] += " You have no skills listed."
    return state


graph = StateGraph(AgentState)
graph.add_node("greet", greeter)
graph.add_node("check_age", age_checker)
graph.add_node("check_skills", skills_checker)
graph.set_entry_point("greet")

graph.add_edge("greet", "check_age")
graph.add_edge("check_age", "check_skills")

app = graph.compile()

initial_state = AgentState(name="Benjamin", agr=20, skills=["Python", "AWS"], message="")
result = app.invoke(initial_state)
print(result["message"])  # Output: Hello Benjamin! You are an adult. Your skills are: Python, AWS.
