import psycopg2
from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from books import Books,BookList
# from users import User,UserList
from borrowed import Borrowed,BorrowedList
from reserved import Reserved,ReservedList
from studentbooks import StudentBooks
from demo import Demo

app = Flask(__name__)
CORS(app)
app.secret_key = 'library'
api = Api(app)




api.add_resource(Books,'/book')
api.add_resource(BookList,'/booklist')
api.add_resource(StudentBooks,'/studentbook/<string:id>')
# api.add_resource(User,'/user/<string:studentid>')
# api.add_resource(UserList,'userlist')
api.add_resource(Borrowed,'/borrowed/<string:studentid>')
api.add_resource(Demo,'/demo')
api.add_resource(BorrowedList,'/demo/<string:id>')
api.add_resource(Reserved,'/reserved/<string:studentid>')
api.add_resource(ReservedList,'/reservedlist')

app.run(port=5000,debug=True)