from typing import *
from enum import Enum

from openai.types.chat import (
  ChatCompletionToolParam,
  ChatCompletion,
  ChatCompletionMessageParam,
  ChatCompletionMessageToolCall,
)

from openai.types.beta.assistant import Tool, Assistant, ToolFunction
from openai.types.shared import FunctionDefinition, FunctionParameters
from openai.types.beta.thread_create_params import Message
from openai.types.beta.thread import Thread
from openai.types.beta.threads.thread_message import ThreadMessage
from openai.types.beta.threads import Run, RequiredActionFunctionToolCall, MessageContentText
from openai.types.beta.threads.message_content_text import Text as MessageText
from openai.types.beta.threads.run_submit_tool_outputs_params import ToolOutput


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
    GPT_4 = "gpt-4"
    GPT_4_TURBO = "gpt-4-turbo-preview"

class ChatRole(Enum):
    USER = 'user'
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
