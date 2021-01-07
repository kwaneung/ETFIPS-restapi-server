# ETFIPS-restapi-server
ETF Index Prediction Service rest-api linux server


# Rest API Server

사용 라이브러리 : Flask, flask_restful, pymysql

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