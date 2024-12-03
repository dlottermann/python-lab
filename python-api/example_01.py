import openai
from dotenv import load_dotenv, find_dotenv

# Load the .env file
_ = load_dotenv(find_dotenv())

client  = openai.Client()