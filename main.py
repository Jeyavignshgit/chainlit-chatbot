import chainlit as cl
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API Key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set the API Key
openai.api_key ="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"

@cl.on_message
async def handle_message(message: cl.Message):
    try:
        # Send user input to OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.content}]
        )
        
        # Extract and send the response
        reply = response["choices"][0]["message"]["content"]
        await cl.Message(content=reply).send()

    except Exception as e:
        await cl.Message(content=f"Error: {str(e)}").send()
