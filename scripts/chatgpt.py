import openai

openai.api_key = open("../config/openai_apikey.txt", "r").read()


def chat(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{prompt}"}]
    )
    reply_content = completion.choices[0].message.content
    return reply_content


prompt = """
what is the meaning of life?
"""

response = chat(prompt)
print(response)
