from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient

Client = MongoClient('localhost', 27017)

app = Flask(__name__)


class Demo:
    def __init__(self):
        self.name = "demo"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        dob = request.form['dob']
        gender = request.form['gender']
        course = request.form['course']
        address = request.form['address']

        students.insert_one({
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'dob': dob,
            'gender': gender,
            'course': course,
            'address': address
        })
        return redirect(url_for('registrationsuccessful'))

    all_students = students.find()
    return render_template("registration.html", students=all_students)


@app.route('/registrationsuccessful')
def registrationsuccessful():
    return render_template("index.html")


@app.route('/user/<name>')
def user(name):
    demo = Demo()
    return render_template("user.html", content=name, x=42, demo=demo)


db = Client.SchoolManagement
students = db.students

if __name__ == '__main__':
    app.run(debug=True)
