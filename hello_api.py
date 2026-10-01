from dotenv import load_dotenv


from anthropic import Anthropic


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(client,messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return "".join(block.text for block in message.content if block.type == "text")

if __name__ == "__main__":
    load_dotenv()
    client = Anthropic()
    model = "claude-sonnet-5-5"

    # Start with an empty message list
    messages = []

    # Add the initial user question
    add_user_message(messages, "Define quantum computing in one sentence")

    # Get Claude's response
    answer = chat(client, messages)

    # Add Claude's response to the conversation history
    add_assistant_message(messages, answer)

    # Add a follow-up question
    add_user_message(messages, "Write another sentence")

    # Get the follow-up response with full context
    final_answer = chat(client, messages)
    add_assistant_message(messages, final_answer)

    # Print the full conversation history
    for message in messages:
        print(f"{message['role'].capitalize()}: {message['content']}")  
