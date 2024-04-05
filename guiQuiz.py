import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        
        self.conn = sqlite3.connect('assessDB.db')
        self.cursor = self.conn.cursor()
        
        self.categories = ["History", "Management", "Database", "Python", "Accounting"]
        self.selected_category = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Select Category:").pack()
        for category in self.categories:
            tk.Radiobutton(self.root, text=category, variable=self.selected_category, value=category).pack()
        
        tk.Button(self.root, text="Submit", command=self.start_quiz).pack()
    
    def start_quiz(self):
        category = self.selected_category.get()
        if category:
            self.show_questions(category)
        else:
            messagebox.showerror("Error", "Please select a category!")
    
    def show_questions(self, category):
        questions_window = tk.Toplevel(self.root)
        questions_window.title(f"{category} Questions")
        
        self.cursor.execute(f"SELECT question, answer FROM {category.lower()}")
        questions = self.cursor.fetchall()
        random.shuffle(questions)
        
        self.answers = {}
        for i, (question, answer) in enumerate(questions):
            frame = tk.Frame(questions_window)
            frame.pack(pady=5)
            
            tk.Label(frame, text=f"Question {i+1}: {question}").pack(anchor="w")
            entry = tk.Entry(frame)
            entry.pack(anchor="w")
            submit_btn = tk.Button(frame, text="Submit", command=lambda q=question, a=answer, e=entry: self.check_answer(q, a, e))
            submit_btn.pack(anchor="w")
            result_label = tk.Label(frame)
            result_label.pack(anchor="w")
            self.answers[question] = (entry, result_label)
        
        self.questions_window = questions_window
    
    def check_answer(self, question, answer, entry):
        user_answer = entry.get().strip()
        if user_answer.lower() == answer.lower():
            entry.config(bg="green")
            self.answers[question][1].config(text="Correct", fg="green")
        else:
            entry.config(bg="red")
            self.answers[question][1].config(text="Incorrect", fg="red")
    
    def reset_answers(self):
        for entry, label in self.answers.values():
            entry.delete(0, tk.END)
            entry.config(bg="white")
            label.config(text="")
        
    def destroy_questions_window(self):
        if hasattr(self, 'questions_window'):
            self.questions_window.destroy()
    
    def close_connection(self):
        self.conn.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
