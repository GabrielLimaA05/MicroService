import requests

PESSOA_SERVICE_URL = "http://localhost:5001/persons"

class PersonServiceClient:
    @staticmethod
    def verify_teaches(teacher_id, discipline_id):
        url = f"{PERSON_SERVICE_URL}/leciona/{teacher_id}/{discipline_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('teaches', False) if data.get('isok') else False
        except requests.RequestException as e:
            print(f"Erro ao acessar o person_service: {e}")
            return False