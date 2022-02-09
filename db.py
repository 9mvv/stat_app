import MySQLdb
import log
from os import environ

mysql_host = environ['DB_SERVER']
mysql_user = environ['DB_USER']
mysql_passwd = environ['DB_PASS']
mysql_db = environ['DB_NAME']
conn_string = "host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db, charset='utf8', use_unicode= True"


def add_record(sql_insert, data):
    db = MySQLdb.connect(conn_string)
    cursor = db.cursor()
    cursor.execute(sql_insert, data)
    db.commit()
    db.close()
    log.info('DB Запись сохранена.')

def set_opt(opt_name,opt_val):
    log.info('Запись опции {} в БД.'.format(opt_name))
    db = MySQLdb.connect(conn_string)
    cursor = db.cursor()
    sql="UPDATE options SET value='"+opt_val+"' WHERE name='"+opt_name+"';"
    cursor.execute(sql)
    log.info('Запись опции {} завершена.'.format(opt_name))
    db.commit()
    db.close()

def get_opt(opt_name):
    db = MySQLdb.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db, charset = 'utf8', use_unicode = True)
    cursor = db.cursor()
    sql="SELECT value FROM options WHERE name='"+opt_name+"';"
    cursor.execute(sql)
    result = cursor.fetchone()
    db.close()
    return result[0]