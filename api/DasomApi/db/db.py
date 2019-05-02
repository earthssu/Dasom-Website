import pymysql

db_info = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'kimh1785',
    'db': '',
    'charset': 'utf8'
}

try:
    db = pymysq.connect()