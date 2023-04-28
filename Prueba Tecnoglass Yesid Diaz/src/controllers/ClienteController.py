from flask import jsonify, request
from models.Clientes import *

def agregar_cliente():
    try:
        nombre = request.json['nombre']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        nacionalidad = request.json['nacionalidad']
        correo = request.json ['correo']

        new_cliente = Clientes(nombre,direccion,telefono,nacionalidad,correo)
        db.session.add(new_cliente)
        db.session.commit()

        return jsonify({"message": "Cliente creado correctamente ", "status" : 200})
    
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

def listar_clientes():
    try:
        clientes = Clientes.query.all()
        if not clientes:
            return jsonify({'message': 'No hay clientes'}), 404
        else:
            toclientes = [cliente.getDatos() for cliente in clientes]
            return jsonify(toclientes)
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

def editar_cliente(id_cliente):
    try:
        cliente = Clientes.query.get(id_cliente)
        if not cliente:
            return jsonify({'message': 'El cliente no existe'}), 404
        else:
            cliente.nombre = request.json['nombre']
            cliente.direccion = request.json['direccion']
            cliente.telefono = request.json['telefono']
            cliente.nacionalidad = request.json['nacionalidad']
            cliente.correo = request.json['correo']

            db.session.commit()

            return jsonify({"message" : "Cliente actualizado"}) , 200

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : + str(e)} )

def eliminar_cliente(id_cliente):
    try:
        cliente = Clientes.query.get(id_cliente)
        if not cliente:
            return jsonify({'message': 'El cliente no existe'}), 404
        else:
            db.session.delete(cliente)
            db.session.commit()
            return jsonify({'message': 'Cliente eliminado'}), 200
    
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : + str(e)} )
