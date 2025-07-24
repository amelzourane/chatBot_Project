# Classe BaseDeDonnees
class BaseDeDonnees:
    def __init__(self):
        self.interactions_stockees = []

    def inserer_interaction(self, interaction):
        self.interactions_stockees.append(interaction)

    def get_historique_utilisateur(self, utilisateur_id):
        return [i for i in self.interactions_stockees if i.utilisateur_id == utilisateur_id]
