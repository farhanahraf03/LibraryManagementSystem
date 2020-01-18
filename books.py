import psycopg2
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

class Books(Resource):
    def get(self):
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
        cur.close()
        con.close()
        
        if row:
            return {'item' : {
                'Id':row[0],
                'Title':row[1],
                'Author':row[2],
                'Stock':row[3],
                'Shelf number':row[4],
                'Category':row[5]
                }}
        return {'message':'Item not found'},404

    def post(self):
        data = request.get_json()
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
        title = data['volumeInfo']
        cur.execute('INSERT INTO books1 VALUES (%s,%s,%s,NULL,NULL,%s)',(data['id'],title['title'],title['authors'],data['categories']))
        con.commit()
        cur.close()
        con.close()
        return {'message':"Added '{}'".format(title['title'])}

    def put(self):
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

    def delete(self):
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

    
class BookList(Resource):
    def get(self):
        books=[]
        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )
        cur = con.cursor()
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
        con.commit()
        cur.close()
        con.close()
        return {'Books':books}

    