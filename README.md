# GadhaBot
The source code of GadhaBot, a discord bot with many miscellaneous functions. It sends an email to me everytime someone runs a command with what command they run and who ran it. It's hosted on the Raspberry Pi.

# Bot commands
https://github.com/gadhagod/GadhaBot/blob/master/commands.txt

# Necessary packages
discord, flask, feedparser, bs4, countryinfo

# Invite
click this link to invite this bot to your server: https://discord.com/oauth2/authorize?client_id=714911868455747629&permissions=0&scope=bot

# Download
to download this repo, run this in your terminal
$ git clone https://github.com/GadhaGod/GadhaBot
$ cd GadhaBot

# Edit
Then create .env:
$ sudo nano .env

Write the following into the file:
DISCORD_BOT_SECRET=sercret bot token
Change the values of the enviroment variables to your email credentials and your bot token.
