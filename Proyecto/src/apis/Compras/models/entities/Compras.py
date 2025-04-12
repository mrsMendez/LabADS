from utils.DateFormat import DateFormat

class Compra:
    def __init__(self, id_compra, cliente_id, fecha, total):
        self.id_compra = id_compra
        self.cliente_id = cliente_id
        self.fecha = fecha
        self.total = total

    def to_JSON(self):
        return {
            "id_compra": self.id_compra,
            "cliente_id": self.cliente_id,
            "fecha": self.fecha,
            "total": self.total
        }
