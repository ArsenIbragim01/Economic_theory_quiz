from flask import Flask, render_template, request, redirect, url_for
from questions import questions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        total = len(questions)
        user_answers = {}
        
        for q_id, question in questions.items():
            user_answer = request.form.get(f'q{q_id}')
            correct_answer = question['answer']
            
            user_answers[q_id] = {
                'user_answer': user_answer,
                'correct': user_answer == str(correct_answer),
                'explanation': question.get('explanation', '')
            }
            
            if user_answers[q_id]['correct']:
                score += 1
        
        return render_template('index.html', 
                             questions=questions, 
                             results=user_answers, 
                             score=score, 
                             total=total,
                             show_results=True)
    
    return render_template('index.html', questions=questions, show_results=False)

if __name__ == '__main__':
    app.run(debug=True)
