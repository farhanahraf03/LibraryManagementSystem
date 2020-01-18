import psycopg2
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

class User(Resource):
    def get(self,studentid):
        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )

        cur = con.cursor()

        query = "select * from users where studentid = %s"
        cur.execute(query,(studentid,))
        row = cur.fetchone()
        cur.close()
        con.close()
        
        if row:
            return {'user' : {
                'Student ID':row[0],
                'Name':row[1],
                'Branch':row[2],
                'Current Allowed':row[3],
                'Borrowed Index':row[4],
                'Reserved Index':row[5]
                }}
        return {'message':'Item not found'},404

    def post(self,studentid):
        data = request.get_json()
        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )
        cur = con.cursor()
        query = "select * from users where studentid = %s"
        cur.execute(query,(studentid,))
        row = cur.fetchone()
        if row: 
            
            con.commit()
            cur.close()
            con.close()
            return {'message':'Item already exists'}
        else:
            max_allowed = 3    # number of books allowed to borrow = 3
            cur.execute('INSERT INTO users VALUES (%s,%s,%s,%s)',(studentid,data['Name'],data['Branch'],max_allowed))
            con.commit()
            cur.close()
            con.close()
            return {'message':"Added record"}

    def put(self,id):
        data = request.get_json()

        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )
        cur = con.cursor()
        query = "select * from books1 where id = %s"
        cur.execute(query,(id,))
        row = cur.fetchone() 
        cur.execute('UPDATE books1 SET %s = %s WHERE id = %s'%(data['Attribute'],data['Value'],id))#attribute = stock/shelf #value = stock+1 / stock-1 / shelf number
        con.commit()
        cur.close()
        con.close()
        return {'message':"Editted '{}'".format(data['Attribute'])}

    def delete(self,id):
        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )
        cur = con.cursor()
        query = "select * from books1 where id = %s"
        cur.execute(query,(id,))
        row = cur.fetchone()
        if row: 
            cur.execute('DELETE FROM books1 WHERE id = %s',(id,))
            con.commit()
            cur.close()
            con.close()
            return {'message':"Record deleted"}
        else:
            con.commit()
            cur.close()
            con.close()
            return {'message':"Item not in base"}

class USerList(Resource):
