# Level 1: Basic Local LLM with Docker Model Runner

This is the foundational level demonstrating how to create a simple AI agent using Docker's Model Runner with a local LLM. This level shows the basics of local AI agent development.

## 🎯 What This Level Demonstrates

- **Basic Local LLM Integration**: Using Docker Model Runner with Gemma3 4B
- **Simple Tool Integration**: Basic Python function as a tool
- **Web Interface**: FastAPI-based chat interface
- **No External Dependencies**: Runs completely locally

## 🚀 Features

- Simple web-based chat with an AI assistant
- Runs completely locally using Docker Model Runner  
- No external API keys required
- Uses Google's ADK framework with web interface
- Interactive browser-based chat
- Basic time-telling functionality

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
- Provides a web interface using ADK's built-in FastAPI integration
- The model (Gemma3 4B) runs entirely on your local machine
- No internet connection required after initial model download
- Basic tool integration with a simple Python function

## 🎯 Key Differences from Other Levels

- **Level 1**: Basic local LLM + simple Python tools
- **Level 2**: Adds MCP Gateway for external tool integration
- **Level 3**: Multi-agent system with specialized sub-agents

## 📁 File Structure

- `time-agent/agent.py` - Agent definition with basic tool integration
- `compose.yaml` - Docker configuration with model runner
- `Dockerfile` - Container setup
- `requirements.txt` - Python dependencies

## 🔍 What You'll Learn

- How to set up a basic local LLM agent
- Docker Model Runner integration
- Basic tool function implementation
- Web interface for AI interaction
- Local AI development workflow

## 🎮 Try This

Ask the agent questions like:
- "What time is it in New York?"
- "Can you tell me the current time in New York?"
- "What's the time in NYC?"

This level focuses on the fundamentals of local AI agent development with Docker. 