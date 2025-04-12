#Julio
from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime
from ..models.FacturasModels import FacturasModel
from ..models.entities.Facturas import Facturas

main = Blueprint('factura_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_facturas():
    try:
        facturas = FacturasModel.get_all_facturas()
        if facturas:
            return jsonify(facturas), 200
        else:
            return jsonify({"message": "No se encontraron facturas"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_factura_by_id(id):
    try:
        factura = FacturasModel.get_factura_by_id(id)
        if factura:
            return jsonify(factura)
        else:
            return jsonify({"error": "Factura no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
