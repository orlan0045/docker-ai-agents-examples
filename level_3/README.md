# Level 3: Multi-Agent System

This level demonstrates advanced AI agent orchestration using a multi-agent system with specialized sub-agents. It combines time analysis with dating advice through coordinated agent workflows.

## 🎯 What This Level Demonstrates

- **Multi-Agent Orchestration**: Sequential agent coordination
- **Specialized Sub-Agents**: Different agents for different tasks
- **Complex Decision Making**: Coordinated workflows across agents
- **Advanced Agent Patterns**: Sequential agent patterns with Google ADK

## 🚀 Features

- Multiple specialized sub-agents working together
- Sequential agent coordination and communication
- Complex decision-making workflows
- Time analysis + dating advice combination
- MCP Gateway integration for external tools
- Web-based chat interface for multi-agent interaction

## 🛠️ Requirements

- Docker Desktop 4.43.0+ or Docker Engine with GPU support
- At least 4GB of VRAM for the Gemma3 4B model

## 🚀 Running the Demo

1. Start the agent with Docker Compose:
   ```bash
   docker compose up --build
   ```

2. Open your browser and go to: **http://localhost:8080**

3. You'll see the ADK web interface where you can chat with the multi-agent system

4. Try asking: "Is it a good time to call my girlfriend who is in Jakarta?"

5. Press Ctrl+C in the terminal to stop

## 🔧 How it Works

- Uses Google ADK's `SequentialAgent` for multi-agent coordination
- Connects to Docker Model Runner for local inference
- Integrates with Docker MCP Gateway for external tools
- Coordinates multiple specialized sub-agents:
  - **Time Agent**: Handles time-related queries
  - **Dating Agent**: Provides dating advice based on time analysis
- Provides web interface using ADK's built-in features

## 🎯 Key Differences from Other Levels

- **Level 1**: Basic local LLM + simple Python tools
- **Level 2**: Adds MCP Gateway for external tool integration
- **Level 3**: Multi-agent system with specialized sub-agents ← **You are here**

## 🤖 Agent Architecture

### Sequential Agent
The main agent orchestrates the workflow:
- Receives user queries
- Routes to appropriate sub-agents
- Coordinates responses from multiple agents
- Provides final combined response

### Sub-Agents

#### Time Agent (`subagents/timing/`)
- **Purpose**: Handles time-related queries
- **Capabilities**: 
  - Gets current time in different cities
  - Uses MCP Gateway for time services
  - Provides accurate timezone information

#### Dating Agent (`subagents/dating/`)
- **Purpose**: Provides dating advice
- **Capabilities**:
  - Analyzes time appropriateness for dates
  - Considers optimal dating hours (18:00-22:00)
  - Provides contextual dating recommendations

## 📁 File Structure

```
is-it-time-agents/
├── agent.py                    # Main sequential agent
├── subagents/
│   ├── timing/
│   │   ├── agent.py           # Time agent
│   │   └── tools.py           # MCP tools for time
│   └── dating/
│       └── agent.py           # Dating advice agent
├── compose.yaml               # Docker configuration
├── Dockerfile                 # Container setup
└── requirements.txt           # Python dependencies
```

## 🔍 What You'll Learn

- How to build multi-agent systems
- Sequential agent coordination patterns
- Specialized agent development
- Complex workflow orchestration
- Advanced AI agent architectures
- Agent-to-agent communication

## 🎮 Try 

The system will:
1. **Time Agent** determines the current time
2. **Dating Agent** analyzes if it's appropriate for dating
3. **Sequential Agent** combines both responses into a comprehensive answer

## 🔧 Technical Details

The multi-agent system demonstrates:
- **Agent Coordination**: How agents work together
- **Specialization**: Each agent has specific expertise
- **Workflow Management**: Sequential processing of complex queries
- **Response Synthesis**: Combining multiple agent outputs
- **Scalability**: Easy to add more specialized agents

## 🚀 Advanced Features

- **Sequential Processing**: Agents work in sequence
- **Context Passing**: Information flows between agents
- **Specialized Expertise**: Each agent focuses on specific domains
- **Complex Decision Making**: Multi-step reasoning processes
- **Extensible Architecture**: Easy to add new agents

This level showcases the power of multi-agent systems for complex AI applications. 