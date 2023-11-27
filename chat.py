import openai

openai.api_key = "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"
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]   
    )
    
    return response.choices[0].message.content.strip() # type: ignore

if __name__ == "__name__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("Chat: ", response)