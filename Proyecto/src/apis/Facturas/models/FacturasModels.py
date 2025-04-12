from database.database import get_connection
from ..models.entities.Facturas import Factura

class FacturasModel:
    @classmethod
    def get_all_Factura(cls):
        try:
            connection = get_connection()
            facturas_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_factura, compra_id, fecha, total
                    FROM facturas ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    factura = Factura(
                        id_factura=row[0],
                        compra_id=row[1],
                        fecha=row[2],
                        total=float(row[3])
                    )
                    facturas_list.append(factura.to_JSON())
            connection.close()
            return facturas_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_Factura_by_id(cls, id):
        try:
            connection = get_connection()
            factura_data = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_factura, compra_id, fecha, total
                    FROM facturas
                    WHERE id_factura = %s
                """, (str(id),))
                row = cursor.fetchone()
                if row is not None:
                    factura = Factura(
                        id_factura=row[0],
                        compra_id=row[1],
                        fecha=row[2],
                        total=float(row[3])
                    )
                    factura_data = factura.to_JSON()
            connection.close()
            return factura_data
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_Factura(cls, factura):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO facturas (compra_id, fecha, total)
                    VALUES (%s, %s, %s)
                """, (factura.compra_id, factura.fecha, factura.total))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_Factura(cls, id, factura):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE facturas
                    SET compra_id = %s, fecha = %s, total = %s
                    WHERE id_factura = %s
                """, (factura.compra_id, factura.fecha, factura.total, id))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_Factura(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM facturas WHERE id_factura = %s", id,)
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)