from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

import user_DAO

# 실패시 반환은 모두 False지만 추후 유지보수 시 logging 모듈을 통해 각 False가 어떤 오류인지
# 로깅 할 필요가 있음

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
            # 패스워드 검증 후 틀리면 False
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
        parser.add_argument('old_passwd', type=str)
        parser.add_argument('new_passwd', type=str)
        args = parser.parse_args()

        id = args['ID']
        old_passwd = args['old_passwd']
        new_passwd = args['new_passwd']

        users = user_DAO.getUser()
        # users = [i[0] for i in users]  # id만 추출
        # 없는 user id거나 패스워드가 틀리면 False 반환
        if (id, old_passwd) in users:
            return user_DAO.updateUser(id, new_passwd)
        else:
            return False

    def put(self):  # put method :  all change(Delete and insert)
        return "not implemented"
