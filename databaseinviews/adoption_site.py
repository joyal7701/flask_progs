import os
from forms import Addform, Delform, Addowner
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
'''
app.config['SECRET_KEY'] = 'mysecretkeys'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
'''
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkeys'
db = SQLAlchemy(app)
Migrate(app, db)


class puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"puppy name: {self.name} and no owner assigned yet!"


class owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"owner name: {self.name}"


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add_owner', methods=['GET', 'PSOT'])
def add_owner():
    form = Addowner()
    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        new_owner = owner(name, pup_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add_owner.html', form=form)


@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = Addform()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():
    puppies = puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():
    form = Delform()
    if form.validate_on_submit():
        id = form.id.data
        pup = puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
