from src.imports import *

tool_run_win_cli_function_parameters: FunctionParameters = dict(
    type='object',
    properties={
        'command': {
            'type': 'string',
            'description': 'The command to run in the Windows CLI'
        }
    },
    required=['command']
)

tool_run_win_cli_definition: FunctionDefinition = FunctionDefinition(
    name='run_win_cli',
    description='Run a command in the Windows CLI',
    parameters=tool_run_win_cli_function_parameters
)

tool_run_win_cli: ToolFunction = ToolFunction(
    function=tool_run_win_cli_definition,
    type="function"
)

tool_make_http_request_function_parameters: FunctionParameters = dict(
    type='object',
    properties={
        'url': {
            'type': 'string',
            'description': 'The URL to make the request to'
        },
        'method': {
            'type': 'string',
            'description': 'The HTTP method to use'
        },
        'headers': {
            'type': 'object',
            'description': 'The headers to include in the request'
        },
        'body': {
            'type': 'string',
            'description': 'The body of the request'
        }
    },
    required=['url', 'method']
)

tool_make_http_request_definition: FunctionDefinition = FunctionDefinition(
    name='make_http_request',
    description='Make an HTTP request',
    parameters=tool_make_http_request_function_parameters
)

tool_make_http_request: ToolFunction = ToolFunction(
    function=tool_make_http_request_definition,
    type="function"
)

tool_stop_execution_parameters: FunctionParameters = dict(
    type='object',
    properties={
        'reason': {
            'type': 'string',
            'description': 'The reason for stopping the execution'
        }
    }
)

tool_stop_execution_definition: FunctionDefinition = FunctionDefinition(
    name='stop_execution',
    description='Stop the execution of the assistant',
    parameters=tool_stop_execution_parameters
)

tool_stop_execution: ToolFunction = ToolFunction(
    function=tool_stop_execution_definition,
    type="function"
)

tools: Iterable[ToolFunction] = [
    tool_run_win_cli,
    tool_make_http_request,
    tool_stop_execution
]
