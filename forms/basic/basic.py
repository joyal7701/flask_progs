from flask import Flask, render_template
app = Flask(__name__)

'''@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/information')
def info():
    return '<h1>puppies are cute</h1>'
@app.route('/puppy/<name>')
def puppy(name):
    return '<h1>this is apage for {}</h1>'.format(name)#name.upper()'''


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
