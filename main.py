import discord
import covidbackend
import messages
import os
from webapp import keep_running
from timestamp import last_update
from news import headlines
import countries


varlastupdate = last_update()
varlastupdate = str(varlastupdate)

class MyClient(discord.Client):
  async def on_ready(self):
      print("Connected to server: " + varlastupdate)

  async def on_message(self, message):
      if message.content == '!commands' or (message.content).lower() == '!gadhacommands':
        await message.channel.send(messages.commands().format(message))

      if message.content == '!help' or (message.content).lower() == '!gadhahelp':
        await message.channel.send(messages.help().format(message))

      if message.content == '!invite':
          await message.channel.send(messages.invite().format(message)
          )

      if message.content == '!lastUpdated':
          await message.channel.send(("Last updated: " + varlastupdate).format(message))

      if message.content == '!covidCases':
          covidobj = messages.covid()
          await message.channel.send(covidobj.cases().format(message))
      if message.content == '!covidDeaths':
          covidobj = messages.covid()
          await message.channel.send((covidobj.deaths()).format(message))

      if message.content == '!news' or message.content == '!headlines':
          await message.channel.send(str(headlines()).format(message))

      if message.content.startswith('!population'):
          await message.channel.send(str(countries.population(message.content)))

      if message.content.startswith('!capital'):
          await message.channel.send(str(countries.capital(message.content)))



client = MyClient()
keep_running()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
webapp()
