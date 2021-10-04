from books import app, db
import os
from flask import render_template, redirect, url_for, request, flash
from books.forms import AddForm, DelForm,LoginForm, RegistrationForm
from books.models import Book, User
from flask_login import login_user,login_required,logout_user


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Logged In !')
            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('welcome_user')

            return redirect(next)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Successfully registered ! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_book = Book(name)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("list"))

    return render_template("add.html", form=form)


@app.route("/list")
@login_required
def list():
    books = Book.query.all()
    return render_template("list.html", books=books)


@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():

    form = DelForm()

    if form.validate_on_submit():
        isbn = form.isbn.data
        book = Book.query.get(isbn)
        db.session.delete(book)
        db.session.commit()

        return redirect(url_for("list"))
    return render_template("delete.html", form=form)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host="0.0.0.0", port=port)