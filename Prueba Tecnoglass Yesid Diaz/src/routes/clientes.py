from flask import Blueprint
from controllers import ClienteController

cliente = Blueprint('cliente',__name__)

@cliente.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    return ClienteController.agregar_cliente()


@cliente.route('/listar_clientes', methods=['GET'])
def listar_clientes():
    return ClienteController.listar_clientes()


@cliente.route('/editar_cliente/<id_cliente>', methods=['PUT'])
def editar_cliente(id_cliente):
    return ClienteController.editar_cliente(id_cliente)


@cliente.route('/eliminar_cliente/<id_cliente>', methods=['DELETE'])
def eliminar_cliente(id_cliente):
    return ClienteController.eliminar_cliente(id_cliente)


