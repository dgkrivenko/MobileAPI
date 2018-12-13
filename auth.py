import config
import pymysql


def get_data_by_login(req_login):
    connect = pymysql.connect(host=config.host,
                              user=config.user,
                              passwd=config.passwd,
                              db=config.db)
    cursor = connect.cursor()
    query = "SELECT * from users WHERE login='{}'".format(req_login)
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    connect.close()
    if row:
        login = str(row[1])
        password = str(row[2])
        name = str(row[3])
        return (0, login, password, name)
    else:
        return (1,)


# '''
# 	0 - success
# 	1 - invalid login or password
# '''


def auth(login, password, query_result):
    if query_result[0] == 1:
        return 1
    elif query_result[0] == 0:
        if login == query_result[1] and password == query_result[2]:
            return 0
        else:
            return 1
