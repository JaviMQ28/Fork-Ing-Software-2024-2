from sqlalchemy import Column, Integer, String, Boolean, BLOB
from alchemyClasses import db

class Usuarios(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, nullable=False, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apPat = Column(String(200), nullable=False)
    apMat = Column(String(200))
    password = Column(String(64), nullable=False)
    email = Column(String(500), default=None, unique=True)
    profilePicture = Column(BLOB)
    superUser = Column(Boolean, default=None)

    def __init__(self, idUsuario, nombre, apPat, apMat, password, email, profilePicture, superUser):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

    def __str__(self):
        return f'Nombre del usuario: {self.nombre} {self.apPat} {self.apMat}\n - Id: {self.idUsuario}\n - Correo: {self.email}\n - Contraseña: {self.password}\n - Foto de perfil: {self.profilePicture}\n - Super usuario: {self.superUser}\n'