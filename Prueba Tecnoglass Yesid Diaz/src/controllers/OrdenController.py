from flask import jsonify, request
from models.Orden import *
from utils.estado import EstadoOrden
from datetime import datetime


def agregar_orden(id_cliente):
    try:
        orden = Orden.query.filter_by(cliente=id_cliente).first()
        if not orden :
            fecha_orden = request.json['fecha_orden']
            estado = request.json['estado']
            estado_str = EstadoOrden(estado).name

            formato = "%Y-%m-%d"


            try:
                datetime.strptime(fecha_orden, formato)
            except ValueError:
                return jsonify({"message" : "fecha invalida", "status" : 400}), 400


            if EstadoOrden(estado) is not None:
                new_orden = Orden(id_cliente,fecha_orden,estado_str)
                db.session.add(new_orden)
                db.session.commit()
                return jsonify({"message" : "Orden creada correctamente","status" : 200})
        else:
            return jsonify({"message" : "El cliente ya tiene una orden","status" : 400}),400
            
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

def gestionar_orden(nro_orden):
    try: 
        orden = Orden.query.get(nro_orden)
        if not orden:
            return jsonify({'message': 'La orden no existe'}), 404
        else:
            estado = request.json['estado']
            if estado != 2 or estado!= 3:
                return jsonify({"message" : "Por favor verifique que quiera ingresar un estado de aprobado o anulado" ,"status" : 400}), 400
            
            estado_str = EstadoOrden(estado).name

            orden.estado = estado_str
            db.session.commit()
            return jsonify({"message" : "Orden "+estado_str, "status" : 200})

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
    


