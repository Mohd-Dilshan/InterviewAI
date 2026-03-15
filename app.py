from flask import Flask, render_template, request, jsonify
from interview_engine import generate_questions
from analyzer import analyze_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start_interview", methods=["POST"])
def start_interview():
    role = request.json["role"]
    questions = generate_questions(role)
    return jsonify({"questions": questions})

@app.route("/analyze", methods=["POST"])
def analyze():
    answer = request.json["answer"]
    feedback = analyze_answer(answer)
    return jsonify({"feedback": feedback})

if __name__ == "__main__":
    app.run(debug=True)