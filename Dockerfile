FROM python:3.7.6

COPY ./server.py server.py
COPY ./user_DAO.py user_DAO.py
COPY ./user_service.py user_service.py

RUN /usr/local/bin/python -m pip install -y --upgrade pip

RUN pip install flask

RUN pip install flask-restful

RUN pip install pymysql

EXPOSE 8000

CMD python server.py