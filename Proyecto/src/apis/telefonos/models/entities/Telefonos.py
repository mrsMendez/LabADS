class Telefono:
    def __init__(self, id_telefono, cliente_id, numero):
        self.id_telefono = id_telefono
        self.cliente_id = cliente_id
        self.numero = numero
        pass
    def to_Json(self):
        return{
            "id_telefono": self.id_telefono,
            "cliente_id": self.cliente_id,
            "numero": self.numero
        }