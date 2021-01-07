# import pymysql
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

from user_service import User
import user_DAO

app = Flask(__name__)
api = Api(app)


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        parser.add_argument('passwd', type=str)
        args = parser.parse_args()

        id = args['ID']
        passwd = args['passwd']

        users = user_DAO.getUser()  # id, name

        if (id, passwd) in users:
            print('Result : True')
            return {'result': 'true'}
        else:
            print('False')
            return {'result': 'false'}


api.add_resource(Login, '/login')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
