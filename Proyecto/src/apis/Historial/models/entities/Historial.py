from utils.DateFormat import DateFormat

class Historial:
    def __init__(self, id_historial, cliente_id, producto_id, fecha, cantidad, precio_unitario):
        self.id_historial = id_historial
        self.cliente_id = cliente_id
        self.producto_id = producto_id
        self.fecha = fecha
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def to_JSON(self):
        return {
            "id_historial": self.id_historial,
            "cliente_id": self.cliente_id,
            "producto_id": self.producto_id,
            "fecha": self.fecha,
            "cantidad": self.cantidad,
            "precio_unitario": self.precio_unitario
        }

