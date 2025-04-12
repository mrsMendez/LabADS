from database.database import get_connection
from ..models.entities.Compras import Compra

class ComprasModel:
    @classmethod
    def get_all_compra(cls):
        try:
            connection = get_connection()
            compras_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_compra, cliente_id, fecha, total
                    FROM compras ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    compra = Compra(
                        id_compra=row[0],
                        cliente_id=row[1],
                        fecha=row[2],
                        total=float(row[3])
                    )
                    compras_list.append(compra.to_JSON())
            connection.close()
            return compras_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_compra_by_id(cls, id):
        try:
            connection = get_connection()
            compra_data = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_compra, cliente_id, fecha, total
                    FROM compras
                    WHERE id_compra = %s
                """, (id,))
                row = cursor.fetchone()
                if row is not None:
                    compra = Compra(
                        id_compra=row[0],
                        cliente_id=row[1],
                        fecha=row[2],
                        total=float(row[3])
                    )
                    compra_data = compra.to_JSON()
            connection.close()
            return compra_data
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_compra(cls, compra):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO compras (cliente_id, fecha, total)
                    VALUES (%s, %s, %s)
                """, (compra.cliente_id, compra.fecha, compra.total))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_compra(cls, id, compra):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE compras
                    SET cliente_id = %s, fecha = %s, total = %s
                    WHERE id_compra = %s
                """, (compra.cliente_id, compra.fecha, compra.total, id))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_compra(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM compras WHERE id_compra = %s", (id),)
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)