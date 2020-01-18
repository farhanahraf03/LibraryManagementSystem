import psycopg2
from datetime import datetime
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from functionalities import Functionalities

class Borrowed(Resource):
   
    def post(self,studentid):
        var = Functionalities.student_exist(studentid)
        if var:
            now = datetime.now()
            data = request.get_json()
            
            var1 = Functionalities.book_exist(data['Book ID'])
            if var1:
                con = psycopg2.connect(
                    host = "localhost",
                    database = "librarySystem",
                    user = "postgres",
                    password = "jayan123"
                )
                cur = con.cursor()
                query1 = "select currentallowed from users where studentid = %s"
                cur.execute(query1,(studentid,))
                num = cur.fetchone()
                a = int(num[0])
                if a==0: 
                    
                    con.commit()
                    cur.close()
                    con.close()
                    return {'message':'3 entries done already'}
                else:
                    # remaining iterations are required
                    cur.execute('INSERT INTO borrowed VALUES (%s,%s,%s)',(studentid,data['Book ID'],now.strftime("%S")))
                    cur.execute('UPDATE users SET currentallowed = %s WHERE studentid = %s',(str(a-1),studentid))
                    query1 = "select stock from books1 where id = %s"
                    cur.execute(query1,(data['Book ID'],))
                    num = cur.fetchone()
                    cur.execute('UPDATE books1 SET stock = %s WHERE id = %s',(num[0]-1,data['Book ID']))
                    con.commit()
                    cur.close()
                    con.close()
                    return {'message':"Added record"}
            else:
                return {'message':'Book does not exist'}
        else:
            return {'message':'Student does not exist'}

    
    def put(self,studentid):
        var = Functionalities.student_exist(studentid)
        if var:

            now = datetime.now()
            data = request.get_json()

            var1 = Functionalities.book_exist(data['Book ID'])
            if var1:
                con = psycopg2.connect(
                    host = "localhost",
                    database = "librarySystem",
                    user = "postgres",
                    password = "jayan123"
                )
                cur = con.cursor()
                var = now.strftime("%S")
                cur.execute('UPDATE borrowed SET returndate = %s WHERE studentid = %s and returndate is NULL and bookid = %s',(var,studentid,data['Book ID']))
                cur.execute('select issuedate from borrowed where studentid = %s ',(studentid,))
                row = cur.fetchone()
                cur.execute('UPDATE borrowed SET fine = %s WHERE studentid = %s and and returndate is NULL and bookid = %s',(Functionalities.fine_calculation(row[0],var),studentid,data['Book ID']))
                query1 = "select currentallowed from users where studentid = %s"
                cur.execute(query1,(studentid,))
                num = cur.fetchone()
                cur.execute('UPDATE users SET currentallowed = %s WHERE studentid = %s',(str(int(num[0])+1),studentid))
                
                query1 = "select stock from books1 where id = %s"
                cur.execute('select bookid from borrowed where studentid = %s ',(studentid,))
                num1 = cur.fetchone()
                cur.execute(query1,(num1[0],))
                num = cur.fetchone()
                cur.execute('UPDATE books1 SET stock = %s WHERE id = %s',(num[0]+1,num1[0]))
                
                con.commit()
                cur.close()
                con.close()
                return {'message':"Editted record"}
            else:
                return {'message':'Book does not exist'}
        else:
            return {'message':'Student does not exist'}


    
class BorrowedList(Resource):
    def get(self):
        books=[]
        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )
        cur = con.cursor()
        cur.execute("select * from borrowed")
        rows = cur.fetchall()
        for r in rows:
            
            book = {
                'Student ID':r[0],
                'Book ID':r[1],
                'Issue Date':r[2],
                'Return date':r[3],
                'Fine':r[4]
                }
            books.append(book)
        con.commit()
        cur.close()
        con.close()
        return {'Books':books}

    