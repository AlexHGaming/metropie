import discord
from discord.ext import commands

client = commands.Bot(command_prefix="m.")

@client.event
async def on_ready():
    print("Bot is now online")

@client.command()
async def ping(ctx):
    await ctx.send("pong")

client.run("")