from dotenv import load_dotenv


from anthropic import Anthropic


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(client, messages, system_prompt=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "stream": True
    }
    if system_prompt:
        params["system"] = system_prompt
        
    response_text = ""
    with client.messages.create(**params) as stream:
        for event in stream:
            if event.type == "content_block_delta" and event.delta.type == "text_delta":
                print(event.delta.text, end="", flush=True)
                response_text += event.delta.text

    return response_text

def has_duplicates(text: str) -> bool:
    """Return True if any character appears more than once in `text`."""
    return len(set(text)) != len(text)

if __name__ == "__main__":
    load_dotenv()
    client = Anthropic()
    model = "claude-sonnet-5-5"

    # Start with an empty message list
    messages = []

    # Add the initial user question
    add_user_message(messages, "Write a python function that checks a string for duplicate characters")

    # Get Claude's response
    chat(client, messages, system_prompt="you are a Python engineer who writes efficient and clean Python code")


