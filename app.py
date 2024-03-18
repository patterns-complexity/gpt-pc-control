from time import sleep
from click import pause
from src.imports import *

from src.UserGPT.UI.cli import *
from src.UserGPT.Logic.context import *
from src.UserGPT.Logic.Commands.commands import *
from src.UserGPT.Logic.openai_interface import *

def process_tool_calls(run: Run, thread: Thread) -> None:
    if run.required_action is None or run.required_action.type != 'submit_tool_outputs':
        print_with_color('No tool calls to process...', CLIColor.RED)
        return
    print_with_color('Processing ChatGPT\'s request to run a function...', CLIColor.YELLOW)
    required_action = run.required_action
    tool_calls = required_action.submit_tool_outputs.tool_calls
    print_with_color('Running those functions...', CLIColor.YELLOW)
    parsed = parse_tool_calls(tool_calls)
    print_with_color('Submitting functions\' outputs...', CLIColor.GREEN)
    submit_tool_outputs(run, thread, parsed)
    for tool_output in parsed:
        print_with_color(str(tool_output), CLIColor.BLUE)

def main(state: dict[str, Any]) -> None:
    assistants: Iterable[Assistant] = list_assistants()

    print_with_color('Welcome to the Windows CLI Assistant!', CLIColor.GREEN)

    if ASSISTANT_ID not in [assistant.id for assistant in assistants]:
        print_with_color('Creating assistant...', CLIColor.YELLOW)
        assistant: str = create_assistant(
          Model.GPT_4_TURBO,
          name='Windows CLI Assistant',
          description='A Windows CLI Assistant capable of running commands in a Windows CLI',
          instructions=load_context('context.txt'),
          tools=tools
        )
        print(assistant)
        print_with_color('Assistant created!', CLIColor.GREEN)
        print_with_color('Please put this Assistant ID in your .env file:', CLIColor.GREEN)
        print_with_color(f'ASSISTANT_ID={assistant}', CLIColor.BLUE)
        return

    thread = create_thread(ASSISTANT_ID)

    print_with_color('Thread created!', CLIColor.GREEN)
    print_with_color('You can now start chatting with the assistant!', CLIColor.GREEN)
    print_with_color('Type `q` to quit the assistant.', CLIColor.GREEN)

    while not state['should_quit']:
        state['ask_user'] = False

        user_input = prompt_user('You: > ')

        if state['should_quit']:
            break

        create_message(thread, user_input)

        run = create_run(thread, ASSISTANT_ID)

        while run.status != 'completed':
            run = fetch_run(run, thread)
            if run.status == 'requires_action' and run.required_action is not None and run.required_action.type == 'submit_tool_outputs':
                print_with_color(f'Run status: running commands and submitting outputs, this might take a moment...', CLIColor.YELLOW)
                process_tool_calls(run, thread)
            elif run.status == 'completed':
                print_with_color(f'Run status: Finished!', CLIColor.GREEN)
            elif (
              run.status == 'failed'
                or run.status == 'cancelled'
                or run.status == 'cancelling'
                or run.status == 'expired'
            ):
                print_with_color(f'Run status: ERROR!', CLIColor.RED)
                break
            sleep(1)
        all_messages = get_all_message_texts(thread)
        history = '\n'.join(all_messages)
        print_with_color(history, CLIColor.WHITE)
        pause('Press Enter to continue...')


if __name__ == '__main__':
  main(state)