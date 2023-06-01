from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import PLL_Address_Book


@app.route('/')
def index():
    return render_template ("index.html")
   

@app.route('/pll_address', methods=["GET", "POST"])
def pll_address():
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
            return redirect(url_for('pll_address'))
    return render_template('pll_address.html', form=form)