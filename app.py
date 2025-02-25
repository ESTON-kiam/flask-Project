from bson import ObjectId
from flask import Flask, render_template, url_for, request, redirect, session
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
        return redirect(url_for('display_registration'))

    all_students = students.find()
    return render_template("registration.html", students=all_students)


@app.route('/registration_successful')
def registration_successful():
    return render_template("index.html")


@app.route('/display_registration', methods=['GET', 'POST'])
def display_registration():
    all_students = students.find()
    return render_template("display_registration.html", students=all_students)


@app.route('/user/<name>')
def user(name):
    demo = Demo()
    return render_template("user.html", content=name, x=42, demo=demo)


@app.route('/edit/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = students.find_one({"_id": ObjectId(student_id)})

    if request.method == 'POST':
        updated_data = {
            'firstName': request.form['firstName'],
            'lastName': request.form['lastName'],
            'email': request.form['email'],
            'dob': request.form['dob'],
            'gender': request.form['gender'],
            'course': request.form['course'],
            'address': request.form['address']
        }
        students.update_one({"_id": ObjectId(student_id)}, {"$set": updated_data})
        return redirect(url_for('registration_successful'))

    return render_template("edit_student.html", student=student)


@app.route('/delete/<student_id>', methods=['GET'])
def delete_student(student_id):
    from bson.objectid import ObjectId

    students.delete_one({"_id": ObjectId(student_id)})

    return redirect(url_for('display_registration'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


db = Client.SchoolManagement
students = db.students

if __name__ == '__main__':
    app.run(debug=True)
