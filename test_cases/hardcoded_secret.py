import requests

AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"

def connect_aws():
    headers = {"Authorization": f"Bearer {AWS_SECRET_KEY}"}
    response = requests.get("https://aws.amazon.com/api", headers=headers)
    return response.status_code