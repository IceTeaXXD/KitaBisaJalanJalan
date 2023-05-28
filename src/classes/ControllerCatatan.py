import sqlite3
class controllerCatatan:
    def __init__(self, id, catatan):
        self.catatan = catatan
        self.id = id

    def saveCatatan(self, catatan):
        # Save the catatan to the database
        self.catatan = catatan

    def submitCatatan(self):
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        query = """update catatan set isi = :catatan where ID_Catatan = :id"""
        with conn:
            c.execute(query, {'id':self.id, 'catatan':self.catatan})

    def getCatatan(self):
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        query = """select * from catatan where ID_Catatan = :id"""
        c.execute(query, {'id': self.id})
        return c.fetchall()