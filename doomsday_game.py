from flask import Flask, render_template

app = Flask(__name__)

@app.route('/run_quiz', methods=['GET'])
def run_quiz():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run()

