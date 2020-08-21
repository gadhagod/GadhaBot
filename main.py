import discord
import covidbackend
import messages
import os
from webapp import keep_running
from timestamp import last_update
from news import headlines
import countries
import json

varlastupdate = last_update()
varlastupdate = str(varlastupdate)

class MyClient(discord.Client):
  async def on_ready(self):
      print("Connected to server: " + varlastupdate)
      for guild in client.guilds:
        for member in guild.members:
          members.append(members)
          print(members)

  async def on_message(self, message):
      if (message.content).lower() == '!commands' or (message.content).lower() == '!gadhacommands':
        await message.channel.send(messages.commands().format(message))

      if message.content.lower() == '!help' or (message.content).lower() == '!gadhahelp':
        await message.channel.send(messages.help().format(message))

      if (message.content).lower() == '!invite':
        await message.channel.send(messages.invite().format(message)
        )

      if (message.content).lower() == '!lastupdated':
        await message.channel.send(("Last updated: " + varlastupdate).format(message))

      if (message.content).lower() == '!covidcases':
        covidobj = messages.covid()
        await message.channel.send(covidobj.cases().format(message))
      if (message.content).lower() == '!coviddeaths':
        covidobj = messages.covid()
        await message.channel.send((covidobj.deaths()).format(message))

      if (message.content).lower() == '!news' or (message.content).lower() == '!headlines':
        await message.channel.send(str(headlines()).format(message))

      if ((message.content).lower()).startswith('!population'):
        await message.channel.send(str(countries.population(message.content)))

      if ((message.content).lower()).startswith('!capital'):
        await message.channel.send(str(countries.capital(message.content)))

keep_running()
webapp()
