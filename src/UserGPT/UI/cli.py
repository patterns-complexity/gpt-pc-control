from src.imports import *
from src.state import state

def print_with_color(text: str, color: CLIColor) -> None:
    print(color.value.format(text=text))
    print(CLIColor.DEFAULT.value.format(text=''))

def prompt_user(prompt: str) -> str:
    user_input = input(prompt)
    if user_input == 'q':
        state['ask_user'] = True
        state['should_quit'] = True
    elif not user_input or user_input.isspace() or user_input == '':
        return '[User confirmed no input]'
    return user_input
