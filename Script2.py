def contarValles(cadena):
    # Nivel del mar
    altura = 0    

    # Bandera cuando la altura disminuya, desde el nivel del mar
    bandera = False

    # Cantidad de valles
    numValle = 0

    for i in cadena:   
        # Cambia la altura, al recibir cierto caracter
        if i == 'D':
            altura -= 1
        elif i == 'U':
            altura += 1

        if i == 'D' and altura == 0:
            bandera = True
        elif i == 'U' and altura == 0:
            numValle += 1
            bandera = False
    print(f'-> Cantidad de valles que se recorrieron = {numValle} valle(s)')

# ----------------------------------------------
class Nodo:
    def __init__(self, elemento, izq, der, padre):
        # Elemento que tiene el nodo
        self.elemento = elemento
        # Nodo izquierdo
        self.izq = izq
        # Nodo derecho 
        self.der = der
        # Nodo padre 
        self.padre = padre

    def __str__(self):
        return f"({self.izq}, {self.elemento}, {self.der})"
    
    def agregaElemento(self,elem):
        nodo = Nodo(elem, None, None, None)        

        if nodo.elemento <= self.elemento:
            if self.izq is None:
                self.izq = nodo
                nodo.padre = self
            else:
                nodoAux = self.izq
                nodoAux.agregaElemento(nodo.elemento)                    

        elif nodo.elemento > self.elemento:
            if self.der is None:
                self.der = nodo
                nodo.padre = self
            else:
                nodoAux = self.der
                nodoAux.agregaElemento(nodo.elemento)

    # Raiz, izquierdo, derecho
    def preorden(self):         

        print(self.elemento, end="")

        if self.izq is not None:
            print(end=" , ")
            self.izq.preorden()
        if self.der is not None:
            print(end=" , ")
            self.der.preorden()

    # Izquierdo, raiz, derecho
    def inorden(self):         

        if self.izq is None and self.der is None:
            print(self.elemento, end="")          
        elif self.izq is not None:
            self.izq.inorden()
        if self.der is not None:
            print(end=" , ")
            print(self.elemento, end=" , ")            
            self.der.inorden()

    # Izquierdo, derecho, raiz
    def postorden(self):         

        if self.izq is None and self.der is None:
            print(self.elemento, end="")          
        elif self.izq is not None:
            self.izq.postorden()
            print(end=" , ")
        if self.der is not None:
            self.der.postorden()    
            print(end=" , ")        
            print(self.elemento, end="")


# Ejercicio seleccionado
ejercicioSel = 0
while ejercicioSel != 3:
    try:
        ejercicioSel = int(input("- Selecciona algun ejercicio para probarlo, ingresando el número que lo identifica: \n   1. Recorrido de un caminante. \n   2. Árbol binario. \n   3. Salir.\n"))
        if ejercicioSel < 1 or ejercicioSel > 3:
            print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2,3).")        
    except:
        print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2,3).")        
        ejercicioSel = 0 

    # Recorrido del caminante.
    if ejercicioSel == 1:
        res = 0
        while res != 2:
            # Sirve para saber si la cadena es correcta, es decir que solo contiene las letras U y D
            cadenaCorrecta = False
            # Cantidad de letras o otros caracteres especiales que no son U ni D.
            numError = 0

            while not(cadenaCorrecta):
                cadena = input("\nDame una cadena, que solo contenga las letras U y D:\n")    

                if cadena == "":
                    cadenaCorrecta = True
                else:
                    # Verifica que la cadena recibida sea con el formato correcto
                    for i in cadena:
                        if i != 'D' and i != 'U':
                            numError += 1
                        
                        if numError == 0:
                            cadenaCorrecta = True
                        else:
                            cadenaCorrecta = False
                
                if not(cadenaCorrecta):
                    print("ERROR: La cadena de caracteres debe de contener las letras U y D, intentalo nuevamente.")
                    numError = 0    

            # Resultado de la cantidad de valles que tiene
            contarValles(cadena)

            selec = False

            while not(selec):
                try:
                    res = int(input("- Selecciona una opción, ingresando el número que lo identifica: \n   1. Volver a ejecutar el programa. \n   2. Salir.\n"))
                    if res >= 1 and res <= 2:
                        selec = True
                    else:
                        print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2).")        
                except:
                    print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2).")        
                    res = None        

    # Arbol binario
    elif ejercicioSel == 2:
        raizAgregado = False
        while not(raizAgregado):
            elem = input("Ingresa un elemento: ")
            if elem != "":
                raizAgregado = True
            else:
                print("ERROR: No ingresaste ningun elemento, intentalo nuevamente.")
        raiz = Nodo(elem, None, None, None)
        res = 0
        while res != 5:
            selec = False

            print(f"\n -> Árbol = {raiz} \n")

            while not(selec):
                try:
                    res = int(input("- Selecciona una opción, ingresando el número que lo identifica: \n   1. Agregar un elemento. \n   2. Recorrido pre-orden. \n   3. Recorrido in-orden. \n   4. Recorrido post-orden. \n   5. Salir.\n"))
                    if res >= 1 and res <= 5:
                        selec = True
                    else:
                        print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2,3,4,5).")        
                except:
                    print("ERROR: La selección no es correcta, ingresa alguno de los números que se muestran (1,2,3,4,5).")        
                    res = None

            match res:
                case 1:
                    elemAgrega = input("Ingresa el elemento que se quiera agregar al árbol: ")
                    raiz.agregaElemento(elemAgrega)
                case 2:
                    print(end="\nRecorrido pre-orden = [")
                    raiz.preorden()
                    print(end="]")
                case 3:
                    print(end="\nRecorrido in-orden = [")
                    raiz.inorden()
                    print(end="]")
                case 4:
                    print(end="\nRecorrido post-orden = [")
                    raiz.postorden()
                    print(end="]")