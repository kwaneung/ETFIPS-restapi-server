from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

import user_set_DAO
import user_DAO


# 실패시 반환은 모두 False지만 추후 유지보수 시 logging 모듈을 통해 각 False가 어떤 오류인지
# 로깅 할 필요가 있음
# max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon, money

class UserSet(Resource):
    def get(self):  # select
        # 튜플을 딕셔너리로 변환 후 반환
        return user_set_DAO.getUserSet()

    def post(self):  # insert
        return "not implemented"

    def delete(self):  # delete
        return "not implemented"

    def patch(self):  # update
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('max_prft_pct', type=str)
        parser.add_argument('min_loss_pct', type=str)
        parser.add_argument('prft_from_prev_mon', type=str)
        parser.add_argument('loss_from_prev_mon', type=str)
        parser.add_argument('money', type=str)
        args = parser.parse_args()

        id = args['id']
        max_prft_pct = args['max_prft_pct']
        min_loss_pct = args['min_loss_pct']
        prft_from_prev_mon = args['max_prft_pct']
        loss_from_prev_mon = args['loss_from_prev_mon']
        money = args['money']

        users = user_DAO.getUser()
        users = [i[0] for i in users]  # id만 추출
        # 없는 user id거나 패스워드가 틀리면 False 반환
        if id in users:
            return user_set_DAO.updateUserSet(id, max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon, money)
        else:
            return False

    def put(self):  # put method :  all change(Delete and insert)
        return "not implemented"
