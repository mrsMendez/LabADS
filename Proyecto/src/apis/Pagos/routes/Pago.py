#Ronal
from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime
from ..models.PagosModels import PagosModel
from ..models.entities.Pagos import Pagos

main = Blueprint('pago_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_pagos():
    try:
        pagos = PagosModel.get_all_pagos()
        if pagos:
            return jsonify(pagos), 200
        else:
            return jsonify({"message": "No se encontraron pagos"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_pago_by_id(id):
    try:
        pago = PagosModel.get_pago_by_id(id)
        if pago:
            return jsonify(pago)
        else:
            return jsonify({"error": "Pago no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
