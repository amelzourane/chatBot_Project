# Point d'entrée de l'API Flask
# app.py

from flask import Flask, request, jsonify
from models.agent import ChatbotSupport
from models.user import Utilisateur
from models.database import BaseDeDonnees
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Initialisation
chatbot = ChatbotSupport("TechBot")
bdd = BaseDeDonnees()
utilisateurs = {
    1: Utilisateur(1, "Alice", "alice@example.com")
}

@app.route("/ask", methods=["POST"])
def poser_question():
    data = request.get_json()
    user_id = data.get("user_id")
    question = data.get("question")

    if not user_id or not question:
        return jsonify({"error": "user_id et question sont requis."}), 400

    user = utilisateurs.get(user_id)
    if not user:
        return jsonify({"error": "Utilisateur introuvable."}), 404

    reponse = user.poser_question(chatbot, bdd, question)
    return jsonify({"reponse": reponse})

@app.route("/memory/<int:user_id>", methods=["GET"])
def afficher_historique(user_id):
    user = utilisateurs.get(user_id)
    if not user:
        return jsonify({"error": "Utilisateur introuvable."}), 404
    return jsonify(user.voir_historique())

@app.route("/memory/reset", methods=["POST"])
def reinitialiser():
    chatbot.reinitialiser()
    return jsonify({"message": "Mémoire du chatbot réinitialisée."})

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = utilisateurs.get(user_id)
    if not user:
        return jsonify({"error": "Utilisateur introuvable."}), 404
    return jsonify({"id": user.id, "nom": user.nom, "email": user.email})

if __name__ == "__main__":
    app.run(debug=True)
