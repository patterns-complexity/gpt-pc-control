from typing import Iterable
from openai.types.chat import ChatCompletionToolParam

tools: Iterable[ChatCompletionToolParam] = [
    {
        "type": "function",
        "function": {
            "name": "run_win_cli",
            "description": "Run a command in a Windows command line",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command to run in the Windows command line"
                    }
                },
                "required": ["command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "stop_execution",
            "description": '''Stop the execution of the conversation. By default the conversation is executed in a loop without user input. You can stop the execution at any time by calling this function.
            Use this function when:
            - You have fulfilled the user's request
            - You have encountered an error and don't know how to fix it
            - Further actions are dangerous and require user input''',
            "parameters": {
                "type": "object",
                "properties": {
                    "reason": {
                        "type": "string",
                        "description": "The reason for stopping the execution"
                    },
                },
                "required": ["reason"],
            },
        },
    },
]
