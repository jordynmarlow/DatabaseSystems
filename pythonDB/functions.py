import sqlite3

def signUp(name, email, passowrd, username):
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    cur.execute('insert into members (name,email,password,username) VALUES (?,?,?,?,?)', (name, email, passowrd, username))
    con.commit()
    con.close()

def login():
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    cur.execute("select username, password from members")
    users = cur.fetchall()
    con.close()
    return users
