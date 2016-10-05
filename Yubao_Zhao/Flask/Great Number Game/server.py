from flask import Flask, render_template, redirect, request, session
from random import randint

app = Flask(__name__)
app.secret_key = "\x9eh\xb7;)\x10\xf0{\xb7\xf1\x95\xbb?Y*\xd4\x83Q\xfa\xa8\x14\x99s\x96"

@app.route('/')
def index():
    if 'random' not in session:
        session['random'] = randint(1,100)
    # print "Random:", session['random']
    return render_template("index.html")

@app.route('/process', methods = ['POST'])
def process():
    if request.form['number']:
        guess = int(request.form['number'])
        # print "Guess:", guess
    else:
        return redirect('/')
    return render_template("index.html", guess=guess)

@app.route('/restart')
def restart():
    session.pop('random')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
