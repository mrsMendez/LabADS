from flask import Flask
from flask_cors import CORS
from config.config import app_config

from apis.clientes.routes import Cliente
from apis.telefonos.routes import Telefono
from apis.productos.routes import Producto

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

    app.register_blueprint(Cliente.main, url_prefix = "/api/clientes")

    app.register_blueprint(Telefono.main, url_prefix = "/api/telefonos")

    app.register_blueprint(Producto.main, url_prefix = "/api/productos")
    
    app.register_error_handler(404, paginaNoEncontrada)
    app.register_error_handler(500, errorServidor)

    app.run(host='0.0.0.0', port=5000, debug=True)


   

    

    

