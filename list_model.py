from openai import OpenAI

client = OpenAI(
    base_url="https://api.inference.cscs.ch/v1",
    api_key="YOUR_CSCS_API_KEY"
)

# Fetch available models for your API key
models = client.models.list()

print("--- Authorized Models for Your Key ---")
for model in models.data:
    print(model.id)
print("---------------------------------------")