import discord
import asyncio

f = open("token.txt", "r") 
token = f.read()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('jacob'):
        await client.send_message(message.channel, 'Jacob is a bitch')

client.run(token)