import os
import requests
from datetime import datetime
from pytz import timezone

# Get secrets from environment
TOKEN = os.environ['DISCORD_TOKEN']
ROLE_ID = os.environ['DISCORD_ROLE_ID']

# Time setup
IST = timezone('Asia/Kolkata')
now = datetime.now(IST)
timestamp = now.strftime("%Y-%m-%d %H:%M")

# Message to send
message = f"<@&{ROLE_ID}> Time for daily standup! ({timestamp} IST)\nDrop your updates below 👇"

# Replace with your Discord channel ID (hardcoded or via env)
CHANNEL_ID = "YOUR_CHANNEL_ID"  # Example: "123456789012345678"
url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"

# Headers & data
headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json"
}
data = {
    "content": message
}

# Send message
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200 or response.status_code == 204:
    print("✅ Message sent successfully!")
else:
    print(f"❌ Failed to send message: {response.status_code}")
    print(response.text)
