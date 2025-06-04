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
git clone https://github.com/Ashm1t/Trix.git
cd Trix
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Set up your Groq API key:
   - Create a `.env` file in the project root directory
   - Add your Groq API key to the file:
     ```
     GROQ_API_KEY=your_actual_groq_api_key_here
     ```
   - Replace `your_actual_groq_api_key_here` with your actual Groq API key

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
├── .env                    # API key configuration (create this file)
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

## Security Note

⚠️ **Important**: Never commit your `.env` file or share your API key. The `.env` file is included in `.gitignore` to prevent accidental exposure of sensitive information.

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
