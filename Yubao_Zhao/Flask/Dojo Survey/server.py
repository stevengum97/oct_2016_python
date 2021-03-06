from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def show_user():
    return render_template("result.html", user=request.form)

if __name__ == '__main__':
    app.run(debug=True)
