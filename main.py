import discord
import covidbackend
import messages
import os
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
covidobj = messages.covid()

class MyClient(discord.Client):
    async def on_ready(self):
        print("Connected: " + current_time)

    async def on_message(self, message):
        if message.content == '!help':
          await message.channel.send(messages.help().format(message))

        if message.content == '!invite':
            print("Invite query")
            await message.channel.send(messages.invite().format(message))

        if message.content == '!covidCases':
            await message.channel.send(covidobj.cases().format(message))
        if message.content == '!covidDeaths':
            await message.channel.send(covidobj.deaths().format(message))  

client = MyClient()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
