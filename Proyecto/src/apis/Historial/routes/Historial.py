#Ronal
from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime
from ..models.HistorialModels import HistorialModel
from ..models.entities.Historial import Historial

main = Blueprint('historial_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_historial():
    try:
        historial = HistorialModel.get_all_historial()
        if historial:
            return jsonify(historial), 200
        else:
            return jsonify({"message": "No se encontró historial"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_historial_by_id(id):
    try:
        registro = HistorialModel.get_historial_by_id(id)
        if registro:
            return jsonify(registro)
        else:
            return jsonify({"error": "Historial no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
