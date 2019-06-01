from flask import Flask
from flask import render_template, request, redirect

#https://technext.github.io/medino/index.html

#from configuraciones import *
#import psycopg2
#conn = psycopg2.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,passwd))
#cur = conn.cursor()


app= Flask(__name__)


@app.route('/')


@app.route('/index.html')
def index():
	return render_template("index.html")

@app.route('/departments.html')
def dep():
	return render_template("departments.html")

@app.route('/contact.html')
def contact():
	return render_template("contact.html")

@app.route('/about.html')
def about():
	return render_template("about.html")

@app.route('/blog-home.html')
def blog():
	return render_template("blog-home.html")

if __name__== "__main__":
	app.run()