from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom


school = School("ABC School", "Dhaka")

# Adding Classrooms
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)


# Adding Students
rahim = Student("Rahim", eight)
karim = Student("Karim", nine)
fahim = Student("Fahim", ten)
hamim = Student("Hamim", ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)


# Adding Teachers
sakib = Teacher("Sakib Khan")
rakib = Teacher("Rakib Khan")
asif = Teacher("Asif Khan")


# Adding Subjects
bangla = Subject("Bangla", sakib)
physics = Subject("Physics", rakib)
chemistry = Subject("Chemistry", asif)
biology = Subject("Biology", asif)


# Assign Subjects to Classroom
eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)

nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)

ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)


# Take Exam
eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

# Print School Information
print(school)