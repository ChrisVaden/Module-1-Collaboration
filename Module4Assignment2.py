

# 23.1

# books_data = """author,book
# J R R Tolkien,The Hobbit
# Lynne Truss,"Eats, Shoots & Leaves"
# """

# with open('books.csv', 'wt', encoding='utf-8') as f:
#   f.write(books_data.strip())

# 23.2

# import csv

# books = []
# with open('books.csv', 'rt', encoding='utf-8') as f:
#   reader = csv.DictReader(f)
#   for row in reader:
#     books.append(row)

# print("23.2 Books dictionary list:")
# print(books)

# 23.3

# books2_data = """title,author,year
# The Weirdstone of Brisingamen,Alan Garner,1960
# Perdido Street Station,China Miéville,2000
# Thud!,Terry Pratchett,2005
# The Spellman Files,Lisa Lutz,2007
# Small Gods,Terry Pratchett,1992
# """

# with open('books2.csv', 'wt', encoding='utf-8') as f:
#   f.write(books2_data.strip())

# 23.4

# import sqlite3

# db = sqlite3.connect('books.db')
# cursor = db.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS books (
#         title TEXT,
#         author TEXT,
#         year INTEGER
#     )
# ''')
# db.commit()

# 23.5

# import csv

# with open('books2.csv', 'rt', encoding='utf-8') as f:
#   reader = csv.DictReader(f)
#   for row in reader:
#     cursor.execute(
#         'INSERT INTO books VALUES (?, ?, ?)',
#         (row['title'], row['author'], row['year']),
#     )

# db.commit()

# 23.6

# cursor.execute('SELECT title FROM books ORDER BY title ASC')
# print("23.6 Titles in alphabetical order:")
# for row in cursor.fetchall():
#   print(row[0])

# 23.7

# cursor.execute('SELECT * FROM books ORDER BY year ASC')
# print("\n23.7 All columns ordered by publication year:")
# for row in cursor.fetchall():
#   print(row)

# # Close the native sqlite connection when finished with raw sqlite
# db.close()

# 23.8

# import sqlalchemy as sa

# # Connect to the database using SQLAlchemy
# engine = sa.create_engine('sqlite:///books.db')

# print("\n23.8 Titles in alphabetical order via SQLAlchemy:")
# with engine.connect() as connection:
#   # Use sa.text() for modern SQLAlchemy compatibility
#   result = connection.execute(sa.text('SELECT title FROM books ORDER BY title'))
#   for row in result:
#     print(row[0])



