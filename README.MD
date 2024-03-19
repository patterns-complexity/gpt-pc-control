# Windows CLI Assistant - GPT-PC-Control

## Overview

This Windows CLI Assistant is a powerful, interactive tool designed to enhance productivity and facilitate a seamless interaction between end-users, the Windows CLI and OpenAI GPT models through an intuitive interface.

## Features

- **CLI Command Execution**: Run Windows CLI commands directly through the chat interface.
- **HTTP Requests**: Easily make GET or POST requests and receive responses in conversation.
- **Python Code Execution**: Execute Python code snippets on the fly for rapid testing and development.
- **Custom Tool Integration**: Extend functionality by integrating custom tools and commands.

## Getting Started

To get started with the Windows CLI Assistant, follow these simple steps:

### Prerequisites

- Ensure you have Python installed on your system. This project was tested with Python 3.10, you can try running it on other versions but your mileage may vary.
- Additionally, you'll need to set up an OpenAI API key and Organization ID. These can be obtained by creating an account on OpenAI's platform.

### Installation

1. **Clone the repository** to your local machine using Git:

```bash
git clone git@github.com:patterns-complexity/gpt-pc-control.git
```

2. **Navigate** into the project directory:

```bash
cd gpt-pc-control
```

3. **Install dependencies** by running:

```bash
pip install -r requirements.txt
```

4. **Create a** `.env` **file** in the project root with the following variables or move the `.env.dist` file to `.env` and fill in the required values:

```
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_ORGANIZATION=your_organization_id_here
ASSISTANT_ID=optional_assistant_id_here
```

### Usage

To start the assistant, run:

```bash
python app.py
```

Once the assistant is running, follow the interactive prompts. You can execute CLI commands, make HTTP requests, or run Python code by typing your request into the chat interface.

**Example Usage**:

- Everything is controlled through the chat interface. You can type your request in natural, English (or basically any) language and the assistant will respond accordingly.

### Extending Functionality

You can extend the assistant's functionalities by adding new tools and commands in the `src/UserGPT/Logic/Commands` directory. Refer to existing commands for implementation patterns.

## Support

For issues, feature requests, or contributions, please open an issue or pull request in the project's GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
