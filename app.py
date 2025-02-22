from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient

app = Flask(__name__)


class Demo:
    def __init__(self):
        self.name = "demo"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/user/<name>')
def user(name):
    demo = Demo()
    return render_template("user.html", content=name, x=42, demo=demo)


Client = MongoClient('localhost', 27017)
db = Client.SchoolManagement
students = Client.students

if __name__ == '__main__':
    app.run(debug=True)
