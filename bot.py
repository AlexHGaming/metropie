import random
import discord
from discord.ext import commands
import json
import sys

client = commands.Bot(command_prefix="m.")
config = None
try:
    with open("conf.json", "r") as jsonData:
        config = json.load(jsonData)
except IOError:
    sys.exit()

@client.event
async def on_ready():
    print("Bot is now online")

@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command()
async def genRan(ctx):
    await ctx.send(random.randrange(1, 10))

client.run(config["token"])