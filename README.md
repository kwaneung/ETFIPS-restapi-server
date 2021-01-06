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
- post : insert user {id, passwd}
- patch : update user {id, passwd} password 변경
- get : get user
- delete : delete user {id}

공인IP 및 포트포워딩 체크