#!/usr/bin/env python3

import os
import discord
import re
import ujson
import random
from discord.ext.commands import Bot
import aiohttp
from io import BytesIO


TOKEN = os.environ.get("BOT_TOKEN")

WORDLIST = {
    'hi-hello': [
        'hi', 
        "hello",
        "hey",
    ]
}

# CATHY = {
#     "image": './assets/images-1-4.jpeg'
# }

BOT_PREFIX = ("?", "!")
INTRO = """
Name: 🔫 **Cathy!!** (King of Memepur)


COMMAND: !cathy 
RESULT: Radom memes for you.



✅ Who is Cathy Memrs:
COMMAND: Cathy and kon/who needs to be in message.

- @Cathy
"""

with open("memers.json", "r") as file:
    meme_data = ujson.load(file)

def get_random_memes():
    global meme_data
    lol = random.randint(0, len(meme_data))
    lol_data = meme_data[str(lol)]
    return lol_data



e = discord.Embed()
client = discord.Client()

@client.event
async def on_message(message):
    """When some one sends the message."""
    username = str(message.author).split("#")[0]
    msg = str(message.content).lower()
    if message.author == client.user:
        return 
    if msg.split(' ')[0] in WORDLIST['hi-hello']:
        msg = msg.split(' ')[0]
        for i in WORDLIST['hi-hello']:
            if i in msg:
                await message.channel.send(f"Suno {username}, ye hi, hello thik hai lekin **Memer** ham hai.")
                break

    if msg == "!meme":
    
        print(msg)
        temp_meme_data = get_random_memes()
        url_img = temp_meme_data['image']
        print("[DOWNLOADING]")
        async with aiohttp.ClientSession() as session:
            async with session.get(url_img) as resp:
                buffer = BytesIO(await resp.read())
                print("buffer",buffer)
        file_ = discord.File(fp=buffer, filename="lol.webm")
        await message.channel.send(f"{temp_meme_data['text']}", file = file_)

    if msg == "!help":
        await message.channel.send(INTRO)

client.run(TOKEN)
