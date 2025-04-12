from utils.DateFormat import DateFormat

class Descuento:
    def __init__(self, id_descuento, producto_id, porcentaje, fecha_inicio, fecha_fin):
        self.id_descuento = id_descuento
        self.producto_id = producto_id
        self.porcentaje = porcentaje
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def to_JSON(self):
        return {
            "id_descuento": self.id_descuento,
            "producto_id": self.producto_id,
            "porcentaje": self.porcentaje,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin
        }
