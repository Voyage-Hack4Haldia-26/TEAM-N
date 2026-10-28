import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
CORS(app)
BASE = os.path.dirname(os.path.abspath(__file__))


@app.get("/")
def index():
    return send_from_directory(BASE, "index.html")


@app.get("/health")
def health():
    return jsonify(status="ok", project="Team N: AI Study Planner + Quiz", stack="flask")

@app.route("/api/plan", methods=["POST"])
def ep_0(**kwargs):
    # TODO: Body: {syllabus, days} -> plan
    return jsonify(error="Not implemented", todo="Body: {syllabus, days} -> plan"), 501

@app.route("/api/quiz", methods=["POST"])
def ep_1(**kwargs):
    # TODO: Body: {topic} -> questions[]
    return jsonify(error="Not implemented", todo="Body: {topic} -> questions[]"), 501

@app.route("/api/review", methods=["POST"])
def ep_2(**kwargs):
    # TODO: Body: {cardId, quality} -> next review date
    return jsonify(error="Not implemented", todo="Body: {cardId, quality} -> next review date"), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
