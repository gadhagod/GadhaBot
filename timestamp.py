from datetime import datetime

def last_update():
  last_update = datetime.now()
  last_update = str(last_update)
  last_update = last_update[:19] + " GMT"
  return last_update
