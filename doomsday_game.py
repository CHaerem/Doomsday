from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learning')
def learning():
    return render_template('learning.html')

@app.route('/quiz')
def run_quiz():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

