from . import app
from flask import render_template, request

names = []


@app.route('/', methods=['GET', 'POST'])
def home():
    # global names
    if request.method == 'POST':
        name = request.form['name']
        print('Hello')
        if name in names:
            message = f"Вже бачилися, {name}"
            print('Hello name')
            return render_template('home.html', message=message)
        else:
            names.append(name)
            message = f"Привіт, {name}"
            return render_template('home.html', message=message)
    return render_template('home.html')


@app.route('/show_all')
def show_all():
    return render_template('show_all.html', names=names)
