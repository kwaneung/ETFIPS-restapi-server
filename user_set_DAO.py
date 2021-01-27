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
        # print(sql)
        # print(var)
        cur.execute(sql, var)
        connect.commit()
        return True
    except Exception as e:
        logging.error(e)
        logging.exception(e)
        return False
        raise


def getUserSet():
    connect = dbConnect('192.168.0.40', 'etfuser', '1q2w3e4r', 'ETFIPS')
    if not connect:
        print("Connection fail")
        return False
    else:
        cur = connect.cursor()
        sql = """select * from user"""
        cur.execute(sql)
        return [(i[0], i[2], i[3], i[4], i[5], i[6]) for i in cur.fetchall()]
        # return cur.fetchall()


def updateUserSet(id, max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon, money):
    connect = dbConnect('192.168.0.40', 'etfuser', '1q2w3e4r', 'ETFIPS')
    if not connect:
        print("Connection fail")
        return False
    else:
        # cur = connect.cursor()
        # print(id, max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon, money)
        sql = """update user set max_prft_pct=%s, min_loss_pct=%s, prft_from_prev_mon=%s, loss_from_prev_mon=%s, money=%s where id=%s"""
        # cur.execute(sql, (password, id))
        # connect.commit()
        # return True
        return sqlExcute(connect, sql, (max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon, money, id))


if __name__ == '__main__':
    print("==========getUser==========")
    print(getUserSet())
    # print("==========updateUser==========")
    # print(updateUserSet('DAOtest', '31', '16', '6', '4', '1500001'))
