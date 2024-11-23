from flask import Flask
from config import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db.init_app(app)

# Importar e registrar blueprints
from ActivityController.ActivityController import activities_blueprint
from DisciplineController.DisciplineController import disciplines_blueprint

app.register_blueprint(activities_blueprint)
app.register_blueprint(disciplines_blueprint)

with app.app_context():
    db.create_all()  # Cria todas as tabelas

if __name__ == '__main__':
    app.run(debug=True)