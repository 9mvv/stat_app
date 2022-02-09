import schedule
import time
import wot
import weather
import log

from os import environ

print(environ)

log.info('Start application')
weather.get_data()
wot.add_record()
wot.update_token()
schedule.every().hour.do(wot.add_record)
schedule.every().hour.do(weather.get_data)
schedule.every().day.at("00:00").do(wot.update_token)
while True:
    schedule.run_pending()
    time.sleep(1)
