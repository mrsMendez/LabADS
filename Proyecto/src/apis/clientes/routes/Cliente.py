from flask import Blueprint, jsonify, request
import uuid # para generar en Postgres
from ..models.ClientesModels import ClienteModel
from ..models.entities.Clientes import Cliente
from datetime import datetime

main = Blueprint('cliente_blueprint', __name__)

@main.route('/', methods = ['GET'])
def getClientes():
    try:
        clientes = ClienteModel.get_all_clientes()
        if clientes:
            return jsonify(clientes), 200
        else:
            return jsonify({"message": "No se encontraron clientes."}), 200
    except Exception as ex: 
        return jsonify({"error": str(ex)}), 500
    
@main.route('/<id>', methods = ['GET'])
def get_cliente_by_id(id):
    try:
        cliente = ClienteModel.get_clientes_by_id(id)
        if cliente:
            return jsonify(cliente)
        else:
            return jsonify({"error": "Cliente no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
@main.route('/add', methods = ['POST'])
def add_cliente():
    try:
        data = request.get_json()
        required_fields = ['nombre', 'email', 'fecha_ingreso']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        
        cliente_id = str(uuid.uuid4())

        fecha_regis_str = data.get('fecha_registro', datetime.now().strftime('%d/%m/%Y'))
        fecha_regis_obj = datetime.strptime(fecha_regis_str, '%d/%m/%Y')

        cliente = Cliente(
            id_cliente=cliente_id,
            nombre=data.get('nombre'),
            email=data.get('email'),
            fecha_registro= fecha_regis_obj
        )
        ClienteModel.add_cliente(cliente)

        return jsonify({"message": "Cliente agregado", "id": cliente_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
@main.route('/update/<id>', methods=['PUT'])
def update_cliente(id):
    try:
        data = request.get_json()
        existing_cliente = ClienteModel.get_clientes_by_id(id)
        if not existing_cliente:
            return jsonify({"error": "Cliente no encontrado"}), 404
        required_fields = ['nombre', 'email', 'fecha_ingreso']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"})
        fecha_regis_str = data.get('fecha_registro')
        fecha_regis_obj = datetime.strptime(fecha_regis_str, '%d/%m/%Y')
        cliente = Cliente(
            id_cliente=id,
            nombre=data.get('nombre'),
            email=data.get('email'),
            fecha_registro= fecha_regis_obj
        )
        affected_rows = ClienteModel.update_cliente(cliente)
        if affected_rows == 1:
            return jsonify({"message": "Cliente actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se puede actualizar el cliente"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    

@main.route('/delete/<id>', methods=['DELETE'])
def delete_cliente(id):
    try:
        cliente = Cliente(
            id_cliente=id,
            nombre="",
            email="",
            fecha_registro=datetime.now()
        )
        affected_rows = ClienteModel.delete_cliente(cliente)
        if affected_rows == 1:
            return jsonify({"message": f"Cliente {id} eliminado"}), 200
        else:
            return jsonify({"error": "Cliente no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
