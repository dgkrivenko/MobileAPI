import config
import pymysql


def add_genre(login, genre):
    connect = pymysql.connect(host=config.host,
                              user=config.user,
                              passwd=config.passwd,
                              db=config.db)
    cursor = connect.cursor()
    if cursor:
        query = "UPDATE `users` SET gener='{}' WHERE login='{}'".format(genre, login)
        cursor.execute(query)
        connect.commit()
        cursor.close()
        connect.close()
        return "0"
    else:
        return "1"
