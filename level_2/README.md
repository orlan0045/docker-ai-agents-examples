# Level 2: Local LLM + Docker MCP Gateway

This level builds upon Level 1 by adding Docker's MCP (Model Context Protocol) Gateway, demonstrating how to integrate external tools and services through the MCP protocol.

## 🎯 What This Level Demonstrates

- **Enhanced Tool Integration**: Using MCP Gateway for external tool access
- **Protocol-Based Communication**: MCP protocol for tool communication
- **External Service Integration**: Access to external time services
- **Robust Tool Management**: Better tool discovery and management

## 🚀 Features

- Same time-telling functionality as Level 1
- Enhanced with MCP (Model Context Protocol) Gateway
- External tool integration through MCP
- More robust tool management
- Web-based chat interface
- Local LLM with external tool capabilities

## 🛠️ Requirements

- Docker Desktop 4.43.0+ or Docker Engine with GPU support
- At least 4GB of VRAM for the Gemma3 4B model

## 🚀 Running the Demo

1. Start the agent with Docker Compose:
   ```bash
   docker compose up --build
   ```

2. Open your browser and go to: **http://localhost:8080**

3. You'll see the ADK web interface where you can chat with the agent

4. Try asking: "What time is it in New York?"

5. Press Ctrl+C in the terminal to stop

## 🔧 How it Works

- Uses Google ADK's `Agent` class with `LiteLlm` model
- Connects to Docker Model Runner for local inference
- Integrates with Docker MCP Gateway for external tools
- Uses MCP protocol for tool communication
- Provides web interface using ADK's built-in features
- External time service integration through MCP

## 🎯 Key Differences from Other Levels

- **Level 1**: Basic local LLM + simple Python tools
- **Level 2**: Adds MCP Gateway for external tool integration ← **You are here**
- **Level 3**: Multi-agent system with specialized sub-agents

## 🔍 MCP Gateway Integration

This level introduces the MCP (Model Context Protocol) Gateway, which:
- Enables communication with external tools and services
- Provides standardized protocol for tool integration
- Allows for more sophisticated tool management
- Supports external service discovery

## 📁 File Structure

- `time-agent/agent.py` - Agent definition with MCP tool integration
- `time-agent/tools.py` - MCP toolset configuration
- `compose.yaml` - Docker configuration with model runner and MCP gateway
- `Dockerfile` - Container setup
- `requirements.txt` - Python dependencies

## 🔍 What You'll Learn

- How to integrate MCP Gateway with local LLMs
- External tool integration through MCP protocol
- Enhanced tool management capabilities
- Protocol-based AI agent development
- Docker MCP Gateway configuration

## 🎮 Try 

The agent now uses MCP Gateway to access external time services, providing more robust and accurate time information.

## 🔧 Technical Details

The MCP integration allows the agent to:
- Connect to external time services
- Use standardized tool protocols
- Scale to more complex tool integrations
- Maintain better tool discovery and management

This level demonstrates the power of protocol-based tool integration in AI agents. 