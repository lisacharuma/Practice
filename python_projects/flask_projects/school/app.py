from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)

# Define Student and Course models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    courses = db.relationship('Course', backref='student', lazy=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

# Create database tables
# db.create_all()

# Routes
@app.route('/')
def index():
    return 'Welcome to the School Management System'

@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        name = request.form['name']
        new_student = Student(name=name)
        db.session.add(new_student)
        db.session.commit()
    students = Student.query.all()
    return render_template('students.html', students=students)

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        name = request.form['name']
        student_id = request.form['student_id']
        new_course = Course(name=name, student_id=student_id)
        db.session.add(new_course)
        db.session.commit()
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

if __name__ == '__main__':
    # Import db here to ensure it's imported within the application context.
    #from models import db  # Assuming your models are defined in a 'models.py' file

    # Create the database tables based on the defined models
    with app.app_context():
        db.create_all()
    app.run(debug=True)
