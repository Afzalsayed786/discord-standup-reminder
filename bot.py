import os
import requests
from datetime import datetime
from pytz import timezone
import os
TOKEN = os.environ['DISCORD_TOKEN']
THREAD_ID = os.getenv("1397907627454894092")
ROLE_ID = os.getenv("1397907627454894092")
IST = timezone('Asia/Kolkata')
now = datetime.now(IST)
timestamp = now.strftime("%Y-%m-%d %H:%M")
message = f"<@&{ROLE_ID}> Time for daily standup! ({timestamp} IST)\nDrop
your updates below "
url = f"https://discord.com/api/v10/channels/{THREAD_ID}/messages"
headers = {
"Authorization": f"Bot {TOKEN}",
"Content-Type": "application/json"
}
data = {
"content": message
}
response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
print(" Message sent successfully!")
else:
print(f" Failed to send message: {response.status_code}")
print(response.text)