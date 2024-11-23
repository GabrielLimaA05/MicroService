from flask import Blueprint, request, jsonify
from ActivityModel.ActivityModel import Activity, ActivityNotFound

activities_blueprint = Blueprint('activities', __name__)

@activities_blueprint.route('/activities/', methods=['POST'])
def create_activity():
    new_activity = {
        'discipline_id': request.json['discipline_id'],
        'announced': request.json['announced'],
        'answers': request.json.get('answers', [])
    }
    Activity.add_activity(new_activity)
    return jsonify(Activity.get_all()), 201

@activities_blueprint.route('/activities/<int:activity_id>/', methods=['PUT'])
def update_activity(activity_id):
    try:
        new_data = {
            'discipline_id': request.json['discipline_id'],
            'announced': request.json['announced'],
            'answers': request.json['answers']
        }
        Activity.update_activity(activity_id, new_data)
        return jsonify(Activity.get_by_id(activity_id))
    except ActivityNotFound:
        return jsonify({'message': 'Activity not found'}), 404

@activities_blueprint.route('/activities/<int:activity_id>/', methods=['DELETE'])
def delete_activity(activity_id):
    try:
        Activity.delete_activity(activity_id)
        return jsonify(Activity.get_all())
    except ActivityNotFound:
        return jsonify({'message': 'Activity not found'}), 404