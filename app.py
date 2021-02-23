from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
#file:///home/sreejeet/Desktop/eon/.projectscript/flask/formpage.html
@app.route('/index')
def hello():
    return render_template('formpage.html')

@app.route('/')
def index():
    return """ Start Process """

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run()
