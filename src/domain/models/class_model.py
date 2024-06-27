class ClassModel:
    def __init__(self, name, number_of_students, teacher, status, group, grade):
        self.name = name
        self.number_of_students = number_of_students
        self.teacher = teacher
        self.status = status
        self.group = group
        self.grade = grade

        #transcription, students

    def to_dict(self):
        return {
            'name': self.name,
            'number_of_students': self.number_of_students,
            'teacher': self.teacher,
            'status': self.status,
            'group': self.group,
            'grade': self.grade
        }