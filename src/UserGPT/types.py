from typing import *
from enum import Enum

class ChatState(dict[str, Any]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['history'] = []
        self['should_quit'] = False
        self['ask_user'] = False

class CLIColor(Enum):
    RED = '\033[91m{text}\033[0m'
    GREEN = '\033[92m{text}\033[0m'
    YELLOW = '\033[93m{text}\033[0m'
    BLUE = '\033[94m{text}\033[0m'
    WHITE = '\033[97m{text}\033[0m'
    DEFAULT = '\033[99m{text}\033[0m'

class Model(Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_INSTRUCTIONS = "gpt-3.5-turbo-1106"
    GPT_4 = "gpt-4"
    GPT_4_TURBO = "gpt-4-0125-preview"

class ChatRole(Enum):
    USER = 'user'
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
