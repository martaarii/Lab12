from database.DB_connect import DBConnect

from model.retailer import Retailer
from model.connessione import Connessione
class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getCountries():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Database non esiste")
            return
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct Country from go_retailers gr"""
        cursor.execute(query,())
        for row in cursor:
            result.append(row["Country"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getRetailersCountry(country):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Database non esiste")
            return
        cursor = cnx.cursor(dictionary=True)
        query = """select * from go_retailers gr 
                    where Country = %s """
        cursor.execute(query,(country,))
        for row in cursor:
            result.append(Retailer(**row))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getConnessioni(data, country):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Database non esiste")
            return
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT gds1.Retailer_code as R1, gds2.Retailer_code as R2, COUNT(distinct gds1.Product_number) AS product_count
                    FROM go_daily_sales gds1,  go_daily_sales gds2
                    where  YEAR(gds1.Date) = YEAR(gds2.Date)
                    and YEAR(gds2.Date) = %s
                    AND gds1.Product_number = gds2.Product_number
                    and gds1.Retailer_code in (select Retailer_code from go_retailers gr where Country = %s)
                    and gds2.Retailer_code in (select Retailer_code from go_retailers gr where Country = %s)
                    AND gds1.Retailer_code < gds2.Retailer_code
                    GROUP BY gds1.Retailer_code, gds2.Retailer_code
                    ORDER BY gds1.Retailer_code, gds2.Retailer_code;"""
        cursor.execute(query, (data,country,country))
        for row in cursor:
            result.append(Connessione(**row))
        cursor.close()
        cnx.close()
        return result
