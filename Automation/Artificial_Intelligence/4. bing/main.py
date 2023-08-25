import asyncio, json
import re
from EdgeGPT import Chatbot, ConversationStyle


async def main():
    while True:
        cookies = json.loads(open("cookies.json", encoding="utf-8").read())  # might omit cookies option
        bot = await Chatbot.create(cookies=cookies)
        command = input(">> ")
        response = await bot.ask(prompt=command, conversation_style=ConversationStyle.precise, simplify_response=True)
        reply = response["text"]
        reply = re.sub('\[\^\d+\^\]', '', reply)
        print(json.dumps(reply)) 

        await bot.close()
        if "quit" in command or exit in command:
            exit()

if __name__ == "__main__":
    asyncio.run(main())