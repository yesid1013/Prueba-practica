from flask import Blueprint
from controllers import DetalleOrdenController

detalleOrden = Blueprint('detalleOrden',__name__)

@detalleOrden.route('/agregar_detalle_orden/<nro_orden>', methods=['POST'])
def agregar_detalle_orden(nro_orden):
    return DetalleOrdenController.agregar_detalles(nro_orden)
