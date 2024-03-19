from flask import Blueprint, request, render_template, flash, url_for, redirect
from datetime import datetime, timedelta
from alchemyClasses import db
from alchemyClasses.Rentar import Rentar
from alchemyClasses.Usuarios import Usuarios
from alchemyClasses.Peliculas import Peliculas

rentar_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@rentar_blueprint.route('/')
def ver_acciones():
    return render_template('renta.html')

@rentar_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():

    if request.method == 'GET':
        return render_template('agrega_renta.html')
    else:
        idUsuario = request.form['idUsuario']
        idPelicula = request.form['idPelicula']
        dias_de_renta = request.form['dias_de_renta']
        if idUsuario != Usuarios.query.filter(Usuarios.idUsuario == idUsuario).first().idUsuario:
            flash("ERROR: El identificador del usuario no existe!")
            return render_template('agrega_renta.html')
        elif idPelicula != Peliculas.query.filter(Peliculas.idPelicula == idPelicula).first().idPelicula:
            flash("ERROR: El identificador de la pelicula no existe!")
            return render_template('agrega_renta.html')
        if dias_de_renta == None:
            dias_de_renta = 5
        id = 1
        for registro in Rentar.query.all():
            id += 1
        renta = Rentar(id, idUsuario, idPelicula, datetime.now(), dias_de_renta, 0)
        db.session.add(renta)
        db.session.commit()
        return render_template('renta_agregada.html', idUsuario=idUsuario, idPelicula=idPelicula)

@rentar_blueprint.route('/seleccionar', methods=['GET', 'POST'])
def seleccionar_renta():
    if request.method == 'GET':
        rentas = Rentar.query.all()
        return render_template('selecciona_idRentar.html', rentas=rentas)
    else:
        id = request.form['idRentar']
        renta = Rentar.query.filter(Rentar.idRentar == id).first()
        return redirect(url_for('renta.actualizar_renta', idRentar=renta.idRentar))

@rentar_blueprint.route('/actualizar/<int:idRentar>', methods=['GET', 'POST'])
def actualizar_renta(idRentar):
    if request.method == 'GET':
        renta = Rentar.query.filter(Rentar.idRentar == idRentar).first()
        return render_template('actualiza_renta.html', renta=renta)
    else:
        renta = Rentar.query.filter(Rentar.idRentar == idRentar).first()
        estatus = renta.estatus
        if 'checkbox1' in request.form:
            estatus = 1
        elif 'checkbox1' not in request.form and 'checkbox2' not in request.form:
            estatus = 0
        db.session.delete(renta)
        renta.estatus = estatus
        db.session.add(renta)
        db.session.commit()
        return render_template('renta_actualizada.html')

@rentar_blueprint.route('/rentas')
def ver_rentas():
    rentas = Rentar.query.all()
    lista = []
    for renta in rentas:
        fecha_lim = [renta, renta.fecha_renta + timedelta(days=renta.dias_de_renta)]
        lista.append(fecha_lim)
    return render_template('ver_rentas.html', lista=lista, fecha_act=datetime.now())
    