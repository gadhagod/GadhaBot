from countryinfo import CountryInfo

def capital(message):
  message = message.replace('!capital ', '')
  message = message.replace('!capital', '')
  if message == '':
    return 'Please specify country.'
  else:
    countryinfo = CountryInfo(message)
    message = message.replace(message[0], message[0].upper())
    message = message.replace(message[1:], message[1:].lower())
    return "The capital of " + message  + " is " + str(countryinfo.capital() + ".")

def population(message):
  message = message.replace('!population ', '')
  message = message.replace('!population', '')
  if message == '':
    return 'Please specify country.'
  else:
    countryinfo = CountryInfo(message)
    message = message.replace(message[0], message[0].upper())
    message = message.replace(message[1:], message[1:].lower())
    return "The population of " + message + " is " + str(countryinfo.population() + ".")
