# import pymysql
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

from user_service import User
from user_set_service import UserSet
import user_DAO

app = Flask(__name__)
api = Api(app)


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        id = args['ID']
        password = args['password']

        users = user_DAO.getUser()  # id, name

        if (id, password) in users:
            print('Result : True')
            return {'result': 'true'}
        else:
            print('False')
            return {'result': 'false'}

# test = (1, 2)
# test2 = [3, 4, 5, 6]
# a = {"test" : test, "test2" : test2}
# print(a)
# class test(Resource):
#     def get(self):
#         return a


# api.add_resource(test, '/test')
api.add_resource(Login, '/login')
api.add_resource(User, '/user')
api.add_resource(UserSet, '/userset')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
