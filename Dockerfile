FROM python:3.7.6

COPY ./server.py server.py
COPY ./user_DAO.py user_DAO.py
COPY ./user_service.py user_service.py
COPY ./user_set_DAO.py user_set_DAO.py
COPY ./user_set_service.py user_set_service.py

RUN pip install Flask==1.1.1
RUN pip install Flask-RESTful==0.3.8
RUN pip install PyMySQL==0.10.1

EXPOSE 8000

CMD python server.py