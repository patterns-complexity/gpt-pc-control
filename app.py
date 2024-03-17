from src.imports import *

from src.UserGPT.types import *
from src.UserGPT.UI.cli import *
from src.UserGPT.Logic.history_management import *
from src.UserGPT.Logic.commands import *
from src.UserGPT.Logic.openai_interface import *

def main(state: dict[str, Any]) -> None:
    # Reset the conversation context
    reset_context('context.txt')

    while not state['should_quit']:
        # Reset the ask_user variable
        state['ask_user'] = False

        # Ask for user input
        user_input = prompt_user('You: > ')

        # Check if the user wants to quit
        if state['should_quit']:
            break

        # Add user input to history
        add_to_history(ChatRole.USER, user_input)

        # Reset the loop count
        loop_count = 0

        # Start the inner loop
        while not state['ask_user']:
          # Increment the loop count
          loop_count += 1

          # Set the model
          model = Model.GPT_4_TURBO

          # Set the model to GPT-3.5 Turbo if the loop count is greater than 1
          if loop_count > 1:
            model = Model.GPT_3_5_INSTRUCTIONS

          # Get response from GPT
          sanitize_history()
          response = ask_gpt(model, history=state['history'], tools=tools)
          message_content = get_message_content(response)
          tool_calls = get_tool_calls(response)

          if message_content is not None:
            # Print response from GPT
            print_with_color(f'Assistant: > {message_content}', CLIColor.GREEN)

            # Add response to history
            add_to_history(ChatRole.ASSISTANT, message_content)

          # Parse tool calls
          if tool_calls and len(list(tool_calls)) > 0:
            add_to_history(ChatRole.ASSISTANT, f'Running functions: {", ".join(get_function_names(tool_calls))}...')
            tool_calls_results = parse_tool_calls(tool_calls)
            history_message = ''
            for function_name, arguments, function_result in tool_calls_results:
              history_message += f'Function:\n`{function_name}`\nRan with arguments:\n`{str(arguments)}`\nReturned:\n`{function_result}`\n'
            add_to_history(ChatRole.SYSTEM, history_message)
            print_with_color(history_message, CLIColor.BLUE)

          add_to_history(
            ChatRole.SYSTEM,
            '''User has received the above responses.
            Remember that user can't see command outputs, so you have to summarize the output in the response.
            Otherwise, the user won't know what happened.
            If the Assistant has nothing more to do, he should use the `stop_execution` tool call.'''
          )

if __name__ == '__main__':
  main(state)