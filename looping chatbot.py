from dotenv import load_dotenv


from anthropic import Anthropic


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(client,messages, system = None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return "".join(block.text for block in message.content if block.type == "text")

if __name__ == "__main__":
    continue_conversation = True
    load_dotenv()
    client = Anthropic()
    model = "claude-sonnet-5-5"

    # Start with an empty message list
    messages = []
    
    user_input = input(">: ")
    system_prompt = """
        You are a patient math tutor.
        Do not directly answer a student's questions.
        Guide them to a solution step by step.
        
        If the user has the intention to left the conversation does not ask for that, politely acknowledge it and you MUST add the phrase 'Good Bye' in the reply. 
        """

    while continue_conversation:
        add_user_message(messages, user_input)        
        answer = chat(client, messages)
        add_assistant_message(messages, answer)
        print("---")
        print("Assistant:", answer)
        print("---")
        user_input = input(">: ")
        if "Good Bye" in user_input:
            continue_conversation = False
    
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
