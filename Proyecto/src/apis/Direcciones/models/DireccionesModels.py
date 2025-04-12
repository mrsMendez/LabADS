from database.database import get_connection
from ..models.entities.Direccion import Direccion

class DireccionModel:

    @classmethod
    def get_all_direcciones(cls):
        try:
            connection = get_connection()
            direcciones_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_direccion, cliente_id, direccion, ciudad, pais
                    FROM direcciones
                    ORDER BY ciudad ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    direccion = Direccion(
                        id_direccion=row[0],
                        cliente_id=row[1],
                        direccion=row[2],
                        ciudad=row[3],
                        pais=row[4]
                    )
                    direcciones_list.append(direccion.to_JSON())
            connection.close()
            return direcciones_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_direccion_by_id(cls, direccion_id):
        try:
            connection = get_connection()
            direccion_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_direccion, cliente_id, direccion, ciudad, pais
                    FROM direcciones
                    WHERE id_direccion = %s
                """, (direccion_id,))
                row = cursor.fetchone()
                if row is not None:
                    direccion = Direccion(
                        id_direccion=row[0],
                        cliente_id=row[1],
                        direccion=row[2],
                        ciudad=row[3],
                        pais=row[4]
                    )
                    direccion_json = direccion.to_JSON()
            connection.close()
            return direccion_json
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_direccion(cls, direccion: Direccion):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO direcciones 
                    (id_direccion, cliente_id, direccion, ciudad, pais)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    direccion.id_direccion,
                    direccion.cliente_id,
                    direccion.direccion,
                    direccion.ciudad,
                    direccion.pais
                ))
                affected_rows = cursor.rowcount
            connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_direccion(cls, direccion: Direccion):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM direcciones
                    WHERE id_direccion = %s
                """, (direccion.id_direccion,))
                affected_rows = cursor.rowcount
            connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
