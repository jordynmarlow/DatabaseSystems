import sqlite3
import pandas as pd

#Connect to SQLite database
con = sqlite3.connect(r'library.db')
#Create cursor object
cur = con.cursor()

#LOAD THE CSV INTO PANDAS
bookData = pd.read_csv('bookData.csv')
#Write the data to books table
cur.execute('drop table books')
bookData.to_sql('books', con, if_exists = 'replace', index=False)

#Create cursor object

for row in cur.execute('select * from books'):
        print (row)

