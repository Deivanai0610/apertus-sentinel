import subprocess

def ping_host(hostname):
    # Secure approach using subprocess.run with proper argument handling
    subprocess.run(["ping", "-c", "1", hostname], check=True)