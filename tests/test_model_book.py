from books.models import Book
from books import db

def test_book():
    newbook = Book("Peril")

    db.session.add(newbook)
    x = db.session.commit()
    print(x)

    assert(1==1)
