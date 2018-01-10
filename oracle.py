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
    cmd = message.content.split()
    if cmd[0] == "-oracle" or cmd[0] == "-o":
        action = cmd[1]
        subject = ""
        for i in range(2,len(cmd)):
            subject = subject + cmd[i] + " "
        subject = subject.strip()
        print("|" + action + "|")
        print("|" + subject + "|")
        if action == "help":
            helpString = "-oracle[-o]\n"
            helpString = helpString + "    " + "matchup[mu] {hero-name}: returns heroes best against and worst against and best with relative to {hero-name}\n"
            await client.send_message(message.channel, helpString)
        elif action == "matchup" or action == "mu":
            localname = subject
            await client.send_message(message.channel, str(hero.determineMatchUp(localname)))
        #elif action == "bestwith" or action == "bw":
        #    localname = subject
        #    await client.send_message(message.channel, str(hero.findBestWith(localname)))

client.run(token)