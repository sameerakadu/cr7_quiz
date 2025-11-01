import tkinter as tk
from tkinter import messagebox
import random
import time

# Ronaldo Quiz Questions & Answers
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

class QuizUI:
    def __init__(self, master):
        self.master = master
        master.title("Cristiano Ronaldo Quiz")
        self.score = 0
        self.q_index = 0
        self.questions = questions.copy()
        random.shuffle(self.questions)
        self.total_questions = len(self.questions)

        self.question_label = tk.Label(master, text="", font=("Arial", 14), wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(master, text="", font=("Arial", 12), width=30, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.status_label = tk.Label(master, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.next_button = tk.Button(master, text="Next", font=("Arial", 12), command=self.next_question, state="disabled")
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.q_index < self.total_questions:
            q = self.questions[self.q_index]
            self.question_label.config(text=f"Q{self.q_index+1}: {q['question']}")
            for i, option in enumerate(q['options']):
                self.option_buttons[i].config(text=option, state="normal")
            self.status_label.config(text="")
            self.next_button.config(state="disabled")
        else:
            self.show_result()

    def check_answer(self, idx):
        q = self.questions[self.q_index]
        selected = q['options'][idx]
        for btn in self.option_buttons:
            btn.config(state="disabled")
        if selected.lower() == q['answer'].lower():
            self.score += 1
            self.status_label.config(text="✅ Correct!", fg="green")
        else:
            self.status_label.config(text=f"❌ Wrong! Correct: {q['answer']}", fg="red")
        self.next_button.config(state="normal")

    def next_question(self):
        self.q_index += 1
        self.show_question()

    def show_result(self):
        msg = f"Your final score: {self.score}/{self.total_questions}\n"
        if self.score == self.total_questions:
            msg += "🎉 Incredible! You’re a true Ronaldo legend!"
        elif self.score >= self.total_questions * 0.7:
            msg += "🔥 Great job! You really know your CR7 facts!"
        elif self.score >= self.total_questions * 0.4:
            msg += "⚽ Not bad! A few more games and you’ll be a pro!"
        else:
            msg += "😅 Time to watch some Ronaldo highlights and try again!"
        messagebox.showinfo("Quiz Over", msg)
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = QuizUI(root)
    root.mainloop()