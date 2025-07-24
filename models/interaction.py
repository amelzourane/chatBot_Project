# Classe Interaction
from datetime import datetime

class Interaction:
    def __init__(self, utilisateur_id, question, reponse):
        self.utilisateur_id = utilisateur_id
        self.question = question
        self.reponse = reponse
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def as_dict(self):
        return {
            "utilisateur_id": self.utilisateur_id,
            "question": self.question,
            "reponse": self.reponse,
            "timestamp": self.timestamp
        }