#Julio
from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime
from ..models.DescuentosModels import DescuentosModel
from ..models.entities.Descuentos import Descuentos

main = Blueprint('descuento_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_descuentos():
    try:
        descuentos = DescuentosModel.get_all_descuentos()
        if descuentos:
            return jsonify(descuentos), 200
        else:
            return jsonify({"message": "No se encontraron descuentos"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_descuento_by_id(id):
    try:
        descuento = DescuentosModel.get_descuento_by_id(id)
        if descuento:
            return jsonify(descuento)
        else:
            return jsonify({"error": "Descuento no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
