import psycopg2
from flask import Flask, request
from flask_restful import Resource, Api

class Demo(Resource):
    def post(self):
        data = request.get_data()
        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )
        cur = con.cursor()
        #query = "select * from books1 where id = %s"
        #cur.execute(query,(id,))
        # row = cur.fetchone()
        # if row: 
        #     con.commit()
        #     cur.close()
        #     con.close()
        #     return {'message':'Item already exists'}
        # else:
        if data is None:
            cur.close()
            con.close()
            return {'message':"data is empty"},401
        cur.execute('INSERT INTO books1 VALUES (%s,%s,%s,NULL,NULL,%s)',(data['id'],data.volumeInfo.title,data.volumeInfo.authors,data.volumeInfo.categories))
        cur.execute('select * from books1 where id = %s'(data.id))
        xyz = cur.fetchone()
        if xyz is None:
            con.commit()
            cur.close()
            con.close()
            return {'message':"item not added"},401
        con.commit()
        cur.close()
        con.close()
        return {'message':"Added '{}'".format(data.volumeInfo.title)}
