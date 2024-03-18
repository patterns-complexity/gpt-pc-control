from src.imports import *
from src.UserGPT.UI.cli import *

def create_assistant(
    model: Model,
    name: str = '',
    description: str = '',
    instructions: str = '',
    tools: Iterable[Tool] = []
) -> str:
    assistant = client.beta.assistants.create(
        name=name,
        description=description,
        instructions=instructions,
        tools=tools,
        model=model.value,
    )
    return assistant.id

def list_assistants() -> Iterable[Assistant]:
    assistants = client.beta.assistants.list()
    return assistants.data

def create_thread(assistant_id: str, messages: Iterable[Message] = []) -> Thread:
    return client.beta.threads.create(messages=messages)

def create_message(thread: Thread, content: str) -> ThreadMessage:
    thread_id = thread.id
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role='user',
        content=content,
    )

def create_run(thread: Thread, assistant_id: str) -> Run:
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

def fetch_run(run: Run, thread: Thread) -> Run:
    return client.beta.threads.runs.retrieve(
        run_id=run.id,
        thread_id=thread.id,
    )

def submit_tool_outputs(run: Run, thread: Thread, tool_outputs: Iterable[ToolOutput]) -> Run:
    return client.beta.threads.runs.submit_tool_outputs(
        run_id=run.id,
        thread_id=thread.id,
        tool_outputs=tool_outputs,
    )

def list_thread_messages(thread: Thread) -> Iterable[ThreadMessage]:
    return client.beta.threads.messages.list(thread_id=thread.id).data

def get_all_message_texts(thread: Thread, assistant_message_color: CLIColor = CLIColor.WHITE, user_message_color: CLIColor = CLIColor.GREEN) -> Iterable[str]:
    thread_messages: Iterable[ThreadMessage] = list_thread_messages(thread)
    all_texts = []
    for message in thread_messages:
        message_content: MessageContentText = MessageContentText.parse_obj(message.content[0])
        message_content_txt: MessageText = MessageText.parse_obj(message_content.text)
        assistant_prompt: str = assistant_message_color.value.format(text='Assistant: >')
        user_prompt: str = user_message_color.value.format(text='You: >')
        role: str = message.role
        all_texts.append(
            f"{assistant_prompt if role == 'assistant' else user_prompt} {message_content_txt.value}"
        )
    all_texts.reverse()
    return all_texts

