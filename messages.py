import covidbackend

def help():
  print("Help query")
  return "Hi {0.author.mention}!, Thanks for using the GadhaBot! It can do a lot of miscellaneous things and is still develpment. \n\n!invite lets you invite this bot to another server.\n!covidCases will tell you the number of Coronavirus cases there are in the world.\n!covidDeaths will tell you the number of coronavirus deaths there are in the world\n\nThe source code of this bot is open source. View it here: "

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
