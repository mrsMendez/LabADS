from database.database import get_connection
from ..models.entities.Pagos import Pago

class PagosModel:
    @classmethod
    def get_all_pago(cls):
        try:
            connection = get_connection()
            pagos_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_pago, factura_id, monto, metodo_pago, fecha
                    FROM pagos ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    pago = Pago(
                        id_pago=row[0],
                        factura_id=row[1],
                        monto=float(row[2]),
                        metodo_pago=row[3],
                        fecha=row[4]
                    )
                    pagos_list.append(pago.to_JSON())
            connection.close()
            return pagos_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_pago_by_id(cls, id):
        try:
            connection = get_connection()
            pago_data = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_pago, factura_id, monto, metodo_pago, fecha
                    FROM pagos
                    WHERE id_pago = %s
                """, (id,))
                row = cursor.fetchone()
                if row is not None:
                    pago = Pago(
                        id_pago=row[0],
                        factura_id=row[1],
                        monto=float(row[2]),
                        metodo_pago=row[3],
                        fecha=row[4]
                    )
                    pago_data = pago.to_JSON()
            connection.close()
            return pago_data
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_pago(cls, pago):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO pagos (factura_id, monto, metodo_pago, fecha)
                    VALUES (%s, %s, %s, %s)
                """, (pago.factura_id, pago.monto, pago.metodo_pago, pago.fecha))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_pago(cls, id, pago):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE pagos
                    SET factura_id = %s, monto = %s, metodo_pago = %s, fecha = %s
                    WHERE id_pago = %s
                """, (pago.factura_id, pago.monto, pago.metodo_pago, pago.fecha, id))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_pago(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM pagos WHERE id_pago = %s", id,)
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)