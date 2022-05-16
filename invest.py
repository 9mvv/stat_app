import db
import requests
import json
from os import environ
import tgl
invest_token = environ['INVEST_TOKEN']

#получение баласна с использованием офф SDK
def get_invest_balance():
    from tinkoff.invest import Client
    try:
        TOKEN = invest_token
        with Client(TOKEN) as client:
            # Получение баланса Брок счет 2003351141
            PortfolioResponse = client.operations.get_portfolio(account_id='2003351141')
            brok_balance=PortfolioResponse.total_amount_shares.units+PortfolioResponse.total_amount_bonds.units+PortfolioResponse.total_amount_etf.units+PortfolioResponse.total_amount_currencies.units+PortfolioResponse.total_amount_futures.units
            print("Общий:" + str(brok_balance))
            # Получение баланса ИИС 2019998208
            PortfolioResponse = client.operations.get_portfolio(account_id='2019998208')
            iis_balance=PortfolioResponse.total_amount_shares.units+PortfolioResponse.total_amount_bonds.units+PortfolioResponse.total_amount_etf.units+PortfolioResponse.total_amount_currencies.units+PortfolioResponse.total_amount_futures.units
            print("Общий:" + str(iis_balance))
            db.set_invest_balance('3', str(brok_balance+iis_balance))
    except:
        tgl.send("Ошибка обновления баланса инвестиций")

#получение баласна без SDK
def get_invest_balance2():
    # Получение баланса Брок счет 2003351141
    response_brok = get_invest_request("2003351141").json()
    print(response_brok)
    brok_balance=int(response_brok["totalAmountShares"]["units"])+ \
        int(response_brok["totalAmountCurrencies"]["units"])+ \
        int(response_brok["totalAmountEtf"]["units"])+ \
        int(response_brok["totalAmountFutures"]["units"])
    print("Общий:" + str(brok_balance))
    # Получение баланса ИИС 2019998208
    response_iis = get_invest_request("2019998208").json()
    print(response_iis)
    iis_balance = int(response_iis["totalAmountShares"]["units"])+ \
        int(response_iis["totalAmountCurrencies"]["units"])+ \
        int(response_iis["totalAmountEtf"]["units"])+ \
        int(response_iis["totalAmountFutures"]["units"])
    print("Общий:" + str(iis_balance))
    #PortfolioResponse = client.operations.get_portfolio(account_id='2019998208')
    db.set_invest_balance('3', str(brok_balance+iis_balance))

def get_invest_request(account):
    url = "https://invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.OperationsService/GetPortfolio"
    payload = json.dumps({
      "accountId": account
    })
    headers = {
      'Authorization': 'Bearer '+invest_token,
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response