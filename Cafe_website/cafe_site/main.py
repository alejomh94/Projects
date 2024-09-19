from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from wtforms.fields.choices import SelectField
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])

    location = StringField('Location (URL)', validators=[DataRequired(), URL(message="Please enter a valid URL")])

    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=[
        ('0', '✘'), ('1', '☕️'), ('2', '☕️☕️'), ('3', '☕️☕️☕️'), ('4', '☕️☕️☕️☕️'), ('5', '☕️☕️☕️☕️☕️')
    ], validators=[DataRequired()])
    wifi = SelectField('Wifi Strength', choices=[
        ('0', '✘'), ('1', '💪'), ('2', '💪💪'), ('3', '💪💪💪'), ('4', '💪💪💪💪'), ('5', '💪💪💪💪💪')
    ], validators=[DataRequired()])
    power = SelectField('Power Availability', choices=[
        ('0', '✘'), ('1', '🔌'), ('2', '🔌🔌'), ('3', '🔌🔌🔌'), ('4', '🔌🔌🔌🔌'), ('5', '🔌🔌🔌🔌🔌')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = [
            form.cafe.data,
            form.location.data,
            form.open.data,
            form.close.data,
            form.coffee.data,
            form.wifi.data,
            form.power.data
        ]

        with open('cafe-data.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_cafe)
        return redirect(url_for('add_cafe'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    # Open the CSV file and read it as a dictionary
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.DictReader(csv_file)
        list_of_rows = [row for row in csv_data]  # Convert CSV rows to a list of dictionaries
    return render_template('cafes.html', cafes=list_of_rows)



if __name__ == '__main__':
    app.run(debug=True)
