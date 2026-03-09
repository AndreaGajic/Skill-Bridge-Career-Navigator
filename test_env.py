import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

if key:
    print(f"SUCCESS: Key found. Starts with: {key[:5]}...")
else:
    print("FAILURE: No key found. Check your .env file.")