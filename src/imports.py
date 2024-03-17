import subprocess

from typing import Any, Iterable
from json import loads

from openai.types.chat import (
  ChatCompletionToolParam,
  ChatCompletion,
  ChatCompletionMessageParam,
  ChatCompletionMessageToolCall
)

from src.UserGPT.types import *

from src.OpenAI.OpenAIClient import client

exported = {
    'Model': Model,
    'client': client,
    'subprocess': subprocess,
    'loads': loads,
    'ChatRole': ChatRole,
    'ChatCompletionToolParam': ChatCompletionToolParam,
    'ChatCompletion': ChatCompletion,
    'ChatCompletionMessageParam': ChatCompletionMessageParam,
    'ChatCompletionMessageToolCall': ChatCompletionMessageToolCall,
    'Any': Any,
    'Iterable': Iterable
}