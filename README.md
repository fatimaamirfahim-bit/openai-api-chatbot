# OpenAI API Chatbot

A simple conversational chatbot built with Python and the OpenAI API (GPT-4o-mini). Features multi-turn conversation memory, meaning it remembers the full chat history for context. Built as a beginner project to learn how to integrate LLMs into real applications using the OpenAI SDK.

## Features
- Multi-turn conversation memory
- Runs directly in the terminal
- Uses GPT-4o-mini for cost efficiency
- Simple and easy to understand codebase

## Requirements
- Python 3.11+
- OpenAI API key
- OpenAI Python SDK

## Installation

1. Clone the repository
```bash
git clone https://github.com/fatimaamirfahim-bit/openai-api-chatbot.git
cd openai-api-chatbot
```

2. Install dependencies
```bash
pip install openai
```

3. Set up your OpenAI API key as an environment variable

**Windows:**
```powershell
setx OPENAI_API_KEY "your-api-key-here"
```

**Mac/Linux:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

Run the chatbot in your terminal:
```bash
python openai_chatbot.py
```

## Tech Stack
- **Language:** Python
- **API:** OpenAI API
- **Model:** GPT-4o-mini