import schedule
import time
import log
import wot
import weather
#import invest

from os import environ
print(environ)

log.info('Start application')
#Получение инфы при старте
#invest.get_invest_balance()
weather.get_data()
wot.add_record()
wot.update_token()
#Планировщик
schedule.every().hour.do(wot.add_record)
schedule.every().hour.do(weather.get_data)
schedule.every().day.at("00:00").do(wot.update_token)
#schedule.every().hour.do(invest.get_invest_balance)

while True:
    schedule.run_pending()
    time.sleep(1)
