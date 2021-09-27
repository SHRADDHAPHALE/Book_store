from flask import Blueprint,render_template,redirect,url_for
from bookstore import db
from bookstore.books.forms import AddForm,DelForm
from bookstore.models import Book

books_blueprint = Blueprint('books',__name__,template_folder='templates/books')

@books_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_book = Book(name)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('books.list'))

    return render_template('add.html',form=form)

@books_blueprint.route('/list')
def list():
    books = Book.query.all()
    return render_template('list.html', books=books)

@books_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        isbn = form.isbn.data
        book = Book.query.get(isbn)
        db.session.delete(book)
        db.session.commit()

        return redirect(url_for('books.list'))
    return render_template('delete.html',form=form)
