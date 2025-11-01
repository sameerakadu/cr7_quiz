from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'cr7_secret_key'  # Needed for session

questions = [
    {
        "question": "In which year did Cristiano Ronaldo join Real Madrid?",
        "options": ["2007", "2008", "2009", "2010"],
        "answer": "2009"
    },
    {
        "question": "How many goals did Ronaldo score in the 2018 FIFA World Cup?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Which club did Ronaldo join after leaving Real Madrid?",
        "options": ["Juventus", "Manchester United", "Al-Nassr", "Sporting CP"],
        "answer": "Juventus"
    },
    {
        "question": "What is Ronaldo’s famous celebration shout?",
        "options": ["Vamos!", "Siiiuuu!", "Força!", "Goal!"],
        "answer": "Siiiuuu!"
    },
    {
        "question": "How many Ballon d'Or titles has Ronaldo won (as of 2023)?",
        "options": ["3", "4", "5", "6"],
        "answer": "5"
    },
    {
        "question": "What is Cristiano Ronaldo’s jersey number for Portugal?",
        "options": ["7", "9", "10", "11"],
        "answer": "7"
    },
    {
        "question": "Which country is Ronaldo from?",
        "options": ["Spain", "Portugal", "Brazil", "Argentina"],
        "answer": "Portugal"
    },
    {
        "question": "At which club did Ronaldo start his professional career?",
        "options": ["Sporting CP", "Benfica", "Porto", "Andorinha"],
        "answer": "Sporting CP"
    },
    {
        "question": "In which year was Cristiano Ronaldo born?",
        "options": ["1984", "1985", "1986", "1987"],
        "answer": "1985"
    },
    {
        "question": "Which team did Ronaldo join in 2023?",
        "options": ["Manchester United", "Juventus", "Al-Nassr", "Real Madrid"],
        "answer": "Al-Nassr"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_questions')
def get_questions():
    q = questions.copy()
    random.shuffle(q)
    session['quiz'] = q  # Store shuffled questions in session
    q_no_answers = []
    for item in q:
        q_item = item.copy()
        q_item.pop('answer', None)
        q_no_answers.append(q_item)
    return jsonify(q_no_answers)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    q_idx = data.get('q_idx')
    selected = data.get('selected')
    quiz = session.get('quiz', questions)
    correct = quiz[q_idx]['answer']
    return jsonify({"correct": selected == correct, "answer": correct})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
