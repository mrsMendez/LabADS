from flask import Blueprint, jsonify, request
import uuid # para generar en Postgres
from ..models.ProductosModels import ProductoModel
from ..models.entities.Productos import Producto

main = Blueprint('producto_blueprint', __name__)

@main.route('/', methods = ['GET'])
def getProductos():
    try:
        productos = ProductoModel.get_all_productos()
        if productos:
            return jsonify(productos), 200
        else:
            return jsonify({"message": "No se encontraron productos."}), 200
    except Exception as ex: 
        return jsonify({"error": str(ex)}), 500
    
@main.route('/<id>', methods = ['GET'])
def get_producto_by_id(id):
    try:
        producto = ProductoModel.get_productos_by_id(id)
        if producto:
            return jsonify(producto)
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
@main.route('/add', methods = ['POST'])
def add_producto():
    try:
        data = request.get_json()
        required_fields = ['nombre', 'descripcion', 'precio', 'stock']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        
        producto_id = str(uuid.uuid4())

        producto = Producto(
            id_producto=producto_id,
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion'),
            precio=data.get('precio'),
            stock=data.get('stock')
        )
        ProductoModel.add_producto(producto)

        return jsonify({"message": "Producto agregado", "id": producto_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
@main.route('/update/<id>', methods=['PUT'])
def update_producto(id):
    try:
        data = request.get_json()
        existing_producto = ProductoModel.get_productos_by_id(id)
        if not existing_producto:
            return jsonify({"error": "Producto no encontrado"}), 404
        required_fields = ['nombre', 'descripcion', 'precio', 'stock']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"})
        
        producto = Producto(
            id_producto=id,
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion'),
            precio=data.get('precio'),
            stock=data.get('stock')
        )
        affected_rows = ProductoModel.update_producto(producto)
        if affected_rows == 1:
            return jsonify({"message": "Producto actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se puede actualizar el producto"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
@main.route('/delete/<id>', methods=['DELETE'])
def delete_producto(id):
    try:
        producto = Producto(
            id_producto=id,
            nombre="",
            descripcion="",
            precio="",
            stock=""
        )
        affected_rows = ProductoModel.delete_producto(producto)
        if affected_rows == 1:
            return jsonify({"message": f"Producto {id} eliminado"}), 200
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
