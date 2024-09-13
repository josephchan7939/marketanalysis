import requests

# Check external IP to confirm VPN routing
response = requests.get("https://api.ipify.org?format=json")
print("Your IP:", response.json()["ip"])
