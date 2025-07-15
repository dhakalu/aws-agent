"""
A simple calculator agent implemented using LangGraph and OpenAI's GPT-4.1 model.
This agent can perform basic arithmetic operations like addition and subtraction.

The purpose of this agent is to demonstrate how to build a ReAct-based calculator using LangGraph and OpenAI's API.

ReAct is a design patterns combines (Re)asoning and (Act)ion to allow agents to interact with their environment effectively.
"""

import os
from collections.abc import Sequence
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI as OpenAI
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

load_dotenv()


model = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.getenv("GITHUB_TOKEN"),
    model="openai/gpt-4o-mini",
)


class AgentState(TypedDict):
    """
    Represents the state of the calculator agent.
    """

    messages: Annotated[Sequence[BaseMessage], add_messages]


@tool(
    description="Adds two numbers together.",
)
def add(a: float, b: float) -> float:
    """
    Adds two numbers together.
    s
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The sum of the two numbers.
    """
    return a + b


@tool(
    description="Subtracts the second number from the first.",
)
def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first.
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The result of the subtraction.
    """
    return a - b


def model_call(state: AgentState) -> AgentState:
    """
    Node that responds to the user query with an appropriate response.
    """
    if not state["messages"]:
        raise ValueError("No messages in the state to process.")

    response = model_with_tools.invoke(
        input=state["messages"],
    )
    if not isinstance(response, AIMessage):
        raise ValueError("Response is not of type AIMessage.")
    return {"messages": [response]}


def next_node(state: AgentState) -> str:
    """Determine the next node based on the last message in the state."""
    if not state["messages"]:
        raise ValueError("No messages in the state to process.")

    last_message = state["messages"][-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "tools"


tools = [add, subtract]
model_with_tools = model.bind_tools(tools)

graph = StateGraph(AgentState)

graph.add_node("model_call", model_call)
graph.add_node("tools", ToolNode(tools=tools))
graph.set_entry_point("model_call")

graph.add_conditional_edges(
    "model_call",
    next_node,
    {
        "tools": "tools",
        "end": END,
    },
)
graph.add_edge("tools", "model_call")  # Loop back to model_call after tool use
agent = graph.compile()


def print_stream(stream):
    for response in stream:
        if "model_call" in response:
            # Print the last message from the model call
            print(response["model_call"]["messages"][-1].content)
        elif "tools" in response:
            print(f"using tool {response['tools']['messages'][-1].name}...")
        else:
            print(response)


if __name__ == "__main__":
    system_prompt = SystemMessage(
        content="""
    You are a calculator that can perform basic arithmetic operations like addition and subtraction.
    You can add and subtract two numbers provided by the user.
    """
    )
    print("Welcome to the Calculator CLI! Type 'exit' to quit.")

    current_state = {"messages": [system_prompt]}

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        stream = agent.stream(
            {"messages": current_state["messages"] + [HumanMessage(content=user_input)]},
            stream_mode="updates",
        )
        print_stream(stream)
