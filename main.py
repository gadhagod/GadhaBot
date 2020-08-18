import discord
import covidbackend
import messages
import os
from webapp import keep_running
from timestamp import last_update

covidobj = messages.covid()
varlastupdate = last_update()
varlastupdate = str(varlastupdate)

class MyClient(discord.Client):
    async def on_ready(self):
        print("Connected to server: " + varlastupdate)

    async def on_message(self, message):
        if message.content == '!help':
          await message.channel.send(messages.help().format(message))

        if message.content == '!invite':
            print("Invite query")
            await message.channel.send(messages.invite().format(message))

        if message.content == '!lastUpdate':
            print("Last update query")
            await message.channel.send(("Last updated: " + varlastupdate).format(message))

        if message.content == '!covidCases':
            await message.channel.send(covidobj.cases().format(message))
        if message.content == '!covidDeaths':
            await message.channel.send(covidobj.deaths().format(message))  

client = MyClient()
keep_running()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)

webapp()
