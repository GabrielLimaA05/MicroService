from config import db

class Discipline(db.Model):
    __tablename__ = 'disciplines'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    activities = db.relationship('Activity', backref='discipline', lazy=True)

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "activities": [activity.to_dict() for activity in self.activities]
        }

    @staticmethod
    def get_all():
        disciplines = Discipline.query.all()
        return [discipline.to_dict() for discipline in disciplines]

    @staticmethod
    def get_by_id(discipline_id):
        discipline = Discipline.query.get(discipline_id)
        if not discipline:
            raise DisciplineNotFound
        return discipline.to_dict()

    @staticmethod
    def add_discipline(discipline_data):
        discipline = Discipline(name=discipline_data['name'])
        db.session.add(discipline)
        db.session.commit()
        return discipline.to_dict()

    @staticmethod
    def update_discipline(discipline_id, new_data):
        discipline = Discipline.query.get(discipline_id)
        if not discipline:
            raise DisciplineNotFound
        discipline.name = new_data['name']
        db.session.commit()
        return discipline.to_dict()

    @staticmethod
    def delete_discipline(discipline_id):
        discipline = Discipline.query.get(discipline_id)
        if not discipline:
            raise DisciplineNotFound
        db.session.delete(discipline)
        db.session.commit()
        return discipline.to_dict()

class DisciplineNotFound(Exception):
    pass