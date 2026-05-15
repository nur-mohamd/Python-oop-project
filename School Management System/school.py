class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        class_name = student.classroom.name
        self.classrooms[class_name].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'

        elif 70 <= marks < 80:
            return 'A'

        elif 60 <= marks < 70:
            return 'A-'

        elif 50 <= marks < 60:
            return 'B'

        elif 40 <= marks < 50:
            return 'C'

        elif 33 <= marks < 40:
            return 'D'

        else:
            return 'F'

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.00,
            'D': 1.00,
            'F': 0.00
        }
        return grade_map[grade]

    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <= 5.00:
            return 'A+'

        elif 3.5 <= value < 4.5:
            return 'A'

        elif 3.0 <= value < 3.5:
            return 'A-'

        elif 2.5 <= value < 3.0:
            return 'B'

        elif 2.0 <= value < 2.5:
            return 'C'

        elif 1.0 <= value < 2.0:
            return 'D'

        else:
            return 'F'

    def __repr__(self):
        result = "===== SCHOOL INFO =====\n"
        result += "\nAll Classrooms:\n"

        for key in self.classrooms.keys():
            result += f"{key}\n"

        result += "\n===== STUDENTS =====\n"

        for key, value in self.classrooms.items():
            result += f"\n--- {key.upper()} Classroom Students ---\n"

            for student in value.students:
                result += f"Name: {student.name} | ID: {student.id}\n"

        result += "\n===== SUBJECTS =====\n"

        for key, value in self.classrooms.items():
            result += f"\n--- {key.upper()} Classe's Subjects ---\n"

            for sub in value.subjects:
                result += f"{sub.name} ---> "
                result += f"Teacher: {sub.teacher.name}\n"

        result += "\n===== RESULTS =====\n"

        for key, value in self.classrooms.items():

            for student in value.students:
                result += f"\nStudent: {student.name}\n"

                for subject, marks in student.marks.items():
                    grade = student.subject_grade[subject]

                    result += f"{subject} : {marks} ({grade})\n"

                result += f"{student.calculate_final_grade()}\n"

        return result