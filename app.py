from books import app, db
from flask import render_template, redirect, url_for
from books.forms import AddForm, DelForm
from books.models import Book

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/add", methods=["GET", "POST"])
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
def list():
    books = Book.query.all()
    return render_template("list.html", books=books)


@app.route("/delete", methods=["GET", "POST"])
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
    app.run(debug=True)
