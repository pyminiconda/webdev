from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return "<p>This is the about page.</p>"


@app.route('/services')
def services():
  return "<p>This is the services page.</p>"


@app.route('/blogs')
def blogs():
  return "<p>This is the blogs page.</p>"


@app.route('/contact')
def contact():
  return "<p>This is the contact page.</p>"
  
if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True, port=8080)