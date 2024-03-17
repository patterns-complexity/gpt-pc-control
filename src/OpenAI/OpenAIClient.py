from openai import OpenAI
from src.config import API_KEY, ORGANIZATION

# set api key
client = OpenAI(api_key=API_KEY, organization=ORGANIZATION)
