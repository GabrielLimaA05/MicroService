from config import db
from DisciplineModel.DisciplineModel import Discipline, DisciplineNotFound

class Activity(db.Model):
    __tablename__ = 'activities'

    activity_id = db.Column(db.Integer, primary_key=True)
    discipline_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), nullable=False)
    announced = db.Column(db.String(255), nullable=False)
    answers = db.Column(db.JSON, nullable=True)

    def __init__(self, discipline_id, announced, answers=None):
        self.discipline_id = discipline_id
        self.announced = announced
        self.answers = answers if answers is not None else []

    def to_dict(self):
        return {
            "activity_id": self.activity_id,
            "discipline_id": self.discipline_id,
            "announced": self.announced,
            "answers": self.answers
        }

    @staticmethod
    def get_all():
        activities = Activity.query.all()
        return [activity.to_dict() for activity in activities]

    @staticmethod
    def get_by_id(activity_id):
        activity = Activity.query.get(activity_id)
        if not activity:
            raise ActivityNotFound
        return activity.to_dict()

    @staticmethod
    def add_activity(activity_data):
        discipline = Discipline.query.get(activity_data['discipline_id'])
        if not discipline:
            raise DisciplineNotFound
        activity = Activity(
            discipline_id=activity_data['discipline_id'],
            announced=activity_data['announced'],
            answers=activity_data.get('answers', [])
        )
        db.session.add(activity)
        db.session.commit()
        return activity.to_dict()

    @staticmethod
    def update_activity(activity_id, new_data):
        activity = Activity.query.get(activity_id)
        if not activity:
            raise ActivityNotFound
        discipline = Discipline.query.get(new_data['discipline_id'])
        if not discipline:
            raise DisciplineNotFound
        activity.discipline_id = new_data['discipline_id']
        activity.announced = new_data['announced']
        activity.answers = new_data['answers']
        db.session.commit()
        return activity.to_dict()

    @staticmethod
    def delete_activity(activity_id):
        activity = Activity.query.get(activity_id)
        if not activity:
            raise ActivityNotFound
        db.session.delete(activity)
        db.session.commit()
        return activity.to_dict()

class ActivityNotFound(Exception):
    pass