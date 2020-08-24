                       

import covidbackend

def help():
  print("Help query")
  return "Hi {0.author.mention}! Thanks for using GadhaBot, by GadhaGod Electro$

def invite():
  print("Invite query")
  return "Click this link to invite this bot: https://discord.com/oauth2/author$

class covid():
  def __init__(self):
    self.varcases, self.vardeaths = covidbackend.data_return()

  def cases(self):
    print("Covid Cases query")
    return self.varcases + " global cases"

  def deaths(self):
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
