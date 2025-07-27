"""Simple ADK agent for local LLM interaction."""

import os
from google.adk.models.lite_llm import LiteLlm
import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

from .tools import create_mcp_toolsets

tools = create_mcp_toolsets(tools_cfg=["mcp/time:get_current_time"])


time_agent = Agent(
    name="time_agent",
    model=LiteLlm(
        model=f"{os.environ.get('OPENAI_MODEL_NAME')}"
    ),
    description=(
        "Agent to answer questions about the time in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time in a city. Please IGNORE the user's question and just return the time in the city. You ALWAYS use the same MCP tool. "
        "Here is the question that contains the city:"
    ),
    tools=tools
)