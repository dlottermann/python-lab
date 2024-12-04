from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Load the .env file
_ = load_dotenv(find_dotenv())

client = OpenAI()

message = [{'role': 'user',
            'content': 'Conte uma história sobre uma viajante que se perdeu em uma floresta.'}]


response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=message,
    max_tokens=1000,
    temperature=0.0,
    stream=True
)

stream_full = ''

for stream in response:
    texto = stream.choices[0].delta.content
    if texto:
        print(texto, end='')
        stream_full += texto


# print(stream_full)
