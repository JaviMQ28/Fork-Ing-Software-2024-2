from flask import Blueprint, request, render_template, flash, url_for
from alchemyClasses import db
from alchemyClasses.Peliculas import Peliculas
from alchemyClasses.Rentar import Rentar

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/')
def ver_acciones():
    return render_template('pelicula.html')

@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():

    if request.method == 'GET':
        return render_template('agrega_pelicula.html')
    else:
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        id = 1
        for registro in Peliculas.query.all():
            id += 1
        pelicula = Peliculas(id, nombre, genero, duracion, inventario)
        db.session.add(pelicula)
        db.session.commit()
        return render_template('pelicula_agregada.html', nombre=nombre, genero=genero)

@pelicula_blueprint.route('/actualizar', methods=['GET', 'POST'])
def actualizar_pelicula():
    if request.method == 'GET':
        return render_template('actualiza_pelicula.html')
    else:
        idPelicula = request.form['idPelicula']
        opciones = request.form['opciones']
        opcion = request.form['opcion']
        pelicula = Peliculas.query.filter(Peliculas.idPelicula == idPelicula).first()
        if pelicula == None :
            flash("ERROR: Pelicula no encontrada")
            return render_template('actualiza_pelicula.html')
        db.session.delete(pelicula)
        if opciones == 'opcion1':
            if len(opcion) <= 200:
                pelicula.nombre = opcion
            else:
                flash("ERROR: Pon un nombre válido!")
                return render_template('actualiza_pelicula.html')
        elif opciones == 'opcion2':
            if len(opcion) <= 45:
                pelicula.genero = opcion
            else:
                flash("ERROR: Pon un nombre válido!")
                return render_template('actualiza_pelicula.html')
        elif opciones == 'opcion3':
            try:
                pelicula.duracion = int(opcion)
            except ValueError:
                flash("ERROR: Pon un número!")
                return render_template('actualiza_pelicula.html')
        elif opciones == 'opcion4':
            try:
                pelicula.inventario = int(opcion)
            except ValueError:
                flash("ERROR: Pon un número!")
                return render_template('actualiza_pelicula.html')
        db.session.add(pelicula)
        db.session.commit()
        return render_template('pelicula_actualizada.html', nombre=pelicula.nombre)

def actualizar_ids():
    id = 1
    for registro in Peliculas.query.all():
        registro.idPelicula = id
        db.session.commit()
        id += 1

@pelicula_blueprint.route('/eliminar', methods=['GET', 'POST'])
def eliminar_pelicula():
    if request.method == 'GET':
        return render_template('elimina_pelicula.html')
    else:
        nombre = request.form['nombre']
        pelicula = Peliculas.query.filter(Peliculas.nombre == nombre).first()
        if pelicula == None :
            flash("ERROR: Pelicula no encontrado")
            return render_template('elimina_pelicula.html')
        elif pelicula.idUsuario == Rentar.query.filter(Rentar.idPelicula == pelicula.idPelicula).first().idPelicula:
            flash("ERROR: La película no puede ser eliminada, un usuario la rento")
            return render_template('elimina_pelicula.html')
        db.session.delete(pelicula)
        db.session.commit()
        actualizar_ids()
        return render_template('pelicula_eliminada.html', nombre=nombre)

@pelicula_blueprint.route('/peliculas')
def ver_peliculas():
    peliculas = Peliculas.query.all()
    return render_template('ver_peliculas.html', peliculas=peliculas)
