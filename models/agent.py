# Classe ChatbotSupport (Agent)
class ChatbotSupport:
    def __init__(self, nom):
        self.nom = nom
        self.memoire = []
        self.base_connaissance = {
            "mon wi-fi ne fonctionne pas": "Vérifiez que votre routeur est allumé et redémarrez-le.",
            "comment réinitialiser mon mot de passe windows": "Cliquez sur 'Mot de passe oublié' sur l'écran de connexion Windows.",
            "l’écran reste noir au démarrage": "Vérifiez si le câble est bien branché et testez avec un autre écran.",
            "impossible d’imprimer depuis mon ordinateur": "Vérifiez la connexion de l’imprimante et réinstallez les pilotes.",
            "je ne reçois plus mes courriels outlook": "Vérifiez votre connexion Internet et la configuration de votre compte Outlook.",
            "mon ordinateur est lent, que faire": "Fermez les applications inutiles, redémarrez votre PC, et analysez avec un antivirus."
        }

    def repondre(self, question):
        question = question.lower()
        for cle in self.base_connaissance:
            if cle in question:
                return self.base_connaissance[cle]
        return "Je suis désolé, je n'ai pas compris la question."

    def afficher_historique(self):
        return self.memoire

    def reinitialiser(self):
        self.memoire = []

