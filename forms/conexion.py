from sqlite3 import connect
import pymysql


def conexionBD():
    db = pymysql.connect(

        host = 'localhost',
        user = 'root', 
        passwd = '',
        db = 'portafolio'

        )
    return db