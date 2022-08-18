from flask import Flask, render_template
from data import posts
from datamath import amrs
app= Flask(__name__)
posts= posts()
amrs=amrs()
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/blogger')
def blogger():
    return render_template('blogger.html',posts=posts)

@app.route('/post/<string:id>/')
def post(id):
    return render_template('post.html',id=id)


@app.route('/math')
def math():
    return render_template('math.html',amrs=amrs)



@app.route('/amr/<string:id1>/')
def amr(id1):
    return render_template('amr.html',id1=id1)     

if __name__=='__main__':
    app.run(debug=True)
