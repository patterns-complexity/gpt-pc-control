from src.imports import *
from src.state import state

def stop_execution(reason: str = '') -> str:
    state['ask_user'] = True
    return f'Execution stopped. Reason: {reason}.'

def run_win_cli(command: str) -> str:
    return subprocess.run(command, shell=True, capture_output=True, text=True, timeout=1000).stdout

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

commands = {
    'stop_execution': stop_execution,
    'run_win_cli': run_win_cli
}

def run_function(function_name: str, arguments: dict[str, str]) -> tuple[str, dict[str, str], str]:
    function_result = commands[function_name](**arguments) if function_name in commands else f'Function {function_name} not found'
    return function_name, arguments, function_result

def parse_tool_calls(tool_calls: Iterable[ChatCompletionMessageToolCall]) -> list[tuple[str, dict[str, str], str]]:
    results = []
    for tool_call in tool_calls:
      function_name = tool_call.function.name
      arguments = loads(tool_call.function.arguments) if tool_call.function.arguments else {}
      results.append(run_function(function_name, arguments))
    return results
