from app import app
from flask import render_template, redirect, url_for, flash
from forms import PLL_Address_Book


@app.route('/')
def pll_address():
    return "Hello Beautiful People"
   

@app.route('/pll_address', methods=["GET", "POST"])
def login():
    form = PLL_Address_Book()
    if form.validate_on_submit():
        print('Form Validated!')
        username = form.username.data
        print(username)
        if username != 'Pretty Little Liar' or  'secretcanyoukeepit':
            flash('Invalid username and/or email', 'danger')
            return redirect(url_for('ppl address'))
        else:
            flash(f'{username} has successfully added another PLL', 'Great Job')
            return redirect(url_for('index'))
    return render_template('ppl_address.html', form=form)