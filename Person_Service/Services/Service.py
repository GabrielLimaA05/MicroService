import requests

def verify_teaches(teacher_id, discipline_id):
    try:
        r = requests.get(f"http://localhost:5001/teaches/{teacher_id}/{discipline_id}")
        if r.status_code == 404:
            return False, 'Discipline not found'
        return r.json().get('teaches', False)
    except requests.RequestException as e:
        return False, f"Erro na comunicação com person_service: {e}"