from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy import orm

Base = declarative_base()


class Author(Base):
    __tablename__ = "author"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)  
    name = sa.Column(sa.Text ,nullable=False)   

    def __repr__(self):
        return "<Author(id='{}', name='{}')>".format(self.id, self.name)
    

class Genres(Base):
    __tablename__ = "genre"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    genre = sa.Column(sa.Text, nullable=False)

    def __repr__(self):
        return "<Genre(id='{}', genre='{}')>".format(self.id ,self.genre)

class Books(Base):
    __tablename__ = "books"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.Text ,nullable=False)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('author.id'),nullable=False)
    pages = sa.Column(sa.Integer, nullable=False)
    genre_id = sa.Column(sa.Integer, sa.ForeignKey('genre.id'),nullable=False)
    public_date = sa.Column(sa.DateTime,nullable=False)

    def __repr__(self):
        return "Books(id='{}', title='{}', author_id='{}', pages='{}', genre_id='{}', public_date='{}')>".format(
            self.id, self.title, self.author_id, self.author_id, self.pages, self.genre_id, self.public_date
        )