from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys, satisfaction_survey, personality_quiz

app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY'] = "key"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    
    satisfaction= satisfaction_survey
    
    return render_template('homepage.html',satisfaction=satisfaction)



@app.route('/questions')
def questions_page():
    satisfaction= satisfaction_survey
    
    return render_template('questions.html',satisfaction=satisfaction)
    


@app.route('/result', methods=['POST'])
def survey_result():
    user_result=[]
    answer= request.form['result']
    user_result.append(answer)
    return render_template('result.html',answer=user_result)

@app.route('/thankyou',methods=['POST'])
def thankyou_page():
    return render_template('thankyou.html')