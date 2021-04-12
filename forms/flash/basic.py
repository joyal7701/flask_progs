from flask import Flask,flash,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
app=Flask(__name__)
app.config['SECRET_KEY']='kmykey'
class simpleform(FlaskForm):
    submit=SubmitField('clicl me.')
@app.route('/',methods=['GET','POST'])
def index():
    form=simpleform()
    if form.validate_on_submit():
        flash('you just clicked a button')
        return redirect(url_for('index'))
    return render_template('index.html',form=form)
if __name__=='__main__':
    app.run(debug=True)
