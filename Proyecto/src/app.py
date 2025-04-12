from flask import Flask
from flask_cors import CORS
from config.config import app_config

from apis.Compras.routes import Compra
from apis.Productos.routes import Producto
from apis.Facturas.routes import Factura
from apis.Pagos.routes import Pago
from apis.Descuentos.routes import Descuento
from apis.Historial.routes import Historial

app = Flask(__name__)

CORS(app)

def paginaNoEncontrada(error):
    return "<h1> Pagina no encrotada</h1>", 404

def errorServidor(error):
    return "<h1>Error interno del servidor</h1>", 500

@app.route('/')
def principal():
    return "<h1>Bienvenido a mi apliación con Flask</h1>"

if __name__ == '__main__':
    app.config.from_object(app_config['development'])

    app.register_error_handler(404, paginaNoEncontrada)
    app.register_error_handler(500, errorServidor)

    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    app.config.from_object(app_config['development'])
    app.register_blueprint(Compra.main, url_prefix = "/api/Compra")
    app.register_blueprint(Producto.main, url_prefix="/api/productos")
    app.register_blueprint(Factura, url_prefix="/api/facturas")
    app.register_blueprint(Pago, url_prefix="/api/pagos")
    app.register_blueprint(Descuento, url_prefix="/api/descuentos")
    app.register_blueprint(Historial, url_prefix="/api/historial")