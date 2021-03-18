import csv, sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()
cur.execute("DROP TABLE books")
cur.execute("CREATE TABLE books (title text, author text, genre text, duration int, year int, available int, isbn int, bid int);")

with open('books.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['title'], i['author'], i['genre'], i['duration'], i['year'], i['available'], i['isbn'], i['bid']) for i in dr]
cur.executemany("INSERT INTO books ('title', 'author', 'genre', 'duration', 'year', 'available', 'isbn', 'bid') VALUES (?,?,?,?,?,?,?,?);", to_db)
#con.commit()
#con.close()

