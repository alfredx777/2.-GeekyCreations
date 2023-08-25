import wolframalpha

APP_ID = "enter APP_ID"

self = input("prompt: ")
client = wolframalpha.Client(APP_ID)
res = client.query(self.query)
output = next(res.results).text
print("\n" + output)