teachers = [
    {'nome': "joao", 'teacher_id': 1},
    {'nome': "jose", 'teacher_id': 2},
    {'nome': "maria", 'teacher_id': 3}
]

students = [
    {'nome': "alexandre", 'student_id': 1},
    {'nome': "miguel", 'student_id': 2},
    {'nome': "janaina", 'student_id': 3},
    {'nome': "cicero", 'student_id': 4},
    {'nome': "dilan", 'student_id': 5}
]

disciplines = [
    {'nome': "apis e microservicos", 'discipline_id': 1, 'students': [1, 2, 3, 4], 'teachers': [1], 'public': False},
    {'nome': "matematica financeira", 'discipline_id': 2, 'students': [2], 'teachers': [3], 'public': True},
    {'nome': "matematica basica", 'discipline_id': 3, 'students': [1, 2], 'teachers': [3, 2], 'public': False}
]

class DisciplineNotFound(Exception):
    pass

def list_teachers():
    return teachers

def list_students():
    return students

def teaches(teacher_id, discipline_id):
    for discipline in disciplines:
        if discipline['discipline_id'] == discipline_id:
            return teacher_id in discipline['teachers']
    raise DisciplineNotFound