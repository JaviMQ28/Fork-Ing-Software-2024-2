import random as rm

if __name__ == '__main__':

    # Prueba del programa
    simularJuego = 0
    while simularJuego != 2:
        try:
            simularJuego = int(input("- Selecciona alguna opcion, ingresando el número que lo identifica: \n   1. Simular un juego de tenis. \n   2. Salir.\n"))
            if simularJuego < 1 or simularJuego > 2:
                print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2).")        
        except:
            print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2).")        
            simularJuego = 0 

        if simularJuego == 1:
            # Registro de jugadores
            print("\n--- Partido de tenis ---\n - Registro de jugadores:")

            # -> Registro del primer jugador
            jugador1 = ""
            while jugador1 == "":
                jugador1 = input("Dame el nombre de un jugador = ")
                if jugador1 == "":
                    print("ERROR: El jugador debe de tener un nombre, intentalo nuevamente.")
            print(" -> El jugador " + jugador1 + " se ha registrado")

            # -> Registro del segundo jugador
            jugador2 = ""
            while jugador2 == "":
                jugador2 = input("Dame el nombre de un jugador = ")
                if jugador2 == "":
                    print("ERROR: El jugador debe de tener un nombre, intentalo nuevamente.")
            print(" -> El jugador " + jugador2 + " se ha registrado")

            # Registro de la cantidad de sets
            print("\n- Registro de sets:")

            # Define la cantidad de sets, siempre tiene que ser impar
            numImpar = False
            while not(numImpar):
                try:
                    numSets = int(input("Dame la cantidad de sets para el partido de " + jugador1 + " vs " + jugador2 + " = "))
                    if numSets > 0 and numSets % 2 != 0:
                        numImpar = True
                    else:
                        print("ERROR: La cantidad de sets no tiene que ser par, intentalo nuevamente.")
                except:
                    print("ERROR: El dato recibido no es un numero entero, intentalo nuevamente.")

            # Sets de cada jugador
            setsJugador1 = 0
            setsJugador2 = 0
            # Ganador del juego
            ganadorPartido = None

            # Selecciona jugador que saque primero
            jugadorSaca = None
            saque = rm.randrange(0,2)
            # Jugador que saca
            if saque == 1:
                jugadorSaca = jugador1
            else:
                jugadorSaca = jugador2

            # TO-DO -> Partido en ejecucion
            while ganadorPartido == None:        

                # Juegos de cada jugador
                juegosJugador1 = 0
                juegosJugador2 = 0    
                setFinalizado = False    

                while not(setFinalizado):

                    # Puntos de cada jugador
                    puntosJugador1 = 0
                    puntosJugador2 = 0
                    juegoFinalizado = False        

                    while not(juegoFinalizado):            
                        print("\n * Saca el jugador " + jugadorSaca)

                        # Punto seleccionado para un jugador
                        puntoSel = False
                        while not(puntoSel):
                            empate = False
                            ganadorPunto = str(input("- Punto para: "))
                            if ganadorPunto == jugador1:
                                ganadorPunto = jugador1
                                puntoSel = True
                            elif ganadorPunto == jugador2:
                                ganadorPunto = jugador2
                                puntoSel = True
                            else:
                                print("ERROR: Tiene que ser un nombre de algun jugador del partido.")

                        if ganadorPunto == jugador1:
                            punto = puntosJugador1
                        else:
                            punto = puntosJugador2

                        match punto:
                            case 0:
                                punto = 15
                            case 15:
                                punto = 30
                            case 30:
                                punto = 40
                            case 40:                    
                                if (ganadorPunto == jugador1 and puntosJugador2 == 40) or (ganadorPunto == jugador2 and puntosJugador1 == 40):
                                    punto = "Adv"
                                elif (ganadorPunto == jugador1 and puntosJugador2 == "Adv") or (ganadorPunto == jugador2 and puntosJugador1 == "Adv"):
                                    puntosJugador1 = 40
                                    puntosJugador2 = 40
                                    empate = True
                                elif (ganadorPunto == jugador1 and puntosJugador2 < 40) or (ganadorPunto == jugador2 and puntosJugador1 < 40):
                                    punto = "game"
                            case "Adv":
                                if (ganadorPunto == jugador1 and puntosJugador2 == "Adv") or (ganadorPunto == jugador2 and puntosJugador1 == "Adv"):
                                    puntosJugador1 = 40
                                    puntosJugador2 = 40
                                    empate = True
                                elif (ganadorPunto == jugador1 and puntosJugador2 <= 40) or (ganadorPunto == jugador2 and puntosJugador1 <= 40):
                                    punto = "game"

                        if ganadorPunto == jugador1 and not(empate):
                            puntosJugador1 = punto
                        elif ganadorPunto == jugador2 and not(empate):
                            puntosJugador2 = punto

                        print(f' -> Marcador: \n     - {jugador1} = {puntosJugador1} \n     - {jugador2} = {puntosJugador2}')

                        #""" TO-DO -> Cuenta de quien se lleva el juego
                
                        if puntosJugador1 == "game":
                            juegosJugador1 += 1
                            juegoFinalizado = True
                        elif puntosJugador2 == "game":
                            juegosJugador2 += 1
                            juegoFinalizado = True
                        #"""        

                        # Cambio de cancha
                        if juegoFinalizado and (juegosJugador1 - juegosJugador2) % 2 != 0:
                            print("\n** CAMBIO DE CANCHA **\n")     

                    print(f'\n- > Puntaje de juegos: \n     - {jugador1} = {juegosJugador1} \n     - {jugador2} = {juegosJugador2}')        

                    #""" TO-DO -> Cuenta de quien se lleva el set
                
                    if juegosJugador1 >= 6 and juegosJugador1 >= juegosJugador2 + 2:
                        setsJugador1 += 1
                        setFinalizado = True
                    elif juegosJugador2 >= 6 and juegosJugador2 >= juegosJugador1 + 2:
                        setsJugador2 += 1
                        setFinalizado = True
                    #"""         
                        
                    # Cambio de jugador que saca
                    if jugadorSaca == jugador1:
                        jugadorSaca = jugador2
                    elif jugadorSaca == jugador2:
                        jugadorSaca = jugador1

                # El jugador que haga el mayor numero de sets, sera el ganador
                if setsJugador1 > numSets/2 and setsJugador2 <= numSets - setsJugador1:
                    ganadorPartido = jugador1
                elif setsJugador2 > numSets/2 and setsJugador1 <= numSets - setsJugador2:
                    ganadorPartido = jugador2
                print(f'\n -> Puntaje de sets: \n     - {jugador1} = {setsJugador1} \n     - {jugador2} = {setsJugador2}')

            print("\n*** Ganador del partido = " + ganadorPartido + " ***\n")       