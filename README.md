# Trix - AI Assistant with GLaDOS Personality

A Python-based AI assistant that channels the iconic personality of GLaDOS from Portal. Built with FastAPI for the backend and integrated with the Groq API for natural language processing.

## Features

- 🤖 GLaDOS-inspired personality with sarcastic, passive-aggressive responses
- 💬 Interactive CLI interface with rich text formatting
- 🧠 Powered by Groq's LLM API (supporting various models)
- 🔄 Conversation history management
- 🎭 Configurable personality traits
- 🎨 Beautiful blue-themed interface

## Prerequisites

- Python 3.8 or higher
- A Groq API key (get one at [https://console.groq.com](https://console.groq.com))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Trix.git
cd Trix
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Set up your Groq API key:
   - Open `backend/llm_handler.py`
   - Replace the `GROQ_API_KEY` value with your actual API key

## Usage

1. Start the CLI interface:
```bash
cd backend
python trix_cli.py
```

2. Available commands:
- `/clear` - Clear conversation history
- `/history` - Show conversation history
- `/personality` - Display personality traits
- `/exit` - Exit the program

## Project Structure

```
Trix/
├── backend/
│   ├── llm_handler.py      # Groq API integration
│   ├── personality_config.py # GLaDOS personality configuration
│   ├── trix_cli.py         # CLI interface
│   └── requirements.txt     # Python dependencies
├── frontend/               # Reserved for future web interface
└── README.md
```

## Personality Configuration

The AI assistant's personality is configured in `backend/personality_config.py`. It includes:
- Core personality traits
- Conversation style settings
- Behavioral guidelines
- Response patterns
- Error handling responses

## Models Available

The following Groq models are supported:
- llama-3.3-70b-versatile (Latest Llama 3.3 70B model)
- llama-3.1-8b-instant (Fast Llama 3.1 8B model)
- llama3-8b-8192 (Default Llama 3 8B model)
- gemma2-9b-it (Gemma 2 9B model)

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by GLaDOS from Portal
- Built with [Groq](https://groq.com/) for LLM capabilities
- Uses [Rich](https://github.com/Textualize/rich) for terminal formatting

## Disclaimer

This is a fan project and is not affiliated with Valve Corporation or the Portal franchise. GLaDOS personality is inspired by but not directly copied from the Portal games.
