import MySQLdb
import log
from os import environ

mysql_host = environ['DB_SERVER']
mysql_user = environ['DB_USER']
mysql_passwd = environ['DB_PASS']
mysql_db = environ['DB_NAME']
mysql_port = environ['DB_PORT']


def add_record(sql_insert, data):
    db = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db, charset='utf8', use_unicode=True,port=int(mysql_port))
    cursor = db.cursor()
    cursor.execute(sql_insert, data)
    db.commit()
    db.close()
    log.info('DB Запись сохранена.')


def set_opt(opt_name, opt_val):
    log.info('Запись опции {} в БД.'.format(opt_name))
    db = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db, charset='utf8', use_unicode=True,port=int(mysql_port))
    cursor = db.cursor()
    sql = "UPDATE options SET value='"+opt_val+"' WHERE name='"+opt_name+"';"
    cursor.execute(sql)
    log.info('Запись опции {} завершена.'.format(opt_name))
    db.commit()
    db.close()


def get_opt(opt_name):
    db = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db, charset='utf8', use_unicode=True,port=int(mysql_port))
    cursor = db.cursor()
    sql = "SELECT value FROM options WHERE name='"+opt_name+"';"
    cursor.execute(sql)
    result = cursor.fetchone()
    db.close()
    return result[0]

def set_invest_balance(account, balance):
    log.info('Запись баланса в БД.')
    db = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db, charset='utf8', use_unicode=True,port=int(mysql_port))
    cursor = db.cursor()
    sql = "INSERT INTO finances_amount (date_time,account_id,amount) VALUES (NOW(),'"+account+"','"+balance+"');"
    cursor.execute(sql)
    log.info('Запись баланса завершена.')
    db.commit()
    db.close()