from flask import Flask,request,jsonify
import pymysql
import collections
 
#Establishing connection the database 
conn = pymysql.connect(host="localhost",user="root",password="root",db="book")
c = conn.cursor()  

app = Flask(__name__)  # Initializing flask app

#Welcome message when we are initially in loacalhost:5000 (or 127.0.0.1:5000).
@app.route('/',methods=['GET'])   
def main():
 return ("Hi,I am Akarsh, Welcome to my Book Management App")

#The Create or Insert part of CRUD to insert new books into the data base
#I use 'POST' because I want to send the data to the server
@app.route('/insert',methods=['POST'])
def insert_data():
    isbn = request.json['isbn']
    name = request.json['name']
    author = request.json['author']
    price = request.json['price']
    c.execute("""INSERT into book_tb(isbn,name,author,price) VALUES(%s,%s,%s,%s)""",(isbn,name,author,price))
    conn.commit()
    return ("Data Inserted successful")

#The Read part of CRUD to list the books available in the database
#Here, I used 'GET' because I want to receive the list of books from the server
@app.route('/retrieve',methods=['GET'])
def select():
    query = "SELECT * from book_tb"
    c.execute(query)
    data = c.fetchall()
    st = ""
    for row in data:
     st = st + str(row[0]) + "||" + str(row[1]) + "||" +str(row[2]) + "||" +str(row[3]) + "\n"
    return (st)

#The Update part of CRUD to update an old record specified by old_isbn with a new record specified by new_isbn and it's corresponding new values
#here, again I use 'POST' to send the data to the server
@app.route('/update_details',methods=['POST'])
def details_update():
    new_isbn = request.json['new_isbn']
    old_isbn = request.json['old_isbn']
    name = request.json['name']
    author = request.json['author']
    price = request.json['price']
    query = "UPDATE book_tb set isbn=%s,name=%s,author=%s,price=%s WHERE isbn=%s"
    param = (new_isbn,name,author,price,old_isbn)
    c.execute(query,param)
    return ("Update successful!")

#The Delete part of CRUD to delete a record or entry in the database specified by isbn
#Here, I used 'POST' to specify the isbn value that is to be deleted
@app.route('/delete_data',methods=['POST'])
def book_deletion():
    isbn= request.json['isbn']
    query = "DELETE from book_tb where isbn=%s"
    c.execute(query,isbn)
    return ("Record deleted successfully")

#running the app
app.run()


