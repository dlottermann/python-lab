from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Load the .env file
_ = load_dotenv(find_dotenv())

client = OpenAI()


# response = client.chat.completions.create(
#     model="gpt-3.5-turbo-0125",
#     messages=message,
#     max_tokens=500,
#     temperature=0.0,
# )

# print(response.choices[0].message.content)
# message.append(
#     {'role': 'assistant', 'content': response.choices[0].message.content})


def get_response(message, model="gpt-3.5-turbo-0125", max_tokens=500, temperature=0.0):
    response = client.chat.completions.create(
        model=model,
        messages=message,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    print(response.choices[0].message.content)
    message.append(
        response.choices[0].message.model_dump(exclude_none=True))
    return message


message = [{'role': 'user', 'content': 'Me descreva uma maçã em 5 palavras?'}]
get_response(message)
