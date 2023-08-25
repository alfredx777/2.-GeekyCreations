import openai
import webbrowser

openai.api_key = "enter api_key"

print("What would you like to generate?\n")
response = openai.Image.create(
  prompt=input(">> "),
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)
webbrowser.open(image_url)
