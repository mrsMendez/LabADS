from database.database import get_connection
from ..models.entities.Productos import Producto

class ProductosModel:

    @classmethod
    def get_all_producto(cls):
        try:
            connection = get_connection()
            productos_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_producto, nombre, descripcion, precio, stock
                    FROM productos ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    producto = Producto(
                        id_producto=row[0],
                        nombre=row[1],
                        descripcion=row[2],
                        precio=float(row[3]),
                        stock=row[4]
                    )
                    productos_list.append(producto.to_JSON())
            connection.close()
            return productos_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_producto_by_id(cls, id):
        try:
            connection = get_connection()
            producto_data = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_producto, nombre, descripcion, precio, stock
                    FROM productos
                    WHERE id_producto = %s
                """, (id,))
                row = cursor.fetchone()
                if row is not None:
                    producto = Producto(
                        id_producto=row[0],
                        nombre=row[1],
                        descripcion=row[2],
                        precio=float(row[3]),
                        stock=row[4]
                    )
                    producto_data = producto.to_JSON()
            connection.close()
            return producto_data
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_producto(cls, producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO productos (nombre, descripcion, precio, stock)
                    VALUES (%s, %s, %s, %s)
                """, (producto.nombre, producto.descripcion, producto.precio, producto.stock))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_producto(cls, id, producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE productos
                    SET nombre = %s, descripcion = %s, precio = %s, stock = %s
                    WHERE id_producto = %s
                """, (producto.nombre, producto.descripcion, producto.precio, producto.stock, id))
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_productos(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM productos WHERE id_producto = %s", id,)
                connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)