import sqlite3
class daerahWisata:
    def __init__(self, idDaerah: int, namDaerah: int) -> None:
        self.__idDaerah = idDaerah
        self.__namDaerah = namDaerah
    
    def getID(self) -> int:
        return self.__idDaerah
    
    def getNama(self) -> str:
        return self.__namDaerah
    
    def getListDestinasiFromDaerah(self) -> list:
        # Yang dikembalikan adalah hasil query
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        query = "select * from lokasiwisata where daerah = ?"
        c.execute(query, str(self.__idDaerah))
        return c.fetchall()