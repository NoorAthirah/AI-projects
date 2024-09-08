import discord

intents = discord.Intents.default()
intents.message_content = True # Enable the intent to read message content

client = discord.Client(intents=intents) # Create a connection between the client and Discord

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'hi' in message.content.lower():
        await message.channel.send('hi')

client.run("your token")