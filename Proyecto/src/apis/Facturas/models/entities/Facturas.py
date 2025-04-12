from utils.DateFormat import DateFormat

class Factura:
    def __init__(self, id_factura, compra_id, fecha, total):
        self.id_factura = id_factura
        self.compra_id = compra_id
        self.fecha = fecha
        self.total = total

    def to_JSON(self):
        return {
            "id_factura": self.id_factura,
            "compra_id": self.compra_id,
            "fecha": self.fecha,
            "total": self.total
        }
