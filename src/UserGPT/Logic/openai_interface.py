from src.imports import *

def ask_gpt(model: Model, history: Iterable[ChatCompletionMessageParam] = [], tools: Iterable[ChatCompletionToolParam] = []) -> ChatCompletion:
    print(f'Asking {model.value}...')
    result = client.chat.completions.create(
        model=model.value,
        messages=history,
        tools=tools
    )
    return result

def get_message_content(response: ChatCompletion) -> str | None:
    message = response.choices[0].message
    return message.content

def get_tool_calls(response: ChatCompletion) -> Iterable[ChatCompletionMessageToolCall] | None:
    message = response.choices[0].message
    return message.tool_calls

def get_function_names(tool_calls: Iterable[ChatCompletionMessageToolCall]) -> Iterable[str]:
    return [tool_call.function.name for tool_call in tool_calls]
