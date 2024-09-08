import os
import discord
import random
from discord.ext import commands

# create default set of intents then enable intent to receive message content
permissions = discord.Intents.default()
permissions.message_content = True

# create bot
bot = commands.Bot(command_prefix='!', intents=permissions)



@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    # send message to each server the bot belongs to
    for guild in bot.guilds:
        if guild.system_channel:  # Check if the system channel exists
            try:
                await guild.system_channel.send(f"{bot.user} is online!")
            except discord.Forbidden:
                print(f"Do not have permission to send a message to the system channel of {guild.name}")

@bot.event
async def on_message(message):
    # skip messages from the bot itself
    if message.author == bot.user:
        return

    if message.content.lower().startswith("!hi"):
        await message.channel.send("Hello 👋😃")


    await bot.process_commands(message)

# run bot using TOKEN directly in the code
TOKEN = "MTI2MDk2MzQ5MjkyMDU2MTc3OA.G__Fg1.cP15OIufPVf98ZpNCzIB10IJxNo_EDxv6dQKvA"
bot.run(TOKEN)
