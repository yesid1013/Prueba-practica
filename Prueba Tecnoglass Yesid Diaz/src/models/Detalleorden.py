from utils.db import db
from models import *

class Detalleorden(db.Model):
    __tablename__ = 'detalleorden'
    consecutivo_item = db.Column(db.Integer, primary_key = True)
    nro_orden = db.Column(db.Integer, db.ForeignKey('orden.nro_orden'), nullable=False)
    largo_vidrio = db.Column(db.Float,nullable=False)
    ancho_vidrio = db.Column(db.Float,nullable=False)

    def __init__(self,nro_orden,largo_vidrio,ancho_vidrio) :
        self.nro_orden = nro_orden
        self.largo_vidrio = largo_vidrio
        self.ancho_vidrio = ancho_vidrio
        


