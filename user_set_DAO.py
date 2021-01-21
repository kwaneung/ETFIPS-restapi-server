import pymysql
import logging


def dbConnect(host, user, password, db):
    try:
        return pymysql.connect(host, user, password, db, charset='utf8')
    except Exception as e:
        logging.error(e)
        logging.exception(e)
        return False
        raise


def sqlExcute(connect, sql, var):
    try:
        cur = connect.cursor()
        cur.execute(sql, var)
        connect.commit()
        return True
    except Exception as e:
        logging.error(e)
        logging.exception(e)
        return False
        raise


def getUser():
    connect = dbConnect('192.168.0.40', 'etfuser', '1q2w3e4r', 'ETFIPS')
    if not connect:
        print("Connection fail")
        return False
    else:
        cur = connect.cursor()
        sql = """select * from user"""
        cur.execute(sql)
        return cur.fetchall()


def insertUser(id, password, max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon, money):
    connect = dbConnect('192.168.0.40', 'etfuser', '1q2w3e4r', 'ETFIPS')
    if not connect:
        print("Connection fail")
        return False
    else:
        # cur = connect.cursor()
        sql = """insert into user values(%s,%s,%s,%s,%s,%s,%s)"""
        # cur.execute(sql, (id, password))
        # connect.commit()
        # return True
        return sqlExcute(connect, sql, (id, password, max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon, money))


def updateUser(id, max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon, money):
    connect = dbConnect('192.168.0.40', 'etfuser', '1q2w3e4r', 'ETFIPS')
    if not connect:
        print("Connection fail")
        return False
    else:
        # cur = connect.cursor()
        sql = """update user set max_prft_pct=%s, min_loss_pct=%s, prft_from_prev_mon=%s, loss_from_prev_mon=%s, money=%s where id=%s"""
        # cur.execute(sql, (password, id))
        # connect.commit()
        # return True
        return sqlExcute(connect, sql, (max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon, money,id))


def deleteUser(id):
    connect = dbConnect('192.168.0.40', 'etfuser', '1q2w3e4r', 'ETFIPS')
    if not connect:
        print("Connection fail")
        return False
    else:
        # cur = connect.cursor()
        sql = """delete from user where id=%s"""
        # cur.execute(sql, id)
        # connect.commit()
        # return True
        return sqlExcute(connect, sql, id)


def updateUserPass(id, password):
    connect = dbConnect('192.168.0.40', 'etfuser', '1q2w3e4r', 'ETFIPS')
    if not connect:
        print("Connection fail")
        return False
    else:
        # cur = connect.cursor()
        sql = """update user set password=%s where id=%s"""
        # cur.execute(sql, (password, id))
        # connect.commit()
        # return True
        return sqlExcute(connect, sql, (password, id))


if __name__ == '__main__':
    print("==========getUser==========")
    print(getUser())
    print("==========insertUser==========")
    print(insertUser('DAOtest', '1q2w3e4r', '30', '15', '5', '3', '1500000'))
    print(getUser())
    print("==========updateUserPass==========")
    print(updateUserPass('DAOtest', '11111111'))
    print(getUser())
    print("==========updateUser==========")
    print(updateUser('DAOtest', '31', '16', '6', '4', '1500001'))
    print(getUser())
    print("==========deleteUser==========")
    print(deleteUser('DAOtest'))
    print(getUser())
    print("==========getUser==========")
    print(getUser())
