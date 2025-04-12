#Julio
from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime
from ..models.ComprasModels import ComprasModel
from ..models.entities.Compras import Compras

main = Blueprint('compra_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_compras():
    try:
        compras = ComprasModel.get_all_compras()
        if compras:
            return jsonify(compras), 200
        else:
            return jsonify({"message": "No se encontraron compras"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_compra_by_id(id):
    try:
        compra = ComprasModel.get_compra_by_id(id)
        if compra:
            return jsonify(compra)
        else:
            return jsonify({"error": "Compra no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_compra():
    try:
        data = request.get_json()
        required_fields = ['cliente_id', 'fecha', 'total']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        compra_id = str(uuid.uuid4())
        fecha_compra = datetime.strptime(data.get('fecha'), '%d/%m/%Y')

        compra = Compras(
            id_compra=compra_id,
            cliente_id=data.get('cliente_id'),
            fecha=fecha_compra,
            total=data.get('total')
        )

        ComprasModel.add_compra(compra)

        return jsonify({"message": "Compra agregada", "id": compra_id}), 201

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_compra(id):
    try:
        data = request.get_json()
        existing_compra = ComprasModel.get_compra_by_id(id)
        if not existing_compra:
            return jsonify({"error": "Compra no encontrada"}), 404

        required_fields = ['cliente_id', 'fecha', 'total']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        fecha_compra = datetime.strptime(data.get('fecha'), '%d/%m/%Y')

        compra = Compras(
            id_compra=id,
            cliente_id=data.get('cliente_id'),
            fecha=fecha_compra,
            total=data.get('total')
        )

        affected_rows = ComprasModel.update_compra(compra)

        if affected_rows == 1:
            return jsonify({"message": "Compra actualizada correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar la compra"}), 400

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_compra(id):
    try:
        compra = Compras(
            id_compra=id,
            cliente_id="",
            fecha=datetime.now(),
            total=0
        )

        affected_rows = ComprasModel.delete_compra(compra)
        if affected_rows == 1:
            return jsonify({"message": f"Compra {id} eliminada"}), 200
        else:
            return jsonify({"error": "Compra no encontrada"}), 404

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
