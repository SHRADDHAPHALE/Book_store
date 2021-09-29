from bookstore import db


class Book(db.Model):

    __tablename__ = "books"
    isbn = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Book name is {self.name} with ISBN number as {self.isbn}"
