import requests
import log
import db
from os import environ
from tinkoff.invest import Client

import tgl

CONTRACT_PREFIX = "tinkoff.public.invest.api.contract.v1."
invest_token = environ['INVEST_TOKEN']


def get_invest_balance():
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
