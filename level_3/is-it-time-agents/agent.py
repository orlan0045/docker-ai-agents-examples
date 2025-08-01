# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""LLM Auditor for verifying & refining LLM-generated answers using the web."""

from google.adk.agents import SequentialAgent

from .subagents.dating import dating_agent
from .subagents.timing import time_agent

root_agent = SequentialAgent(
    name="is_it_time_agent",
    description=(
        "Agent to answer questions about the time and is it ok to go on an online date with my girlfriend."
    ),
    sub_agents=[time_agent, dating_agent]
)
