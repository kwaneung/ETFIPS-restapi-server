FROM python:3.7.6

COPY ./server.py server.py
COPY ./user_DAO.py user_DAO.py
COPY ./user_service.py user_service.py
COPY ./flask_restful flask_restful
COPY ./flask flask

RUN pip install pymysql

EXPOSE 8000

CMD python server.py