from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)



@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404
   
@app.route('/')
def app():
    return render_template('index.html')



