from flask import Blueprint
from controllers import OrdenController

orden = Blueprint('orden',__name__)


@orden.route('/agregar_orden/<id_cliente>', methods=['POST'])
def agregar_orden(id_cliente):
    return OrdenController.agregar_orden(id_cliente)

@orden.route('/gestionar_orden/<nro_orden>', methods=['PUT'])
def gestionar_orden(nro_orden):
    return OrdenController.gestionar_orden(nro_orden)