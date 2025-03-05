from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__)

# Fonction pour lire un fichier JSON
def read_json(filename):
    filepath = os.path.join("data", filename)
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

# Route API pour récupérer les événements
@app.route("/api/events", methods=["GET"])
def get_events():
    events = read_json("events.json")
    return jsonify(events)

# Route API pour récupérer les actualités
@app.route("/api/news", methods=["GET"])
def get_news():
    news = read_json("news.json")
    return jsonify(news)

# Page principale (affichage HTML des données)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
