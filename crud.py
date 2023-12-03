from datetime import datetime

from sqlalchemy import create_engine, text
from config import DATABASE_URI
from models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import or_

engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

s = Session()

author1 = Author(name='George R. R. Martin')
author2 = Author(name='J.K. Rowling')
author3 = Author(name='Antoine de Saint-Exupéry')
author4 = Author(name='Stephen King')

genre1 = Genres(genre = 'Dark Fantasy')
genre2 = Genres(genre = 'Fantasy')
genre3 = Genres(genre= 'Fairy Tales')
genre4 = Genres(genre ='Horror')


book1_author_id = s.query(Author.id).first()
for i in book1_author_id:
    a1 = i

book2_author_id = s.query(Author.id).filter(Author.id==2).all()
for i in book2_author_id:
    for j in i:
        a2 = j

book3_author_id = s.query(Author.id).filter(Author.id==3).all()
for i in book3_author_id:
    for j in i:
        a3 = j

book4_author_id = s.query(Author.id).filter(Author.id==4).all()
for i in book4_author_id:
    for j in i:
        a4 = j


book1_genre_id = s.query(Genres.id).first()
for i in book1_genre_id:
    g1 = i
    
book2_genre_id = s.query(Genres.id).filter(Genres.id==2).all()
for i in book2_genre_id:
    for j in i:
        g2 = j
        
book3_genre_id = s.query(Genres.id).filter(Genres.id==3).all()
for i in book3_genre_id:
    for j in i:
        g3 = j    

book4_genre_id = s.query(Genres.id).filter(Genres.id==4).all()
for i in book4_genre_id:
    for j in i:
        g4 = j
        
book1 = Books(title='Game of Thrones', author_id=a1, pages=694, genre_id=g1, public_date=datetime(1996,1,1))
book2 = Books(title='Clash of Kings', author_id=a1, pages=706, genre_id=g1, public_date=datetime(1998,4,15))
book3 = Books(title='Storm of Swords', author_id=a1, pages=683, genre_id=g1, public_date=datetime(2000,1,1))
book4 = Books(title='Philosophers Stone', author_id=a2, pages=555, genre_id=g2, public_date=datetime(1997,1,1))
book5 = Books(title='It(nevel)', author_id=a4, pages=666, genre_id=g4, public_date=datetime(2001,1,1))
book6 = Books(title='Litle Prince', author_id=a3, pages=456, genre_id=g3, public_date=datetime(1943,1,1))
book7 = Books(title=' The Dark Half', author_id=a4, pages=777, genre_id=g4, public_date=datetime(1989,12,12))
book9 = Books(title='Goblet of Fire ', author_id=a2, pages=532, genre_id=g2, public_date=datetime(2000,1,12))
book8 = Books(title='Feast for Crows', author_id=a1, pages=556, genre_id=g1, public_date=datetime(2005,1,12))
# s.add_all([author2,author3,author4,genre2,genre3,genre4])
# s.add_all([book2,book3,book4,book5,book5,book6,book7,book8])
# s.add(book9)
# print(s.query(Books).all())

#Подзапрос
result = s.query(Books.title,Author.name,Genres.genre,Books.pages,Books.public_date).filter(Books.author_id==Author.id,Books.genre_id==Genres.id).all()
# print(result)
def search_by_author(author_id):
    return s.query(Books.title,Author.name,Genres.genre,Books.pages,Books.public_date).filter(Books.author_id==Author.id,Books.genre_id==Genres.id).where(Author.id==author_id).all()

def search_by_genre_id(genre_id):
    return s.query(Books.title,Author.name,Genres.genre,Books.pages,Books.public_date).filter(Books.author_id==Author.id,Books.genre_id==Genres.id).where(Genres.id==genre_id).all()

def search_by_name(name_book):
    return s.query(Books.title,Author.name,Genres.genre,Books.pages,Books.public_date).filter(Books.author_id==Author.id,Books.genre_id==Genres.id).where(Books.title==name_book).all()

# print(search_by_name("Game of Thrones"))
# print(search_by_author(int(input("""Filter by author:\n[1]George R.R Martin  [2]J.K. Rowling
# [3]Stephen King  [4]Robert Louis Stevenson\n"""))))

# print(search_by_genre_id(int(input("""Filter by genre:\n[1]Dark Fantasy  [2]Fantasy\n[3]Fairy Tales  [4]Horror\n"""))))

#Views
# sql = text(f"""Create VIEW my_view
# AS SELECT Books.title
# FROM books""")
# s.execute(sql) 
# result1 =s.execute(text("Select * from my_view")).all()
# for i in result1:
#     for j in i:
#         print(j,end=" , ")

# Агрегатные функции
def max_pages(s: Session):
    return s.execute(text("Select MAX(pages) from Books")).all()
max_p = max_pages(s)[0][0]
print(s.query(Books.title,Author.name,Genres.genre,Books.pages,Books.public_date).filter(Books.author_id==Author.id,Books.genre_id==Genres.id).where(Books.pages==max_p).all())
s.commit()
s.close()