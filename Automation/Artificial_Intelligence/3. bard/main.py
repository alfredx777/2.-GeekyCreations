from Bard import Chatbot
import re

token = "paste TOKEN"
chatbot = Chatbot(token)

def prompt_bard(prompt):
    response = chatbot.ask(prompt)
    return response['content']

def main():
    while True:
        command = input("prompt: ")
        print("your prompt:", command, '\n')

        response = prompt_bard(command)
        response = re.sub('\[\^\d+\^\*\]', '', response)
        print(response)
main()