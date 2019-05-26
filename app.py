from flask import Flask, render_template, request
import random
app = Flask(__name__)


@app.route('/')
def strona():
    return render_template('strona.html')
@app.route('/tekst.html')
def tekst():
    if request.method == "POST":
        number = random.randint(1, 30)
        temp = open("gpt2_generated/gpt2_gentext%s.txt" % number, 'r')
        l = ' '.join(map(str, temp))
    return render_template('tekst.html', output=l)

if __name__ == '  strona  ':
    app.run(Debug=True)
