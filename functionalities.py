from datetime import datetime
import psycopg2
class Functionalities:
    def fine_calculation(issue1,return1):

        issue_date = datetime.strptime(issue1, '%S')
        return_date = datetime.strptime(return1, '%S')

        issue1 = issue_date.strftime("%S")
        return1 = return_date.strftime("%S")

        s= int(issue1)
        r = int(return1)

        duration = r-s


        if duration>30:
            x = duration - 30
            return x*10
        else:
            return 0

    def book_exist(bookid):
        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )
        cur = con.cursor()

        query = "select * from books1 where id = %s"
        cur.execute(query,(bookid,))
        row = cur.fetchall()
        if row:
            cur.close()
            con.close()
            return True
        cur.close()
        con.close()
        return False

    def student_exist(studentid):
        con = psycopg2.connect(
            host = "localhost",
            database = "librarySystem",
            user = "postgres",
            password = "jayan123"
        )
        cur = con.cursor()

        query = "select * from users where studentid = %s"
        cur.execute(query,(studentid,))
        row = cur.fetchall()
        if row:
            cur.close()
            con.close()
            return True
        cur.close()
        con.close()
        return False
        


