from database.database import get_connection
from ..models.entities.Telefonos import Telefono

class TelefonoModel:

    @classmethod
    def get_all_telefonos(cls):
        try:
            connection = get_connection()
            telefono_list = []
            with connection.cursor() as cursor:

                cursor.execute("""
                    SELECT id_telefono, cliente_id, numero
                    FROM Telefonos 
                    ORDER BY numero ASC
                               """)
                resultset = cursor.fetchall()
                for row in resultset:
                    telefono = Telefono(
                        id_telefono=row[0],
                        cliente_id=row[1],
                        numero=row[2]
                    )
                    telefono_list.append(telefono.to_Json())
                connection.close()
                return telefono_list
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def get_telefono_by_id(cls, telefono_id):
        try:
            connection = get_connection()
            telefono_json = None 
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_telefono, cliente_id, numero
                    FROM Telefonos
                    WHERE id_telefono = %s""", (telefono_id))
                row = cursor.fetchone()
                if row is not None:
                    telefono = Telefono(
                        id_telefono=row[0],
                        cliente_id=row[1],
                        numero=row[2]
                    )
                    telefono_json = telefono.to_Json()
                connection.close()
                return telefono_json
        except Exception as ex:
            raise Exception(ex)
            

    @classmethod
    def add_telefono(cls, telefono: Telefono):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                INSERT INTO Telefonos
                (id_telefono, cliente_id, numero)
                VALUES(%s, %s, %s)""",
                (
                    telefono.id_telefono,
                    telefono.cliente_id,
                    telefono.numero
                )
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_telefono(cls, telefono: Telefono):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE Telefonos
                    SET cliente_id = %s, numero = %s
                    WHERE id_telefono = %s """,
                    (
                        telefono.cliente_id,
                        telefono.numero
                    )
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_telefono(cls, telefono: Telefono):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM Telefonos 
                    WHERE id_telefono = %s """,
                    (telefono.id_telefono)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)