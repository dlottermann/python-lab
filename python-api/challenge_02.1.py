import json
import yfinance as yf

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Load the .env file
_ = load_dotenv(find_dotenv())

client = OpenAI()


def retorna_cotacao(ticker, period='1mo'):
    ticker_data = yf.Ticker(f'{ticker}.SA').history(period=period)['Close']
    ticker_data.index = ticker_data.index.strftime('%Y-%m-%d')
    ticker_data = round(ticker_data, 2)

    if len(ticker_data) == 0:
        return json.dumps({'error': 'Ticker não encontrado'})

    if len(ticker_data) > 30:
        slice_size = int(len(ticker_data) / 30)
        ticker_data = ticker_data.iloc[::slice_size][::-1]

    return ticker_data.to_json()


tools = [
    {
        'type': 'function',
        'function': {
            'name': 'retorna_cotacao',
            'description': 'Retorna cotação de um ativo',
            'parameters': {
                'type': 'object',
                'properties': {
                    'ticker': {
                        'type': 'string',
                        'description': 'Código do ativo'
                    },
                    'period': {
                        'type': 'string',
                        'description': 'Período de cotação',
                        'enum': ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd']
                    }
                }
            },
        }
    }
]


avaliable_functions = {'retorna_cotacao': retorna_cotacao}


def resturn_message(msg):
    response = client.chat.completions.create(
        messages=msg,
        model='gpt-4o-mini',
        tools=tools,
        tool_choice='auto'
    )

    tool_calls = response.choices[0].message.tool_calls

    if (tool_calls):
        msg.append(response.choices[0].message)
        for tool_call in tool_calls:
            function = avaliable_functions[tool_call.function.name]
            parameters = json.loads(tool_call.function.arguments)
            result = function(**parameters)
            msg.append({'tool_call_id': tool_call.id,
                        'role': 'tool',
                        'name': tool_call.function.name,
                        'content': result})
            response_tool = client.chat.completions.create(
                messages=msg,
                model='gpt-4o-mini',
            )

            print(f'Assistant: {response_tool.choices[0].message.content}')
            print()


if __name__ == '__main__':

    print('Olá, eu sou um assistente virtual. Em que posso te ajudar?\n')

    while True:
        user_input = input('User: ')
        msg = [{'role': 'user', 'content': user_input}]
        resturn_message(msg)
