import discord
import covidbackend
import messages
import os
from webapp import keep_running
from timestamp import last_update
from news import headlines
import countries
from easyemail import sendemail

varlastupdate = last_update()
varlastupdate = str(varlastupdate)

email = os.environ.get("EMAIL")
reciever = os.environ.get("RECIEVER")
password = os.environ.get("PASSWORD")

class MyClient(discord.Client):
	async def on_ready(self):
		print("Connected to server: " + varlastupdate)

	async def on_message(self, message):
		if message.content.lower() == '!commands' or (message.content).lower() == '!gadhacommands':
			await message.channel.send(messages.commands().format(message))
			sendemail(email, reciever, password, 'GadhaBot query', 'GadhaBot commands query from ' + str(message.author))

		if message.content.lower() == '!help' or (message.content).lower() == '!gadhahelp':
			await message.channel.send(messages.help().format(message))
			sendemail(email, reciever, password, 'GadhaBot',  'GadhaBot help query from ' + str(message.author))

		if (message.content).lower() == '!invite':
			await message.channel.send(messages.invite().format(message))
			sendemail(email, reciever, password, 'GadhaBot', 'GadhaBot invite query from ' + str(message.author))

		if (message.content).lower() == '!lastupdated':
			await message.channel.send(("Last updated: " + varlastupdate).format(message))
			sendemail(email, reciever, password, 'GadhaBot', 'GadhaBot last update query from ' + str(message.author))
			print('Last updated query')


		if (message.content).lower() == '!covidcases':
			covidobj = messages.covid()
			await message.channel.send(covidobj.cases().format(message))
			sendemail(email, reciever, password, 'GadhaBot', 'GadhaBot covid cases query from ' + str(message.author))

		if (message.content).lower() == '!coviddeaths':
			covidobj = messages.covid()
			await message.channel.send((covidobj.deaths()).format(message))
			sendemail(email, reciever, password, 'GadhaBot', 'GadhaBot covid deaths query from ' + str(message.author))

		if message.content.lower() == '!news' or (message.content).lower() == '!headlines':
			await message.channel.send(str(headlines()).format(message))
			sendemail(email, reciever, password, 'GadhaBot', 'GadhaBot news query from ' + str(message.author))
			
		if (message.content.lower()).startswith('!population'):
			await message.channel.send(str(countries.population(message.content)))
			sendemail(email, reciever, password, 'GadhaBot', 'GadhaBot population query from ' + str(message.author))

		if (message.content.lower()).startswith('!capital'):
			await message.channel.send(str(countries.capital(message.content)))
			sendemail(email, reciever, password, 'GadhaBot', 'GadhaBot capital query from ' + str(message.author))

		if (message.content.lower()) == '!sourcecode':
			await message.channel.send(messages.code())
			sendemail(email, reciever, password, 'GadhaBot', 'GadhaBot source code query')

client = MyClient()
keep_running()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
webapp()
