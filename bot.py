import os
import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from pytz import timezone

# Get secrets from environment
TOKEN = os.environ['DISCORD_TOKEN']
EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

# Time setup
IST = timezone('Asia/Kolkata')
now = datetime.now(IST)
timestamp = now.strftime("%Y-%m-%d %H:%M")

# Message content (No Role ID)
message = f"@Intern REMINDER - Standup @6pm ({timestamp} IST)"

# Send to Discord
CHANNEL_ID = "1397907627454894092"
url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"

headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json"
}
data = {
    "content": message
}

response = requests.post(url, headers=headers, json=data)

if response.status_code in [200, 204]:
    print("✅ Discord message sent!")
else:
    print(f"❌ Discord failed: {response.status_code}")
    print(response.text)

# Send to Email
try:
    email_msg = MIMEText(message)
    email_msg['Subject'] = "🛎️ Daily Standup Reminder"
    email_msg['From'] = EMAIL_ADDRESS
    email_msg['To'] = EMAIL_ADDRESS

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(email_msg)

    print("✅ Email sent successfully!")

except Exception as e:
    print(f"❌ Email failed: {str(e)}")
