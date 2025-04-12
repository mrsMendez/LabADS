from utils.DateFormat import DateFormat

class Pago:
    def __init__(self, id_pago, factura_id, monto, metodo_pago, fecha):
        self.id_pago = id_pago
        self.factura_id = factura_id
        self.monto = monto
        self.metodo_pago = metodo_pago
        self.fecha = fecha

    def to_JSON(self):
        return {
            "id_pago": self.id_pago,
            "factura_id": self.factura_id,
            "monto": self.monto,
            "metodo_pago": self.metodo_pago,
            "fecha": self.fecha
        }
