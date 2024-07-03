from database.DB_connect import DBConnect
from model.situazione import Situazione


class MeteoDao():

    @staticmethod
    def get_umidita_media(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor()
            query = """SELECT s.Localita, AVG(s.Umidita)
                    FROM situazione s 
                    WHERE MONTH(s.Data) = %s
                    GROUP BY s.Localita"""
            cursor.execute(query, (mese,))
            result = cursor.fetchall()
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_situazioni_meta_mese(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s 
                        WHERE MONTH(s.Data) = %s AND DAY(s.Data) <= 15
                        ORDER BY s.Data ASC"""
            cursor.execute(query, (mese,))
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result


"""
from database.DB_connect import DBConnect
from model.situazione import Situazione


class MeteoDao():

    @staticmethod
    def get_all_situazioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s 
                        ORDER BY s.Data ASC
            cursor.execute(query)
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_situazione_umidita_media(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = select s.Localita, avg(Umidita)  as Media 
                        from situazione s 
                        where month (s.`Data`) = %s 
                        group by s.Localita 
            cursor.execute(query, (mese,))
            for row in cursor:
                result.append((row["Localita"], row["Media"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_situazione_meta_mese(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = select s.Localita, s.Data, s.Umidita
                            from situazione s 
                            where month (s.`Data`) = %s 
                            and day(s.`Data`) <15
                            order by s.`Data` asc 
            cursor.execute(query, (mese,))
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result
"""


