"""Simple ADK agent for local LLM interaction."""

import os
from google.adk.models.lite_llm import LiteLlm
import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

from .tools import create_mcp_toolsets

tools = create_mcp_toolsets(tools_cfg=["mcp/time:get_current_time"])


root_agent = Agent(
    name="time_agent",
    model=LiteLlm(
        model=f"{os.environ.get('OPENAI_MODEL_NAME')}"
    ),
    description=(
        "Agent to answer questions about the time in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time in a city. "
        "You are using MCP Gateway to get the current time in a city. You are always using the same MCP tool."
    ),
    tools=tools,
)