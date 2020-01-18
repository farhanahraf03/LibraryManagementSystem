import psycopg2
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

class Reserved(Resource):
    def post(self,studentid):
        now = datetime.now()
        data = request.get_json()
        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )
        cur = con.cursor()
        query1 = "select borrowed from users where studentid = %s"
        cur.execute(query1,(studentid,))
        num = cur.fetchone()
        a = int(num[0])
        if a==0: 
            
            con.commit()
            cur.close()
            con.close()
            return {'message':'2 entries done already'}
        else:
            later = now + relativedelta(days=+2)
            cur.execute('INSERT INTO reserved VALUES (%s,%s,%s,%s)',(studentid,data['Book ID'],now.strftime("%d/%m/%y"),later.strftime('%d/%m/%y')))
            cur.execute('UPDATE users SET borrowed = %s WHERE studentid = %s',(str(a-1),studentid))
            query1 = "select stock from books1 where id = %s"
            cur.execute(query1,(data['Book ID'],))
            num = cur.fetchone()
            cur.execute('UPDATE books1 SET stock = %s WHERE id = %s',(num[0]-1,data['Book ID']))
            con.commit()
            cur.close()
            con.close()
            return {'message':"Added record"}


class ReservedList(Resource):
    def get(self):
        books=[]
        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )
        cur = con.cursor()
        cur.execute("select * from reserved")
        rows = cur.fetchall()
        for r in rows:
            
            book = {
                'Student ID':r[0],
                'Book ID':r[1],
                'Reservation Date':r[2],
                'Expiry date date':r[3]
                }
            books.append(book)
        con.commit()
        cur.close()
        con.close()
        return {'Books':books}