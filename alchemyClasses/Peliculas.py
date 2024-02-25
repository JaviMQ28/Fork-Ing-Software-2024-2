from sqlalchemy import Column, Integer, String
from alchemyClasses import db

class Peliculas(db.Model):

    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, nullable=False, primary_key=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45), default=None)
    duracion = Column(Integer, default=None)
    inventario = Column(Integer, nullable=False)

    def __init__(self, idPelicula, nombre, genero, duracion, inventario):
        self.idPelicula = idPelicula
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f'Pelicula: {self.nombre}\n - Id: {self.idPelicula}\n - Genero: {self.genero}\n - Duracion: {self.duracion}\n - Inventario: {self.inventario}\n'