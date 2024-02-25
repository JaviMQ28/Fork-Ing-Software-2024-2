import pymysql.cursors
from datetime import datetime, timedelta

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='lab',
                             password='Developer123!',
                             database='lab_ing_software',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def inserta():
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `usuarios` (`idUsuario`, `nombre`, `apPat`, `apMat`, `password`, `email`, `profilePicture`, `superUser`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            idUsuario = 1
            query = "SELECT COUNT(*) FROM `usuarios`"
            cursor.execute(query)
            resultado = cursor.fetchone()
            if resultado != None:
                idUsuario = resultado['COUNT(*)'] + 1
            nombre = input("Dame el nombre del usuario: ")
            app_pat = input("Dame el apellido paterno del usuario: ")
            app_mat = input("Dame el apellido Materno del usuario: ")
            contra = input("Contraseña: ")
            cursor.execute(sql,(idUsuario, nombre, app_pat, app_mat, contra, None, None, None))
            connection.commit()

            sql = "INSERT INTO `peliculas` (`idPelicula`, `nombre`, `genero`, `duracion`, `inventario`) VALUES (%s, %s, %s, %s, %s)"
            idPelicula = 1
            query = "SELECT COUNT(*) FROM `peliculas`"
            cursor.execute(query)
            resultado = cursor.fetchone()
            if resultado != None:
                idPelicula = resultado['COUNT(*)'] + 1
            nombre = input("Dame el nombre de la pelicula: ")
            cursor.execute(sql, (idPelicula, nombre, None, None, 1))
            connection.commit()

            sql = "INSERT INTO `rentar` (`idRentar`, `idUsuario`, `idPelicula`, `fecha_renta`, `dias_de_renta`, `estatus`) VALUES (%s, %s, %s, %s, %s, %s)"
            idRenta = 1
            query = "SELECT COUNT(*) FROM `rentar`"
            cursor.execute(query)
            resultado = cursor.fetchone()
            if resultado != None:
                idRenta = resultado['COUNT(*)'] + 1
            cursor.execute(sql, (idRenta, idUsuario, idPelicula, datetime.now(), None, None))
            connection.commit()


def filtra_usuario(apellido):
    with connection:
        with connection.cursor() as cursor:
            print(f"\nUsuarios con el apellido {apellido}:\n")
            query = "SELECT * FROM `usuarios`"
            cursor.execute(query)
            resultado = cursor.fetchall()
            for usuario in resultado:
                if usuario['apPat'] == apellido or usuario['apMat'] == apellido:
                    print(f"- {usuario['nombre']}\n")


def cambia_genero(nombre, genero):
    with connection:
        with connection.cursor() as cursor:
            query = "SELECT * FROM `peliculas`"
            cursor.execute(query)
            resultado = cursor.fetchall()
            for pelicula in resultado:
                if pelicula['nombre'] == nombre:
                    borra = f"DELETE FROM `peliculas` WHERE nombre = '%s'" % (nombre,)
                    cursor.execute(borra)
                    connection.commit()
                    idPelicula = 1
                    query = "SELECT COUNT(*) FROM `peliculas`"
                    cursor.execute(query)
                    resultado = cursor.fetchone()
                    if resultado != None:
                        idPelicula = resultado['COUNT(*)'] + 1
                    act = "INSERT INTO `peliculas` (`idPelicula`, `nombre`, `genero`, `duracion`, `inventario`) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(act, (idPelicula, pelicula['nombre'], genero, pelicula['duracion'], pelicula['inventario']))
                    connection.commit()


def elimina_rentas():
    with connection:
        with connection.cursor() as cursor:
            query = "SELECT * FROM `rentar`"
            cursor.execute(query)
            resultado = cursor.fetchall()
            for renta in resultado:
                if renta['fecha_renta'] <= datetime.now() - timedelta(days=3):
                    borra = f"DELETE FROM `rentar` WHERE idRentar = '%s'" % (renta['idRentar'],)
                    cursor.execute(borra)
                    connection.commit()


if __name__ == '__main__':
    inserta()
    #app = input("Dame un apellido: ")
    #filtra_usuario(app)
    #nombre = input("Dame el nombre de una pelicula: ")
    #genero = input(f"Dame el genero por la que se cambiara la pelicula {nombre}: ")
    #cambia_genero(nombre,genero)
    #elimina_rentas()
