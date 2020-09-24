import discord
import messages
import os
from timestamp import last_update
from news import headlines
import countries
from mail import sendemail
from search import gsearch
from issues import issuecreate
from weather import weather
import city
import userinfo
import server

varlastupdate = last_update()
varlastupdate = str(varlastupdate)

email = os.environ.get("EMAIL")
reciever = os.environ.get("RECIEVER")
password = os.environ.get("PASSWORD")

class MyClient(discord.Client):
	async def on_ready(self):
		print("Connected to server: " + varlastupdate)

	async def on_message(self, message):
		sender = message.author.name
		userid = message.author.id
		userinfo.store(sender, userid)
		g = message.guild
		server.store(g.id, g.name, g.region, g.description, g.member_count)

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

		if message.content.lower().startswith('!news') or message.content.lower().startswith('!headlines'):
			content = message.content.lower()
			content = content.replace(' ', '')
			content = content.replace('!news', '')
			print(content)
			await message.channel.send(str(headlines(content)))
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

		if (message.content.lower()).startswith('!googlesearch') or (message.content.lower()).startswith('!search'):
			content = message.content
			content = content.replace('!googlesearch ','')
			content = content.replace('!search ','')
			await message.channel.send(gsearch(content))
			sendemail(email, reciever, password, 'GadhaBot', 'GadhaBot google search query')

		if (message.content.lower()).startswith('!issue') or (message.content.lower()).startswith('!report') or (message.content.lower()).startswith('!suggest'):
			content = message.content
			content = content.lower()
			content = content.replace('!suggest', '')
			content = content.replace('!suggest ', '')
			content = content.replace('!issue', '')
			content = content.replace('!report', '')
			content = content.replace('!issue ', '')
			content = content.replace('!report ', '')
			await message.channel.send(issuecreate(sender, content).format(message))
			sendemail(email, reciever, password, 'GadhaBot', 'GadhaBot issue query')

		if message.content.lower() == '!weather':
			data = weather(userid)
			if data == False:
				await message.channel.send('Please set your city. Set your city by typing \'!city {your city\'s name}')
			else:
				description, temp, feels_like, maxtemp, mintemp, humidity = data
				x = str(description + temp + feels_like + maxtemp + mintemp + humidity)
				await message.channel.send(x)

		if message.content.lower().startswith('!city'):
			content = message.content
			content = content.replace('!city ', '')
			content = content.replace('!city', '')
			city.store(userid, content)
			await message.channel.send('City stored')

MyClient().run(os.environ.get("DISCORD_BOT_SECRET"))
