import os

# Remove the hardcoded secret value
# AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"

def connect_aws():
    # Load AWS credentials from environment variables
    aws_secret_key = os.getenv("AWS_SECRET_KEY")
    if not aws_secret_key:
        raise ValueError("AWS_SECRET_KEY environment variable is missing")
    
    headers = {"Authorization": f"Bearer {aws_secret_key}"}
    response = requests.get("https://aws.amazon.com/api", headers=headers)
    return response.status_code