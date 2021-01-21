# ETFIPS-restapi-server
ETF Index Prediction Service rest-api linux server


# Rest API Server

사용 라이브러리 : Flask(1.1.1), flask_restful(0.3.8), pymysql(0.10.1)

server.py : 메인 서버 \
user_DAO.py : 사용자 DB 처리 \
user_service.py : 로직 처리 

/login
- post : login {id, passwd}

/user
- post(Create Method) : insert user {id, passwd}
- patch(Update/Modify Method) : update user {id, old_passwd, new_passwd} password 변경
- get(Read Method) : get user
- delete(Delete Method) : delete user {id}
- put(Update/Replace Method) : not implemented

/userset
- post(Create Method) : insert user_set {max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon, money}
- patch(Update/Modify) : update user_set {max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon, money}
- get(Read Method) : get user_set(dic형으로 반환해야하는데 어떻게 할지 고민좀 해야할듯?)
- delete(Delete Method) : not implemented
- put(Update/Replace Method) : not implemented