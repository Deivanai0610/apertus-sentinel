import os

def ping_host(hostname):
    # Vulnerable to OS Command Injection
    os.system("ping -c 1 " + hostname)