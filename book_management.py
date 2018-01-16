from flask import Flask,request,jsonify
import pymysql
import json
import collections
from collections import Counter

conn = pymysql.connect(host="localhost",user="root",password="root",db="book")
c = conn.cursor()

app = Flask(__name__)

@app.route('/',methods=['GET'])
def main():
 return ("Hello, Welcome to Book Management App")

@app.route('/insert',methods=['POST'])
def insert_data():
    isbn = request.json['isbn']
    name = request.json['name']
    author = request.json['author']
    price = request.json['price']
    c.execute("""INSERT into book_tb(isbn,name,author,price) VALUES(%s,%s,%s,%s)""",(isbn,name,author,price))
    conn.commit()
    return ("Data Inserted successful")

@app.route('/retrieve',methods=['GET'])
def select():
    query = "SELECT * from book_tb"
    c.execute(query)
    data = c.fetchall()
    st = ""
    for row in data:
     st = st + str(row[0]) + "||" + str(row[1]) + "||" +str(row[2]) + "||" +str(row[3]) + "\n"
    return (st)

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

@app.route('/delete_data',methods=['POST'])
def book_deletion():
    isbn= request.json['isbn']
    query = "DELETE from book_tb where isbn=%s"
    c.execute(query,isbn)
    return ("Record deleted successfully")

app.run()



