from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from alchemyClasses import db

class Rentar(db.Model):

    __tablename__ = 'rentar'
    idRentar = Column(Integer, nullable=False, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Boolean, default=0)

    def __init__(self, idRentar, idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus):
        self.idRentar = idRentar
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return f'Renta: {self.idRentar}\n - Id del usuario: {self.idUsuario}\n - Id de la pelicula: {self.idPelicula}\n - Fecha: {self.fecha_renta}\n - Dias de renta: {self.dias_de_renta}\n - Estatus: {self.estatus}\n'