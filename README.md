# AI Docker Demo

This project demonstrates the evolution of AI agents using Docker's new AI features, showcasing different levels of complexity and capabilities.

## Overview

This demo showcases how to build AI agents using Docker's Model Runner and MCP (Model Context Protocol) Gateway. The project is organized into three levels, each demonstrating progressively more advanced AI capabilities:

- **Level 1**: Basic local LLM with Docker Model Runner
- **Level 2**: Local LLM + Docker MCP Gateway for enhanced tooling
- **Level 3**: Multi-agent system with specialized sub-agents

## 🚀 Quick Start

Each level can be run independently. Navigate to any level directory and run:

```bash
docker compose up --build
```

Then open your browser to `http://localhost:8080` to interact with the AI agent.

## 📁 Project Structure

```
docker-ai-demo/
├── level_1/          # Basic local LLM with Docker Model Runner
├── level_2/          # Local LLM + Docker MCP Gateway
└── level_3/          # Multi-agent system
```

## 🎯 Level Descriptions

### Level 1: Basic Local LLM
**Location**: `level_1/`

- **Technology**: Docker Model Runner + Google ADK
- **Features**: 
  - Simple time-telling agent
  - Local LLM inference (no external APIs)
  - Basic tool integration
  - Web interface for interaction
- **Use Case**: Demonstrates basic local AI agent capabilities

### Level 2: Enhanced with MCP Gateway
**Location**: `level_2/`

- **Technology**: Docker Model Runner + Docker MCP Gateway + Google ADK
- **Features**:
  - Same time-telling functionality as Level 1
  - Enhanced with MCP (Model Context Protocol) Gateway
  - External tool integration through MCP
  - More robust tool management
- **Use Case**: Shows how to integrate external tools and services

### Level 3: Multi-Agent System
**Location**: `level_3/`

- **Technology**: Docker Model Runner + Docker MCP Gateway + Google ADK Sequential Agent
- **Features**:
  - Multiple specialized sub-agents
  - Sequential agent coordination
  - Complex decision-making workflows
  - Time analysis + dating advice combination
- **Use Case**: Demonstrates advanced multi-agent orchestration

## 🛠️ Requirements

- Docker Desktop 4.43.0+ or Docker Engine with GPU support
- At least 4GB of VRAM for the Gemma3 4B model
- No external API keys required (runs completely locally)

## 🔧 Technical Stack

- **AI Framework**: Google ADK (Agent Development Kit)
- **Local LLM**: Gemma3 4B via Docker Model Runner
- **Protocol**: MCP (Model Context Protocol) Gateway
- **Web Interface**: FastAPI-based chat interface
- **Containerization**: Docker Compose

## 🎮 Interactive Demo

Each level provides a web-based chat interface where you can:

1. Ask questions about time in different cities
2. Get AI-powered responses from local models
3. Experience different levels of agent sophistication
4. See how tools and multi-agent systems work

## 🚀 Getting Started

1. **Choose a level** to start with (recommended: start with Level 1)
2. **Navigate to the level directory**:
   ```bash
   cd level_1  # or level_2, level_3
   ```
3. **Start the demo**:
   ```bash
   docker compose up --build
   ```
4. **Open your browser** to `http://localhost:8080`
5. **Start chatting** with the AI agent!

## 📚 Learning Path

1. **Start with Level 1** to understand basic local LLM integration
2. **Move to Level 2** to see how MCP Gateway enhances capabilities
3. **Explore Level 3** to understand multi-agent orchestration

## 🔍 Key Features Demonstrated

- **Local AI**: No external API dependencies
- **Docker Integration**: Seamless containerized AI workloads
- **Tool Integration**: From basic functions to external MCP tools
- **Multi-Agent**: Complex agent coordination and workflows
- **Web Interface**: User-friendly chat interface
- **Scalability**: Easy to extend and modify

## 🤝 Contributing

This demo is designed to be educational and extensible. Feel free to:
- Modify agent behaviors
- Add new tools and capabilities
- Create your own levels
- Experiment with different models

## 📄 License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details. 