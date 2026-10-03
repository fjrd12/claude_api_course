# Load env variables and create client
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-sonnet-4-5"
# Helper functions
from anthropic.types import Message

# Magic string to trigger redacted thinking
thinking_test_str = "ANTHROPIC_MAGIC_STRING_TRIGGER_REDACTED_THINKING_46C9A13E193C177646C7398A98432ECCCE4C1253D5E2D82641AC0E52CC2876CB"

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
            "budget_tokens": thinking_budget
        }
    if tools:
        params["tools"] = tools

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message


def text_from_message(message):
    return "\n".join([block.text for block in message.content if block.type == "text"])
messages = []

add_messages(
    messages, 
    # "Write a one pragraph guide to recursion.", 
    thinking_test_str,
    role="user"
)

print(text_from_message(chat(messages, thinking=True)))