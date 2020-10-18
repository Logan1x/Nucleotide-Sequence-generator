import os
from flask import Flask, render_template, request
import random

app = Flask(__name__)


nucleotide = ["A", "G", "T", "C"]


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def hello1():
    if int(request.form['len']) < 1:
        return render_template("index.html", error="Number has to be greater then 0")
    len = request.form['len']
    seq = ''.join([random.choice(nucleotide)
                   for nuc in range(int(len))])
    rev_seq = seq[::-1]
    rev_seq = rev_seq.replace("A", "t").replace(
        "T", "a").replace("G", "c").replace("C", "g").upper()
    # processed_text = text.upper()
    x = 1
    return render_template("index.html", seq=seq, rev_seq=rev_seq, x=x)


@app.route('/know-the-project/')
def know_the_project():
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug="True")
