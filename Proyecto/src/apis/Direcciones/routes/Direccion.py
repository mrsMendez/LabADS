#Ronal
from flask import Blueprint, jsonify, request
import uuid
from ..models.DireccionesModels import DireccionesModel
from ..models.entities.Direccion import Direccion
from datetime import datetime

main = Blueprint('direccion_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_direcciones():
    try:
        direcciones = DireccionesModel.get_all_direcciones()
        if direcciones:
            return jsonify(direcciones), 200
        else:
            return jsonify({"message": "No se encontraron direcciones"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_direccion_by_id(id):
    try:
        direccion = DireccionesModel.get_direccion_by_id(id)
        if direccion:
            return jsonify(direccion)
        else:
            return jsonify({"error": "Dirección no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_direccion():
    try:
        data = request.get_json()
        required_fields = ['cliente_id', 'direccion', 'ciudad', 'pais']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        direccion_id = str(uuid.uuid4())

        direccion = Direccion(
            id_direccion=direccion_id,
            cliente_id=data.get('cliente_id'),
            direccion=data.get('direccion'),
            ciudad=data.get('ciudad'),
            pais=data.get('pais')
        )

        DireccionesModel.add_direccion(direccion)

        return jsonify({"message": "Dirección agregada", "id": direccion_id}), 201

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_direccion(id):
    try:
        data = request.get_json()
        existing_direccion = DireccionesModel.get_direccion_by_id(id)
        if not existing_direccion:
            return jsonify({"error": "Dirección no encontrada"}), 404

        required_fields = ['cliente_id', 'direccion', 'ciudad', 'pais']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        direccion = Direccion(
            id_direccion=id,
            cliente_id=data.get('cliente_id'),
            direccion=data.get('direccion'),
            ciudad=data.get('ciudad'),
            pais=data.get('pais')
        )

        affected_rows = DireccionesModel.update_direccion(direccion)

        if affected_rows == 1:
            return jsonify({"message": "Dirección actualizada correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar la dirección"}), 400

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_direccion(id):
    try:
        direccion = Direccion(
            id_direccion=id,
            cliente_id="",
            direccion="",
            ciudad="",
            pais=""
        )

        affected_rows = DireccionesModel.delete_direccion(direccion)
        if affected_rows == 1:
            return jsonify({"message": f"Dirección {id} eliminada"}), 200
        else:
            return jsonify({"error": "Dirección no encontrada"}), 404

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
