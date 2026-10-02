from dotenv import load_dotenv


from anthropic import Anthropic


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(client, messages, system_prompt=None, stop_sequences=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system_prompt:
        params["system"] = system_prompt
    if stop_sequences:
        params["stop_sequences"] = stop_sequences
    message = client.messages.create(**params)
    return "".join(block.text for block in message.content if block.type == "text")

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
    add_user_message(messages, "Generate a very short event bridge rule as JSON")

    # Get a raw JSON response without assistant-message prefill.
    answer = chat(
        client,
        messages,
        system_prompt="Return only valid JSON. Do not use Markdown code fences.",
    )
    print(answer)

