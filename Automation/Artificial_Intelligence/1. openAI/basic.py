import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write an essay about penguins"}])
print(completion.choices[0].message.content)