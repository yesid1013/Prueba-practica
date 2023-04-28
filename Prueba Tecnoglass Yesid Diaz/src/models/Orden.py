from utils.db import db
from models import *


class Orden (db.Model):
    __tablename__ = 'orden'
    nro_orden = db.Column(db.Integer, primary_key = True)
    cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    fecha_orden = db.Column(db.Date,nullable = False)
    estado = db.Column(db.Enum('solicitada','aprobada','anulada'), nullable = False,name='estado')

    detalleorden = db.relationship('Detalleorden', backref='orden', lazy=True)

    def __init__(self,cliente,fecha_orden,estado) :
        self.cliente = cliente
        self.fecha_orden = fecha_orden
        self.estado = estado

    

    def getDatos(self):
        return {
            "nro_orden" : self.nro_orden,
            "cliente" : self.cliente,
            "fecha_orden" : self.fecha_orden,
            "estado" : self.estado
        }
        

          
