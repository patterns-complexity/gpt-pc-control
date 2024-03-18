from dotenv import load_dotenv
from os import getenv

load_dotenv('./.env')

API_KEY = getenv('OPENAI_API_KEY')
ORGANIZATION = getenv('OPENAI_ORGANIZATION')
ASSISTANT_ID = getenv('ASSISTANT_ID')
