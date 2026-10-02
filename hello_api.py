from dotenv import load_dotenv
from anthropic import Anthropic

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

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)
    
def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)
    
if __name__ == "__main__":
    load_dotenv()
    client = Anthropic()
    model = "claude-sonnet-5-5"
    messages = []
    prompt =  """Generate three different sample AWS CLI commands in Bash. Each should be very short and concise.
             """
    add_user_message(messages, prompt)
    answer = chat(
        client,
        messages,
        system_prompt="Return only Bash commands. Do not use Markdown code fences.",
        stop_sequences=["\n\n"],
    )
    print(answer)
