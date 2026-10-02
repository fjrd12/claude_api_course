# Load env variables and create client
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-sonnet-4-5"
# Helper functions
from anthropic.types import Message

def add_messages(messages, message, role="user"):
    user_message = {
        "role": role,
        "content": message.content if isinstance(message, Message) else message,
    }
    messages.append(user_message)

def chat(messages, system=None, stop_sequences=[], tools=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "stop_sequences": stop_sequences,
    }

    if tools:
        params["tools"] = tools

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message

def text_from_message(message):
    return "\n".join([block.text for block in message.content if block.type == "text"])
web_search_schema = {
    "type": "web_search_20250305",
    "name": "web_search",
    "max_uses": 5,
    "allowed_domains": ["google.com"],
}
messages = []
add_messages(
    messages, 
    """ 
    What's the best exercise for gaining leg muscle?
    """, 
    role="user")
response = chat(messages, tools=[web_search_schema])
print(response)