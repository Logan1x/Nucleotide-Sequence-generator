import os
from flask import Flask, render_template,request
import random

app = Flask(__name__)


nucleotide = ["A","G","T","C"]

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def hello1():
    len = request.form['len']
    seq = ''.join([random.choice(nucleotide)
               for nuc in range(int(len))])
    # processed_text = text.upper()
    x = 1
    return render_template("index.html", seq = seq , x=x)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)

