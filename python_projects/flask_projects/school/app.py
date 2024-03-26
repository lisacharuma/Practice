from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)

# The association table for many-to-many relationships
enrollment = db.Table('enrollment',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)

# Define Student and Course models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True, nullable=False)
    # Establish a many to many relationship btwn students and courses
    courses = db.relationship('Course', secondary=enrollment, backref='students', lazy='dynamic')

    def __repr__(self):
        return f"Student('{self.name}')"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Course('{self.name}')"


# Routes
@app.route('/')
def index():
    return 'Welcome to the School Management System'

@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        name = request.form['name']
        selected_courses = request.form.getlist('courses')  # Get list of selected courses
        new_student = Student(name=name)
        for course_id in selected_courses:
            course = Course.query.get(course_id)
            new_student.courses.append(course)
        db.session.add(new_student)
        db.session.commit()
    students = Student.query.all()
    courses = Course.query.all()
    return render_template('students.html', students=students, courses=courses)

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        name = request.form['name']
        new_course = Course(name=name)
        db.session.add(new_course)
        db.session.commit()
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@app.route('/students/<int:student_id>')
def student_details(student_id):
    student = Student.query.filter_by(id=student_id).first()
    courses = student.courses.all() if student else []
    return render_template('student_details.html', student=student, courses=courses)

@app.route('/courses/<int:course_id>')
def course_details(course_id):
   #  course = Course.query.filter_by(id=course_id).first()
    # students = course.students.all() if course else []
    course = Course.query.get(course_id)
    students_query = course.students
    students = students_query.all() 
    return render_template('course_details.html', course=course, students=students)


if __name__ == '__main__':
    # Import db here to ensure it's imported within the application context.
    #from models import db  # Assuming your models are defined in a 'models.py' file

    # Create the database tables based on the defined models
    with app.app_context():
        db.create_all()
    app.run(debug=True)
