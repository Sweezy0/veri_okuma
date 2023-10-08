import sqlite3
con=sqlite3.connect("sirket.db")
cursor=con.cursor()
def veri_oku():
    cursor.execute("Select*from elemanlar")
    veri=cursor.fetchall()
    print(veri)
veri_oku()
con.close()