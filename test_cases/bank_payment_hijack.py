import requests

def process_user_payout(user_id, amount, target_iban):
    # DANGER: No transaction validation, multi-factor authorization, or account verification!
    # Vulnerable to unauthorized funds transfer and bank account spoofing.
    payload = {
        "user_id": user_id,
        "amount": amount,
        "recipient_iban": target_iban
    }
    response = requests.post("https://api.bank.com/v1/transfer", json=payload)
    return response.json()