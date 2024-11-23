from flask import Blueprint, request, jsonify
from DisciplineModel.DisciplineModel import Discipline, DisciplineNotFound

disciplines_blueprint = Blueprint('disciplines', __name__)

@disciplines_blueprint.route('/disciplines/', methods=['POST'])
def create_discipline():
    new_discipline = {
        'name': request.json['name']
    }
    Discipline.add_discipline(new_discipline)
    return jsonify(Discipline.get_all()), 201

@disciplines_blueprint.route('/disciplines/<int:discipline_id>/', methods=['PUT'])
def update_discipline(discipline_id):
    try:
        new_data = {
            'name': request.json['name']
        }
        Discipline.update_discipline(discipline_id, new_data)
        return jsonify(Discipline.get_by_id(discipline_id))
    except DisciplineNotFound:
        return jsonify({'message': 'Discipline not found'}), 404

@disciplines_blueprint.route('/disciplines/<int:discipline_id>/', methods=['DELETE'])
def delete_discipline(discipline_id):
    try:
        Discipline.delete_discipline(discipline_id)
        return jsonify(Discipline.get_all())
    except DisciplineNotFound:
        return jsonify({'message': 'Discipline not found'}), 404