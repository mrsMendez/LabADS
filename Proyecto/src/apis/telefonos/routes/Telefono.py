from flask import Blueprint, jsonify, request
import uuid
from ..models.TelefonosModels import TelefonoModel
from ..models.entities.Telefonos import Telefono

main = Blueprint('telefono_blueprint', __name__)

@main.route('/', methods = ['GET'])
def getTelefonos():
    try:
        telefonos = TelefonoModel.get_all_telefonos()
        if telefonos:
            return jsonify(telefonos), 200
        else:
            return jsonify({"message": "No se encontraron telefonos"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
@main.route('/<id>', methods = ['GET'])
def get_telefono_by_id(id):
    try:
        telefono : TelefonoModel.get_telefono_by_id
        if telefono:
            return jsonify(telefono)
        else:
            return jsonify({"error":"Telefono no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods = ['POST'])
def add_telefono():
    try:
        data = request.get_json()
        required_fields = ['cliente_id', 'numero']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        telefono_id = str(uuid.uuid4())

        telefono = Telefono(
            id_telefono = telefono_id,
            cliente_id=data.get('cliente_id'),
            numero=data.get('numero')
        )
        TelefonoModel.add_telefono(telefono)
        return jsonify({"message": "Telefono agregado con exito", "id": telefono_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_telefono(id):
    try:
        data = request.get_json()
        existing_telefono = TelefonoModel.get_telefono_by_id(id)
        if not existing_telefono:
            return jsonify({"error": "Telefono no encontrado"}), 404
        required_fields = ['cliente_id', 'numero']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"})
        

        telefono = Telefono(
            id_telefono = id,
            cliente_id=data.get('cliente_id'),
            numero=data.get('numero')
        )
        affected_rows = TelefonoModel.update_telefono(telefono)
        if affected_rows == 1:
            return jsonify({"message": "Telefono actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se puede actualizar el telefono"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    

@main.route('/delete/<id>', methods=['DELETE'])
def delete_telefono(id):
    try:
        telefono = Telefono(
            id_telefono = id,
            cliente_id = "" ,
            numero= ""
        )
        affected_rows = TelefonoModel.delete_telefono(telefono)
        if affected_rows == 1:
            return jsonify({"message": f"Telefono {id} eliminado"}), 200
        else:
            return jsonify({"error": "Telefono no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500