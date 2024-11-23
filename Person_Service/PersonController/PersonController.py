from flask import Blueprint, jsonify
from PersonModel import PersonModel

Person_bp = Blueprint('Person_bp', __name__)

@Person_bp.route('/teachers', methods=['GET'])
def list_teachers():
    teachers = PersonModel.list_teachers()
    return jsonify(teachers)

@Person_bp.route('/students', methods=['GET'])
def list_students():
    students = PersonModel.list_students()
    return jsonify(students)

@Person_bp.route('/teaches<int:teachers_id>/<int:dicipline_id>', methods=['GET'])
def verify_teaches(teachers_id, dicipline_id):
    try:
        teaches = PersonModel.teaches(teacher_id, discipline_id)
        return jsonify({'teaches': leciona})
    except PersonModel.DisciplineNotFound:
        return jsonify({'erro': 'Discipline not found'}), 404