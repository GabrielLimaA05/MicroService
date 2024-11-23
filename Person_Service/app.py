from config import create_app
from PersonController.PersonController import Person_bp

app = create_app()
app.register_blueprint(Person_bp)

if __name__ == '__main__':
    app.run(host='localhost', port=5001)