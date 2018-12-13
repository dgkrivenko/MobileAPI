import config
import pymysql


def registration(login, password, name):
    connect = pymysql.connect(host=config.host,
                              user=config.user,
                              passwd=config.passwd,
                              db=config.db)
    cursor = connect.cursor()
    if cursor:
        query = "SELECT * from users WHERE login='{}'".format(login)
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            return 1
        else:
            query_param = "('{}', '{}', '{}')".format(login, password, name)
            query = "INSERT INTO `users`(`login`, `password`, `user_name`) VALUES "
            query += query_param;
            cursor.execute(query)
            connect.commit()
            cursor.close()
            connect.close()
            return 0
    else:
        return 2
