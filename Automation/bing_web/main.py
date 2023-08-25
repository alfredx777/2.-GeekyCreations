import requests

# Import the random module to generate random responses
import random

def get_search_results(query):
  url = "https://api.bing.microsoft.com/v7.0/search"
  api_key = "enter API_KEY"
  headers = {"Ocp-Apim-Subscription-Key": api_key}
  params = {"q": query, "responseFilter": "Webpages"}
  # Send the request and get the response as a JSON object
  response = requests.get(url, headers=headers, params=params).json()
  return response["webPages"]["value"]

def generate_response(message):
  # If the message is empty, return an empty string
  if not message:
    return "" 
  else:
    # Get the web search results
    results = get_search_results(message)
    if not results:
      return "I'm sorry, I couldn't find anything related to your message."
    else:
      # Get the title, snippet and URL of the first result
      title = results[0]["name"]
      snippet = results[0]["snippet"]
      url = results[0]["url"]
      summary = f"Here's what I found on the web:\n\n**{title}**\n\n{snippet}\n\nYou can read more here: {url}\n"
      questions = ["What do you think about this?", "Do you want to know more?", "Do you have any questions?", "Do you have any feedback?", "Is this helpful?"]
      suggestion = f"\n{random.choice(questions)}"
      # Return the summary and the suggestion as the response
      return summary + suggestion

end_conversation = False

while not end_conversation:
  user_message = input().lower()
  ai_response = generate_response(user_message)
  print(ai_response)
