import covidbackend

def help():
  print("Help query")
  return "Hi {0.author.mention}! Thanks for using GadhaBot, by GadhaGod Electronics! I can do a lot of miscellaneous things. Type !commands to see what all I can do.\n\nThe code for this bot is open-source. View it here: https://github.com/gadhagod/GadhaBot.\n\nGadhaBot's website: https://gadhabot.gadhagod.repl.co/"

def invite():
  print("Invite query")
  return "Click this link to invite this bot: https://discord.com/oauth2/authorize?client_id=714911868455747629&permissions=0&scope=bot"

class covid():
  def __init__(self):
    self.varcases, self.vardeaths = covidbackend.data_return()

  def cases(self):
    print("Covid Cases query")
    return self.varcases + " global cases"

  def deaths(self):
    print("Covid Deaths query")
    return self.vardeaths + " global deaths"

def commands():
  print("Commands query")
  commandslist=open("commands.txt", "r")
  commandslist = commandslist.read()
  return commandslist

def code():
  print('Source code query')
  message = 'This bot is open-source. View it here: https://github.com/gadhagod/GadhaBot/'
  return message
