from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

import user_DAO


class User(Resource):
    def get(self):  # select
        # 튜플을 딕셔너리로 변환 후 반환
        return {i[0]: i[1] for i in user_DAO.getUser()}

    def post(self):  # insert
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        parser.add_argument('passwd', type=str)
        args = parser.parse_args()

        id = args['ID']
        passwd = args['passwd']

        users = user_DAO.getUser()
        users = [i[0] for i in users]

        if id in users:  # 이미 존재하면 실패
            return False
        else:
            return user_DAO.insertUser(id, passwd)

    def delete(self):  # delete
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        args = parser.parse_args()

        id = args['ID']

        users = user_DAO.getUser()
        users = [i[0] for i in users]
        if id in users:
            return user_DAO.deleteUser(id)
        else:
            return False

    def patch(self):  # update
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        parser.add_argument('passwd', type=str)
        args = parser.parse_args()

        id = args['ID']
        passwd = args['passwd']

        users = user_DAO.getUser()
        users = [i[0] for i in users]
        if id in users:
            return user_DAO.updateUser(id, passwd)
        else:
            return False

    def put(self):  # put method :  all change(Delete and insert)
        return "not implemented"
