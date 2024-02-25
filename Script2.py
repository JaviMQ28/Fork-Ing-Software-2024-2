import sqlalchemy.exc
from flask import Flask
from sqlalchemy import and_, or_
from sqlalchemy.exc import IntegrityError

from alchemyClasses import db
from alchemyClasses.Usuarios import Usuarios
from alchemyClasses.Peliculas import Peliculas
from alchemyClasses.Rentar import Rentar
from datetime import datetime

def ver_registros(tabla):
    print(f"Registros de la tabla {tabla}:\n")
    if tabla == 'usuarios':
        for registro in Usuarios.query.all():
            print(registro)
    elif tabla == 'peliculas':
        for registro in Peliculas.query.all():
            print(registro)
    elif tabla == 'rentar':
        for registro in Rentar.query.all():
            print(registro)


def filtrar_registros(tabla,id):
    print(f"Registros de la tabla {tabla}, con el identificador {id}:\n")
    id_encontrado = False
    if tabla == 'usuarios':
        for registro in Usuarios.query.filter(Usuarios.idUsuario == id):
            print(registro)
            id_encontrado = True
    elif tabla == 'peliculas':
        for registro in Peliculas.query.filter(Peliculas.idPelicula == id):
            print(registro)
            id_encontrado = True
    elif tabla == 'rentar':
        for registro in Rentar.query.filter(Rentar.idRentar == id):
            print(registro)
            id_encontrado = True
    if not(id_encontrado):
        print(f"-- No se encontraron registros con el identificador {id} en la tabla {tabla} --\n")


def actualizar_registro(tabla):
    if tabla == 'usuarios':
        col_seleccionada = False
        while not (col_seleccionada):
            columna = input(f"Dame la columna que quieres actualizar: ")
            if columna == 'nombre' or columna == 'apPat' or columna == 'apMat' or columna == 'password' or columna == 'email' or columna == 'profilePicture' or columna == 'superUser':
                col_seleccionada = True
            elif columna == 'idUsuario':
                print(
                    f"ERROR: No se puede actualizar el identificador, pon alguna de estas opciones: \n - nombre \n - apPat \n - apMat\n - password\n - email\n - profilePicture\n - superUser")
                columna = ""
            else:
                print(f"ERROR: Columna no valida, pon alguna de estas opciones: \n - nombre \n - apPat \n - apMat\n - password\n - email\n - profilePicture\n - superUser")
                columna = ""
        id_seleccionado = False
        while not(id_seleccionado):
            try:
                id = int(input(f"Dame el identificador del registro al que actualizaras su columna: "))
                cantidad = 0
                for registro in Usuarios.query.all():
                    cantidad = cantidad + 1
                if id <= cantidad and id > 0:
                    id_seleccionado = True
                else:
                    print(f"ERROR: No existe algun registro con el identificador {id}, escoge un entero de este rango (1 - {cantidad})\n")
                    id = 0
            except:
                print(f"ERROR: Identificador no valido, intentalo nuevamente\n")
                id = 0
        act = input(f"Dame el valor por la que se quiera actualizar la columna {columna} en el registro con id {id}: ")
        usuario = Usuarios.query.filter(Usuarios.idUsuario == id).first()
        if columna == 'nombre':
            usuario.nombre = act
        elif columna == 'apPat':
            usuario.apPat = act
        elif columna == 'apMat':
            usuario.apMat = act
        elif columna == 'password':
            usuario.password = act
        elif columna == 'email':
            usuario.email = act
        elif columna == 'profilePicture':
            usuario.profilePicture = act
        elif columna == 'superUser':
            usuario.superUser = act
        print("Actualización con exito!")
        db.session.commit()
    elif tabla == 'peliculas':
        col_seleccionada = False
        while not (col_seleccionada):
            columna = input(f"Dame la columna que quieres actualizar: ")
            if columna == 'nombre' or columna == 'genero' or columna == 'duracion' or columna == 'inventario':
                col_seleccionada = True
            elif columna == 'idPelicula':
                print(
                    f"ERROR: No se puede actualizar el identificador, pon alguna de estas opciones: \n - nombre \n - genero \n - duracion\n - inventario\n")
                columna = ""
            else:
                print(f"ERROR: Columna no valida, pon alguna de estas opciones: \n - nombre \n - genero \n - duracion\n - inventario\n")
                columna = ""
        id_seleccionado = False
        while not (id_seleccionado):
            try:
                id = int(input(f"Dame el identificador del registro al que actualizaras su columna: "))
                cantidad = 0
                for registro in Peliculas.query.all():
                    cantidad = cantidad + 1
                if id <= cantidad and id > 0:
                    id_seleccionado = True
                else:
                    print(
                        f"ERROR: No existe algun registro con el identificador {id}, escoge un entero de este rango (1 - {cantidad})\n")
                    id = 0
            except:
                print(f"ERROR: Identificador no valido, intentalo nuevamente\n")
                id = 0
        act = input(f"Dame el valor por la que se quiera actualizar la columna {columna} en el registro con id {id}: ")
        pelicula = Peliculas.query.filter(Peliculas.idPelicula == id).first()
        if columna == 'nombre':
            pelicula.nombre = act
        elif columna == 'genero':
            pelicula.genero = act
        elif columna == 'duracion':
            pelicula.duracion = act
        elif columna == 'inventario':
            pelicula.inventario = act
        print("Actualización con exito!")
        db.session.commit()
    elif tabla == 'rentar':
        id_seleccionado = False
        while not (id_seleccionado):
            try:
                id = int(input(f"Dame el identificador del registro al que actualizaras su columna: "))
                cantidad = 0
                for registro in Rentar.query.all():
                    cantidad = cantidad + 1
                if id <= cantidad and id > 0:
                    id_seleccionado = True
                else:
                    print(
                        f"ERROR: No existe algun registro con el identificador {id}, escoge un entero de este rango (1 - {cantidad})\n")
                    id = 0
            except:
                print(f"ERROR: Identificador no valido, intentalo nuevamente\n")
                id = 0
        renta = Rentar.query.filter(Rentar.idRentar == id).first()
        renta.fecha_renta = datetime.now()
        print("Fecha actualizada!")
        db.session.commit()


def eliminar_registro(tabla,seleccion):
    if seleccion == 1:
        id_seleccionado = False
        if tabla == 'usuarios':
            while not (id_seleccionado):
                try:
                    id = int(input(f"Dame el identificador del registro al que eliminaras: "))
                    cantidad = 0
                    for registro in Usuarios.query.all():
                        cantidad = cantidad + 1
                    if id <= cantidad and id > 0:
                        id_seleccionado = True
                    else:
                        print(
                            f"ERROR: No existe algun registro con el identificador {id}, escoge un entero de este rango (1 - {cantidad})\n")
                        id = 0
                except:
                    print(f"ERROR: Identificador no valido, intentalo nuevamente\n")
                    id = 0
            usuario = Usuarios.query.filter(Usuarios.idUsuario == id).first()
            eliminado = True
            try:
                db.session.delete(usuario)
                db.session.commit()
            except sqlalchemy.exc.IntegrityError:
                print(f"ERROR: No se puede eliminar este registro, su identificador {id} es una llave foranea de otra tabla")
                print("Usuario no eliminado!")
                eliminado = False
            if eliminado:
                print("Usuario eliminado!")
                actualizar_ids('usuarios')
        elif tabla == 'peliculas':
            while not (id_seleccionado):
                try:
                    id = int(input(f"Dame el identificador del registro al que eliminaras: "))
                    cantidad = 0
                    for registro in Peliculas.query.all():
                        cantidad = cantidad + 1
                    if id <= cantidad and id > 0:
                        id_seleccionado = True
                    else:
                        print(
                            f"ERROR: No existe algun registro con el identificador {id}, escoge un entero de este rango (1 - {cantidad})\n")
                        id = 0
                except:
                    print(f"ERROR: Identificador no valido, intentalo nuevamente\n")
                    id = 0
            pelicula = Peliculas.query.filter(Peliculas.idUsuario == id).first()
            eliminado = True
            try:
                db.session.delete(pelicula)
                db.session.commit()
            except sqlalchemy.exc.IntegrityError:
                print(
                    f"ERROR: No se puede eliminar este registro, su identificador {id} es una llave foranea de otra tabla")
                print("Pelicula no eliminada!")
                eliminado = False
            if eliminado:
                print("Pelicula eliminada!")
                actualizar_ids('peliculas')
        elif tabla == 'rentar':
            while not (id_seleccionado):
                try:
                    id = int(input(f"Dame el identificador del registro al que eliminaras: "))
                    cantidad = 0
                    for registro in Rentar.query.all():
                        cantidad = cantidad + 1
                    if id <= cantidad and id > 0:
                        id_seleccionado = True
                    else:
                        print(
                            f"ERROR: No existe algun registro con el identificador {id}, escoge un entero de este rango (1 - {cantidad})\n")
                        id = 0
                except:
                    print(f"ERROR: Identificador no valido, intentalo nuevamente\n")
                    id = 0
            renta = Usuarios.query.filter(Usuarios.idUsuario == id).first()
            eliminado = True
            try:
                db.session.delete(renta)
                db.session.commit()
            except sqlalchemy.exc.IntegrityError:
                print(
                    f"ERROR: No se puede eliminar este registro, su identificador {id} es una llave foranea de otra tabla")
                print("Renta no eliminada!")
                eliminado = False
            if eliminado:
                print("Renta eliminada!")
                actualizar_ids('rentar')
    elif seleccion == 2:
        id = 1
        if tabla == 'usuarios':
            eliminados = False
            for registro in Usuarios.query.all():
                usuario = Usuarios.query.filter(Usuarios.idUsuario == id).first()
                try:
                    db.session.delete(usuario)
                    db.session.commit()
                    eliminados = True
                except sqlalchemy.exc.IntegrityError:
                    db.session.rollback()
                id = id + 1
            if eliminados:
                print("Usuarios eliminados!")
            else:
                print("No hubo eliminados!")
        elif tabla == 'peliculas':
            eliminados = False
            for registro in Peliculas.query.all():
                pelicula = Peliculas.query.filter(Peliculas.idPelicula == id).first()
                try:
                    db.session.delete(pelicula)
                    db.session.commit()
                    eliminados = True
                except sqlalchemy.exc.IntegrityError:
                    db.session.rollback()
                id = id + 1
            if eliminados:
                print("Peliculas eliminadas!")
            else:
                print("No hubo eliminados!")
        elif tabla == 'rentar':
            eliminados = False
            for registro in Rentar.query.all():
                renta = Rentar.query.filter(Rentar.idRentar == id).first()
                try:
                    db.session.delete(renta)
                    db.session.commit()
                    eliminados = True
                except sqlalchemy.exc.IntegrityError:
                    db.session.rollback()
                id = id + 1
            if eliminados:
                print("Rentas eliminadas!")
            else:
                print("No hubo eliminados!")

def actualizar_ids(tabla):
    id = 1
    if tabla == 'usuarios':
        for registro in Usuarios.query.all():
            registro.idUsuario = id
            db.session.commit()
            id += 1
    elif tabla == 'peliculas':
        for registro in Peliculas.query.all():
            registro.idPelicula = id
            db.session.commit()
            id += 1
    elif tabla == 'rentar':
        for registro in Rentar.query.all():
            registro.idRentar = id
            db.session.commit()
            id += 1


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        actualizar_ids('usuarios')
        seleccion = 0
        while seleccion != 5:
            try:
                seleccion = int(input("- Selecciona alguna opcion, ingresando el número que lo identifica: \n   1. Ver registros de una tabla. \n   2. Filtrar los registros de una tabla por id. \n   3. Actualizar nombre de la columna de un registro o modificar la fecha de renta. \n   4. Eliminar un registro por id o todos los registros. \n   5. Salir.\n"))
                if seleccion < 1 or seleccion > 5:
                    print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2,3,4,5).")
            except:
                print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2,3,4,5).")
                seleccion = 0

            tabla_seleccionada = False
            if seleccion == 1:
                # Ver registros de una tabla.
                while not(tabla_seleccionada):
                    tabla = input("Dame el nombre de la tabla, que quieres ver sus registros: ")
                    if tabla == 'usuarios' or tabla == 'peliculas' or tabla == 'rentar':
                        tabla_seleccionada = True
                    else:
                        print(f"ERROR: No existe una tabla con el nombre {tabla} en la base de datos, pon alguna de estas opciones: \n - usuarios \n - peliculas \n - rentar")
                        tabla = ""
                ver_registros(tabla)
            elif seleccion == 2:
                # Filtrar los registros de una tabla por id.
                while not (tabla_seleccionada):
                    tabla = input("Dame el nombre de la tabla: ")
                    if tabla == 'usuarios' or tabla == 'peliculas' or tabla == 'rentar':
                        tabla_seleccionada = True
                    else:
                        print(f"ERROR: No existe una tabla con el nombre {tabla} en la base de datos, pon alguna de estas opciones: \n - usuarios \n - peliculas \n - rentar")
                        tabla = ""
                id = input("Dame el identificador: ")
                filtrar_registros(tabla,id)
            elif seleccion == 3:
                # Actualizar nombre de la columna de un registro y modificar la fecha de renta. \n   4. Eliminar un registro por id o todos los registros.
                while not (tabla_seleccionada):
                    tabla = input("Dame el nombre de la tabla: ")
                    if tabla == 'usuarios' or tabla == 'peliculas' or tabla == 'rentar':
                        tabla_seleccionada = True
                    else:
                        print(
                            f"ERROR: No existe una tabla con el nombre {tabla} en la base de datos, pon alguna de estas opciones: \n - usuarios \n - peliculas \n - rentar")
                        tabla = ""
                actualizar_registro(tabla)
            elif seleccion == 4:
                # Eliminar un registro por id o todos los registros.
                while not (tabla_seleccionada):
                    tabla = input("Dame el nombre de la tabla: ")
                    if tabla == 'usuarios' or tabla == 'peliculas' or tabla == 'rentar':
                        tabla_seleccionada = True
                    else:
                        print(
                            f"ERROR: No existe una tabla con el nombre {tabla} en la base de datos, pon alguna de estas opciones: \n - usuarios \n - peliculas \n - rentar")
                        tabla = ""
                seleccion = 0
                while seleccion != 1 and seleccion != 2:
                    try:
                        seleccion = int(input("Selecciona alguna opcion, ingresando el número que lo identifica: \n   1. Eliminar un registro por id. \n   2. Eliminar todos los registros. \n"))
                        if seleccion < 1 or seleccion > 2:
                            print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2).")
                            seleccion = 0
                        else:
                            opcion_sel = True
                    except:
                        print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2).")
                        seleccion = 0
                eliminar_registro(tabla, seleccion)
