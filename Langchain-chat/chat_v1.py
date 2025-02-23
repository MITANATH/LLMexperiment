import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Updated import
from langchain_core.messages import HumanMessage, SystemMessage  # Updated import
# Load OpenAI API key
load_dotenv()
def create_chat():
    return ChatOpenAI(temperature=0.7) 
def main():
    chat = create_chat()
    
    print("Welcome to SimpleChat! (type 'quit' to exit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
            
        messages = [
            SystemMessage(content="You are a helpful AI assistant."),
            HumanMessage(content=user_input)
        ]
        
        response = chat(messages)
        print(f"\nAssistant: {response.content}")
if __name__ == "__main__":
main()
#this is new file