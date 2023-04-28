from flask import jsonify, request
from models.Detalleorden import *
from models.Orden import Orden

def agregar_detalles(nro_orden):
    try:
        orden = Orden.query.get(nro_orden)
        if not orden:
            return jsonify({'message': 'La orden no existe' , "status" : 404}), 404
        else:
            largo_vidrio = request.json['largo_vidrio']
            ancho_vidrio = request.json['ancho_vidrio']

            new_detalleorden = Detalleorden(nro_orden,largo_vidrio,ancho_vidrio)
            db.session.add(new_detalleorden)
            db.session.commit()
            return jsonify({'message': 'Detalle de orden creada correctamente', "status" : 200}), 200
    
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})


