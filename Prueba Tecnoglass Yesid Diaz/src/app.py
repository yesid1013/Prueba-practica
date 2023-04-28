from flask import Flask,jsonify
from utils.db import db
from routes.clientes import cliente 
from routes.ordenes import orden
from routes.detalle_orden import detalleOrden


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tecnoglass'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(cliente)
app.register_blueprint(orden)
app.register_blueprint(detalleOrden)





def pagina_no_encontrada(error):
    return jsonify({"message" : "Pagina no encontrada"})



if __name__=="__main__":
    app.register_error_handler(404 , pagina_no_encontrada)
    app.run(port=5000, debug=True)

