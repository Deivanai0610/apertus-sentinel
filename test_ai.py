import os
from openai import OpenAI

# 1. Initialize the client pointing to the CSCS Inference API endpoint
client = OpenAI(
    base_url="https://api.inference.cscs.ch/v1",  # CSCS Base URL
    api_key="YOUR_CSCS_API_KEY"             # Replace with your key
)

# 2. Send a query to the Apertus model
response = client.chat.completions.create(
    model="swiss-ai/Apertus-v1.5-8B",  # Or the specific model name provided in CSCS docs
    messages=[
        {"role": "user", "content": "Hello! Are you online?"}
    ]
)

# 3. Print the AI's response to your terminal screen
print("\n--- Apertus Output ---")
print(response.choices[0].message.content)
print("----------------------\n")