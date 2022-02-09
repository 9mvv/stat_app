import requests
import log
import db


def get_data():
    headers = {'X-Yandex-API-Key': db.get_opt('yandex_api_key')}
    url = "https://api.weather.yandex.ru/v2/informers?lat=55.749829945655605&lon=37.8730471919356&lang=ru_RU"
    log.info('WEATHER Получение данных. url - {}'.format(url))
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        log.info('WEATHER Получены данные. {}'.format(str(json_response)))
        fact_weather = json_response["fact"]
        sql_insert = "INSERT INTO weather_fact (" \
                    "update_time," \
                    "obs_time," \
                    "temp," \
                    "feels_like," \
                    "icon," \
                    "`condition`," \
                    "wind_speed," \
                    "wind_dir," \
                    "pressure_mm," \
                    "pressure_pa," \
                    "humidity," \
                    "daytime," \
                    "polar," \
                    "season," \
                    "wind_gust" \
                     ") VALUES (CURRENT_TIMESTAMP(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        data = (fact_weather["obs_time"],
                fact_weather["temp"],
                fact_weather["feels_like"],
                fact_weather["icon"],
                fact_weather["condition"],
                fact_weather["wind_speed"],
                fact_weather["wind_dir"],
                fact_weather["pressure_mm"],
                fact_weather["pressure_pa"],
                fact_weather["humidity"],
                fact_weather["daytime"],
                fact_weather["polar"],
                fact_weather["season"],
                fact_weather["wind_gust"]
                )
        db.add_record(sql_insert, data)
    else:
        errortext = "WEATHER Ошибка получения данных {}".format(response)
        log.error(errortext)
