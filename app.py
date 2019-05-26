from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def strona():
    return render_template('strona.html')
@app.route('/tekst.html')
def tekst():
    return render_template('tekst.html')

if __name__ == '  strona  ':
    app.run(Debug=True)
