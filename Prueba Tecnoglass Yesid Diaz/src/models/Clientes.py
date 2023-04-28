from utils.db import db

from models import Orden

class Clientes (db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50),nullable = False)
    direccion = db.Column(db.String(30),nullable = False)
    telefono = db.Column(db.String(20),nullable = False)
    nacionalidad = db.Column(db.String(30),nullable = False)
    correo = db.Column(db.String(50),nullable = False)

    orden = db.relationship('Orden', backref='clientes', lazy=True)



    def __init__(self,nombre,direccion,telefono,nacionalidad,correo) :
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.nacionalidad = nacionalidad
        self.correo = correo
    
    def getDatos(self):
        return {
            "id_cliente" : self.id_cliente,
            "nombre" : self.nombre,
            "direccion" : self.direccion,
            "telefono" : self.telefono,
            "nacionalidad" : self.nacionalidad,
            "correo" : self.correo
        }
        

