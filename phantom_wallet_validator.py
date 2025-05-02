
from solana.rpc.api import Client
import json

# Phantom validator + balance check
solana = Client("https://api.mainnet-beta.solana.com")

def get_balance(wallet_address):
    result = solana.get_balance(wallet_address)
    lamports = result.get('result', {}).get('value', 0)
    sol_balance = lamports / 1e9
    return round(sol_balance, 4)

def validate_invite(wallet_address, invite_key):
    with open("invites.json", "r") as f:
        invites = json.load(f)

    for tier, users in invites.items():
        for user in users:
            if invite_key == user["invite_key"]:
                balance = get_balance(wallet_address)
                return {
                    "status": "granted",
                    "name": user["name"],
                    "tier": tier,
                    "balance": balance,
                    "wallet": wallet_address
                }

    return { "status": "denied", "reason": "Invalid key or wallet." }

# Example usage
if __name__ == "__main__":
    wallet = input("Enter Phantom wallet address: ").strip()
    key = input("Enter your invite key: ").strip()
    result = validate_invite(wallet, key)
    print(result)
