from database.database import get_connection
from ..models.entities.Clientes import Cliente

class ClienteModel:
    
    @classmethod
    def get_all_clientes(cls):
        try:
            connection = get_connection()
            clientes_list = []
            with connection.cursor() as cursor:

                cursor.execute("""
                    SELECT id_cliente, nombre, email, fecha_ingreso
                    FROM Clientes
                    ORDER BY nombre ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    cliente = Cliente(
                        id_cliente=row[0],
                        nombre=row[1],
                        email=row[2],
                        fecha_registro=row[3]
                    )
                    clientes_list.append(cliente.to_Json())
            connection.close()
            return clientes_list
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_clientes_by_id(cls, cliente_id):
        try:
            connection = get_connection()
            cliente_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_cliente, nombre, email, fecha_ingreso
                    FROM Clientes
                    WHERE id_cliente = %s""", (cliente_id))
                row = cursor.fetchone()
                if row is not None:
                    cliente = Cliente(
                        id_cliente=row[0],
                        nombre=row[1],
                        email=row[2],
                        fecha_registro=row[3]
                    )
                    cliente_json = cliente.to_Json()
            connection.close()
            return cliente_json
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_cliente(cls, cliente: Cliente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                INSERT INTO Clientes
                (id_cliente, nombre, email, fecha_ingreso)
                VALUES(%s, %s, %s, %s)""",
                (
                    cliente.id_cliente,
                    cliente.nombre,
                    cliente.email,
                    cliente.fecha_registro
                )
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_cliente(cls, cliente: Cliente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE Clientes
                    SET nombre = %s, email = %s, fecha_registro = %s
                    WHERE id_cliente = %s """,
                    (
                        cliente.nombre,
                        cliente.email,
                        cliente.fecha_registro
                    )
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_cliente(cls, cliente: Cliente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM Clientes 
                    WHERE id_cliente = %s
                    """, 
                    (cliente.id_cliente)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    