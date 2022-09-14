from flask import Flask, render_template, session, request,redirect
app = Flask(__name__)

app.config['SECRET_KEY'] = '10141990PR'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/process", methods= ['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)