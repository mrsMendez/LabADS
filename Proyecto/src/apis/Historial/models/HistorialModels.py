from database.database import get_connection
from ..models.entities.Historial import Historial

class HistorialModel:
    @classmethod
    def get_all_historial(cls):
        try:
            connection = get_connection()
            historial_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_historial, cliente_id, producto_id, fecha, cantidad, precio_unitario
                    FROM historial ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    historial = Historial(
                        id_historial=row[0],
                        cliente_id=row[1],
                        producto_id=row[2],
                        fecha=row[3],
                        cantidad=row[4],
                        precio_unitario=float(row[5])
                    )
                    historial_list.append(historial.to_JSON())
            connection.close()
            return historial_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_historial_by_id(cls, id):
        try:
            connection = get_connection()
            historial_data = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_historial, cliente_id, producto_id, fecha, cantidad, precio_unitario
                    FROM historial
                    WHERE id_historial = %s
                """, (id),)
                row = cursor.fetchone()
                if row is not None:
                    historial = Historial(
                        id_historial=row[0],
                        cliente_id=row[1],
                        producto_id=row[2],
                        fecha=row[3],
                        cantidad=row[4],
                        precio_unitario=float(row[5])
                    )
                    historial_data = historial.to_JSON()
            connection.close()
            return historial_data
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_historial(cls, historial):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO historial (cliente_id, producto_id, fecha, cantidad, precio_unitario)
                    VALUES (%s, %s, %s, %s, %s)
                """, (historial.cliente_id, historial.producto_id, historial.fecha, historial.cantidad, historial.precio_unitario))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_historial(cls, id, historial):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE historial
                    SET cliente_id = %s, producto_id = %s, fecha = %s, cantidad = %s, precio_unitario = %s
                    WHERE id_historial = %s
                """, (historial.cliente_id, historial.producto_id, historial.fecha, historial.cantidad, historial.precio_unitario, id))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_historial(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM historial WHERE id_historial = %s", id,)
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)