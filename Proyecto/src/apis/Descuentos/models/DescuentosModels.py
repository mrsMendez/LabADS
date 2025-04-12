from database.database import get_connection
from ..models.entities.Descuentos import Descuento

class DescuentosModel:
    @classmethod
    def get_all_descuento(cls):
        try:
            connection = get_connection()
            descuentos_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_descuento, producto_id, porcentaje, fecha_inicio, fecha_fin
                    FROM descuentos ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    descuento = Descuento(
                        id_descuento=row[0],
                        producto_id=row[1],
                        porcentaje=float(row[2]) if row[2] is not None else None,
                        fecha_inicio=row[3],
                        fecha_fin=row[4]
                    )
                    descuentos_list.append(descuento.to_JSON())
            connection.close()
            return descuentos_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_descuento_by_id(cls, id):
        try:
            connection = get_connection()
            descuento_data = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_descuento, producto_id, porcentaje, fecha_inicio, fecha_fin
                    FROM descuentos
                    WHERE id_descuento = %s
                """, id,)
                row = cursor.fetchone()
                if row is not None:
                    descuento = Descuento(
                        id_descuento=row[0],
                        producto_id=row[1],
                        porcentaje=float(row[2]) if row[2] is not None else None,
                        fecha_inicio=row[3],
                        fecha_fin=row[4]
                    )
                    descuento_data = descuento.to_JSON()
            connection.close()
            return descuento_data
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_descuento(cls, descuento):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO descuentos (producto_id, porcentaje, fecha_inicio, fecha_fin)
                    VALUES (%s, %s, %s, %s)
                """, (descuento.producto_id, descuento.porcentaje, descuento.fecha_inicio, descuento.fecha_fin))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_descuento(cls, id, descuento):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE descuentos
                    SET producto_id = %s, porcentaje = %s, fecha_inicio = %s, fecha_fin = %s
                    WHERE id_descuento = %s
                """, (descuento.producto_id, descuento.porcentaje, descuento.fecha_inicio, descuento.fecha_fin, id))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_descuento(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM descuentos WHERE id_descuento = %s", (id,))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)
