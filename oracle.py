import discord
import asyncio
from opendota import connection
from heroes import Heroes

f = open("token.txt", "r") 
token = f.read()

client = discord.Client()

hero = Heroes()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('-oracle'):
        cmd = message.content.split('-oracle')[1].split()
        if cmd[0] == "info":
            if not cmd[1]:
                await client.send_message(message.channel, "please provide localname")
            localname = cmd[1]
            await client.send_message(message.channel, str(hero.determineMatchUp(localname)))

client.run(token)