from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import PLL_Address_Book
from app.models import Address



@app.route('/')
def index():
    return render_template ("index.html")
   

@app.route('/pll_address', methods=["GET", "POST"])
def pll_address():
    form = PLL_Address_Book()
    print("hello world")
    if form.validate_on_submit():
        print('Form Validated!')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        new_address = Address(first_name=first_name, last_name=last_name, phone_number = phone_number, address=address)

        db.session.add(new_address)
        db.session.commit()
        # if first_name != 'Pretty Little Liar' or  'secretcanyoukeepit':
        #     flash('Invalid username and/or email', 'danger')
        #     return redirect(url_for('pll_address'))
        # else:
        flash(f'{first_name} has successfully added another PLL', 'Great Job')
        return redirect(url_for('pll_address'))
    return render_template('pll_address.html', form=form)