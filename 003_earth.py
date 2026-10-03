# Load env variables and create client
import base64
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-sonnet-4-5"
# Helper functions
from anthropic.types import Message


def add_messages(messages, message, role="user"):
    message = {"role": role, "content": message.content if isinstance(message, Message) else message}
    messages.append(message)


def chat(
    messages,
    system=None,    
    stop_sequences=[],
    tools=None,
    thinking=False,
    thinking_budget=1024,
):
    params = {
        "model": model,
        "max_tokens": 4000,
        "messages": messages,        
        "stop_sequences": stop_sequences,
    }

    if thinking:
        params["thinking"] = {
            "type": "enabled",
            "budget_tokens": thinking_budget,
        }

    if tools:
        params["tools"] = tools

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message


def text_from_message(message):
    return "\n".join([block.text for block in message.content if block.type == "text"])
with open("earth.pdf", "rb") as f:
    file_bytes = base64.standard_b64encode(f.read()).decode("utf-8")

messages = []

add_messages(messages, [
    # Image Block
    {
        "type": "document",
        "source": {
            "type": "base64",
            "media_type": "application/pdf",
            "data": file_bytes,
        }
    },
    # Text Block
    {
        "type": "text",
        "text": "Summarize the document in one sentence"
    }
],
role="user")

print(text_from_message(chat(messages)))