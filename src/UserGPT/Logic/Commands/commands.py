from src.imports import *
from src.UserGPT.Logic.Commands.local_commands import *
from src.UserGPT.Logic.Commands.tools import *

commands_map = {
    'run_win_cli': run_win_cli,
    'make_http_request': make_http_request,
    'stop_execution': stop_execution,
}

def run_function(function_name: str, arguments: dict[str, str]) -> tuple[str, dict[str, str], str]:
    function_result = commands_map[function_name](**arguments) if function_name in commands_map else f'Function {function_name} not found'
    return function_name, arguments, function_result

def parse_tool_calls(tool_calls: list[RequiredActionFunctionToolCall]) -> Iterable[ToolOutput]:
    results = []
    for tool_call in tool_calls:
      function_name = tool_call.function.name
      function_arguments = loads(tool_call.function.arguments) if tool_call.function.arguments else {}
      _, _, result = run_function(function_name, function_arguments)
      results.append(ToolOutput(output=result, tool_call_id=tool_call.id))
    return results
