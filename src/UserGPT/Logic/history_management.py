from src.imports import *
from src.state import state

def sanitize_history() -> None:
    current_history = list(state['history'])
    for index in range(len(current_history)):
      if len(current_history[index]['content']) > 16000:
        current_history[index]['content'] = current_history[index]['content'][:16000]
        current_history[index]['content'] += '...[Content truncated to first 16k characters]'
    state['history'] = current_history

def add_to_history(role: ChatRole, content: str):
    state['history'].append({
        'role': role.value,
        'content': content
    })

def reset_context(path: str):
    try:
      with open(path, 'r') as file:
          state['history'] = [{'role': ChatRole.SYSTEM.value, 'content': file.read()}]
    except FileNotFoundError as e:
        print(f'System > No context message found')
    except Exception as e:
        print(f'System > Error loading context message: {str(e)}')
