from utils.DateFormat import DateFormat

class Cliente:
    def __init__(self, id_cliente, nombre, email, fecha_registro):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.fecha_registro = DateFormat.convert_date(fecha_registro)
        pass

    def to_Json(self):
        return{
            "id_cliente": self.id_cliente,
            "Nombre": self.nombre,
            "Email": self.email,
            "Fecha de ingreso": self.fecha_registro
        }