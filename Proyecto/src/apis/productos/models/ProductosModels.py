from database.database import get_connection
from ..models.entities.Productos import Producto

class ProductoModel:

    @classmethod
    def get_all_productos(cls):
        try:
            connection = get_connection()
            productos_list = []
            with connection.cursor() as cursor:

                cursor.execute("""
                    SELECT id_producto, nombre, descripcion, precio, stock
                    FROM Productos
                    ORDER BY nombre ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    producto = Producto(
                        id_producto=row[0],
                        nombre=row[1],
                        descripcion=row[2],
                        precio=row[3],
                        stock=row[4]
                    )
                    productos_list.append(producto.to_Json())
                connection.close()
                return productos_list
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_productos_by_id(cls, producto_id):
        try:
            connection = get_connection()
            producto_json = None
            with connection.cursor() as cursor:
                cursor.execute(""" 
                    SELECT id_producto, nombre, descripcion, precio, stock
                    FROM Productos
                    WHERE id_producto = %s""", (producto_id))
                row = cursor.fetchone()
                if row is not None:
                    producto = Producto(
                        id_producto=row[0],
                        nombre=row[1],
                        descripcion=row[2],
                        precio=row[3],
                        stock=row[4]
                    ) 
                    producto_json = producto.to_Json()
            connection.close()
            return producto_json
        except Exception as ex:
            raise Exception(ex)  
    
    @classmethod
    def add_producto(cls, producto: Producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                INSERT INTO Productos
                (id_producto, nombre, descripcion, precio, stock)
                VALUES(%s, %s, %s, %s, %s)""",
                (
                    producto.id_producto,
                    producto.nombre,
                    producto.descripcion,
                    producto.precio,
                    producto.stock
                )
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_producto(cls, producto: Producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE Productos 
                    SET id_producto = %s, nombre = %s, descripcion = %s, precio = %s, stock = %s
                    WHERE id_producto = %s """,
                    (
                        producto.nombre,
                        producto.descripcion,
                        producto.precio,
                        producto.stock
                    )
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_producto(cls, producto: Producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM Productos 
                    WHERE id_producto = %s
                    """, 
                    (producto.id_producto)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)