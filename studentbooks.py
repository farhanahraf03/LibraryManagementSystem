import psycopg2
from flask import Flask, request, Response
from flask_restful import Resource, Api, reqparse

class StudentBooks(Resource):

    def get(self,id):
        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )

        cur = con.cursor()
        books=[]
        query = "select * from books1 where title like %s"
        cur.execute(query,('%'+id+'%',))
        row = cur.fetchall()
        if row:
            cur.execute("select * from books1")
            rows = cur.fetchall()
            for r in rows:
                
                book = {
                    'ID':r[0],
                    'Title':r[1],
                    'Author':r[2],
                    'Stock':r[3],
                    'Shelf Number':r[4],
                    'Category':r[5],
                    }
                books.append(book)
            cur.close()
            con.close()
            return{'Books':books}
        return {'message':'Item not found'},404

    def post(self,id):
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
        if row: 
            
            con.commit()
            cur.close()
            con.close()
            return {'message':'Item already exists'}
        else:
            cur.execute('INSERT INTO books1 VALUES (%s,%s,%s,%s,%s,%s)',(id,data['Title'],data['Author'],data['Stock'],data['Shelf Number'],data['Category']))
            con.commit()
            cur.close()
            con.close()
            return {'message':"Added '{}'".format(data['Title'])}

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


class MyResponse(Response):
    pass