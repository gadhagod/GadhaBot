from countryinfo import CountryInfo

def capital(message):
  message = message.replace('!capital ', '')
  message = message.upper()
  countryinfo = CountryInfo(message)
  return "The capital of " + message.lower() + " is " + str(countryinfo.capital())

def population(message):
  message = message.replace('!population ', '')
  message = message.upper()
  countryinfo = CountryInfo(message)
  return "The population of " + message.lower() + " is " + str(countryinfo.population())
