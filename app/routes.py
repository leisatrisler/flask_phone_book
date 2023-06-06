from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import AddressBook, Home, LoginForm, SignUpForm
from app.models import Address


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/address", methods=["GET", "POST"])
def address():
    form = AddressBook()
    if form.validate_on_submit():
        print("Form Validated!")
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        new_address = Address(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
        )

        db.session.add(new_address)
        db.session.commit()
        # if first_name != 'Pretty Little Liar' or  'secretcanyoukeepit':
        #     flash('Invalid username and/or email', 'danger')
        #     return redirect(url_for('pll_address'))
        # else:
        flash(f"{first_name} has successfully added another PLL", "Great Job")
        return redirect(url_for("address"))
    return render_template("address.html", form=form)


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up_form():
    form = SignUpForm()
    if form.validate_on_submit():
        print("Signup Validated!")
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        confirm_pass = form.confirm_pass.data

        db.session.add(form)
        db.session.commit()
        # if first_name != 'Pretty Little Liar' or  'secretcanyoukeepit':
        #     flash('Invalid username and/or email', 'danger')
        #     return redirect(url_for('pll_address'))
        # else:
        flash(f"{first_name} has successfully added another PLL", "Great Job")
        return redirect(url_for("address"))
    return render_template("address.html", form=form)
