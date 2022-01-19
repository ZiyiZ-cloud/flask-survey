from http.client import responses
from typing import final
from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys, satisfaction_survey, personality_quiz

RESPONSES = "responses"


app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY'] = "key"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    
    satisfaction= satisfaction_survey
        
    return render_template('homepage.html',satisfaction=satisfaction)


@app.route('/begin')
def begin_page():
    
    session[RESPONSES]=[]


    return redirect('/questions/0')

@app.route('/questions/<int:questionid>')
def questions_page(questionid):
    responses = session.get(RESPONSES)

    satisfaction= satisfaction_survey
    
    if (responses is None):
        return redirect("/")

    if (len(responses) != questionid):
        flash(f"Invalid question id: {questionid}.")
        return redirect(f"/questions/{len(responses)}")

    
    return render_template('questions.html',question_num=questionid, satisfaction=satisfaction)
    
    


@app.route('/result', methods=['POST'])
def survey_result():

    
    answer= request.form['result']
    final_result=session[RESPONSES]
    final_result.append(answer)
    session[RESPONSES]=final_result    
    
    if len(final_result) == len(satisfaction_survey.questions):
        return render_template('result.html',answer=final_result)
    else:
        return redirect(f'/questions/{len(final_result)}')
    


@app.route('/thankyou',methods=['POST'])
def thankyou_page():
    return render_template('thankyou.html')