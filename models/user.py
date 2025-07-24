# Classe Utilisateur
from models.interaction import Interaction

class Utilisateur:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email
        self.interactions = []

    def poser_question(self, chatbot, bdd, question):
        reponse = chatbot.repondre(question)
        interaction = Interaction(self.id, question, reponse)
        self.interactions.append(interaction)
        chatbot.memoire.append(interaction)
        bdd.inserer_interaction(interaction)
        return reponse

    def voir_historique(self):
        return [i.as_dict() for i in self.interactions]
