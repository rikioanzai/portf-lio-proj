
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
   return render_template("index.html")

@app.route("/familia")
def fam():
   return render_template("familia-1.html")

@app.route("/informa")
def informa():
   return render_template ("informaeduca.html")
@app.route("/interesses")
def interesses():
   return render_template ("interesses.html")

@app.route("/portfolio")
def portfolio():
   return render_template ("portfólio.html")  
   
if __name__ == '__main__': app.run()