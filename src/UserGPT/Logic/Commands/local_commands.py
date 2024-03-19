import subprocess

from requests import request, Response

from src.state import state

def stop_execution(reason: str = '') -> str:
    state['ask_user'] = True
    return f'Execution stopped. Reason: {reason}.'

def run_win_cli(command: str) -> str:
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            return 'SUCCESS: ' + result.stdout
        return 'ERROR: ' + result.stderr
    except subprocess.TimeoutExpired:
        return 'ERROR: Command timed out'
    except subprocess.CalledProcessError as e:
        return 'ERROR: ' + str(e.stderr)
    except Exception as e:
        return 'ERROR: ' + str(e)

def run_python_code(code: str) -> str:
    try:
        with open('temp.py', 'w') as file:
            file.write(code)
        result = subprocess.run('python temp.py', shell=True, check=True, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            return 'SUCCESS: ' + result.stdout
        return 'ERROR: ' + result.stderr
    except subprocess.TimeoutExpired:
        return 'ERROR: Command timed out'
    except subprocess.CalledProcessError as e:
        return 'ERROR: ' + str(e.stderr)
    except Exception as e:
        return 'ERROR: ' + str(e)

def make_http_request(url: str, method: str, headers: dict[str, str] = {}, body: str = '') -> str:
    try:
        response: Response = request(method, url, headers=headers, data=body)
        return response.text
    except Exception as e:
        return 'ERROR: ' + str(e)
