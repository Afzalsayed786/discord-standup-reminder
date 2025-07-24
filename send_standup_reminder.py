from dotenv import load_dotenv
load_dotenv()
import os
TOKEN = os.environ['DISCORD_TOKEN']

import os
import discord
import asyncio

TOKEN = os.environ['DISCORD_TOKEN']  # Token ab environment se aayega
CHANNEL_ID = 1397907627454894092

MESSAGE = "Good morning! Please share your daily standup update :wave:"

class StandupBot(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
        channel = await self.fetch_channel(CHANNEL_ID)
        await channel.send(MESSAGE)
        await self.close()

intents = discord.Intents.default()
intents.guilds = True

client = StandupBot(intents=intents)
asyncio.run(client.start(TOKEN))
