def load_context(path: str) -> str:
    try:
      with open(path, 'r') as file:
          return file.read()
    except FileNotFoundError as e:
        print(f'System > No context message found')
        return ''
    except Exception as e:
        print(f'System > Error loading context message: {str(e)}')
        return ''
