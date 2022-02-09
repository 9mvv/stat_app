import requests
import log
import db


def update_token():
    url = "https://api.worldoftanks.ru/wot/auth/prolongate/"
    log.info('WOT Обновление токена.')
    post_data = {'application_id': db.get_opt('wot_app_id'),
                 'access_token': db.get_opt('wot_token'),
                 "expires_at": "604800"}
    response = requests.post(url, data=post_data)
    json_response = response.json()
    if response.status_code == 200 and json_response["status"] != 'error' and json_response['status'] == 'ok':
        db.set_opt('wot_token', json_response['data']['access_token'])
    else:
        errortext = "WOT Обновление токена. Ошибка {}".format(json_response['error']['message'])
        log.error(errortext)


def add_record():
    acc_id = db.get_opt('wot_acc_id')
    url = 'https://api.worldoftanks.ru/wot/account/info/?application_id=' + db.get_opt('wot_app_id') + \
          '&access_token=' + db.get_opt('wot_token') + '&account_id=' + acc_id
    log.info('WOT Добавление записи. Запрос данных: {}'.format(url))
    response = requests.get(url)
    wot_response = response.json()
    if response.status_code == 200 and wot_response["status"] != 'error' and wot_response['status'] == 'ok':
        log.info('WOT Получены данные. {}'.format(str(wot_response)))
        wot_data = wot_response["data"][acc_id]
        sql_insert = "INSERT INTO wot_stat (" \
                     "timestamp,account_id," \
                     "nickname," \
                     "global_rating," \
                     "private_bonds," \
                     "private_credits," \
                     "private_free_xp," \
                     "private_gold," \
                     "statistics_all_avg_damage_assisted," \
                     "statistics_all_avg_damage_assisted_radio," \
                     "statistics_all_avg_damage_assisted_track," \
                     "statistics_all_avg_damage_blocked," \
                     "statistics_all_battle_avg_xp," \
                     "statistics_all_battles," \
                     "statistics_all_draws," \
                     "statistics_all_losses," \
                     "statistics_all_wins," \
                     "statistics_all_damage_dealt," \
                     "statistics_all_damage_received," \
                     "statistics_all_survived_battles" \
                     ") VALUES (CURRENT_TIMESTAMP(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        data = (acc_id,
                wot_data['nickname'],
                wot_data['global_rating'],
                wot_data['private']['bonds'],
                wot_data['private']['credits'],
                wot_data['private']['free_xp'],
                wot_data['private']['gold'],
                wot_data['statistics']['all']['avg_damage_assisted'],
                wot_data['statistics']['all']['avg_damage_assisted_radio'],
                wot_data['statistics']['all']['avg_damage_assisted_track'],
                wot_data['statistics']['all']['avg_damage_blocked'],
                wot_data['statistics']['all']['battle_avg_xp'],
                wot_data['statistics']['all']['battles'],
                wot_data['statistics']['all']['draws'],
                wot_data['statistics']['all']['losses'],
                wot_data['statistics']['all']['wins'],
                wot_data['statistics']['all']['damage_dealt'],
                wot_data['statistics']['all']['damage_received'],
                wot_data['statistics']['all']['survived_battles']
                )
        db.add_record(sql_insert, data)
    else:
        errortext = "WOT Ошибка получения данных wot. Ошибка - {}.".format(wot_response['error']['message'])
        log.error(errortext)
