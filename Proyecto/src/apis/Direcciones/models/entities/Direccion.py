from utils.DateFormat import DateFormat

class Direccion:
    def __init__(self, id_direccion, cliente_id, direccion, ciudad, pais):
        self.id_direccion = id_direccion
        self.cliente_id = cliente_id
        self.direccion = direccion
        self.ciudad = ciudad
        self.pais = pais

    def to_JSON(self):
        return {
            "id_direccion": self.id_direccion,
            "cliente_id": self.cliente_id,
            "direccion": self.direccion,
            "ciudad": self.ciudad,
            "pais": self.pais
        }
