# 1 maximo comun divisor

def mcd (x,y):
    mcd = 1
    
    if x % y == 0:
        return y
    
    for k in range(int(y/2), 0, -1):
        if x % k == 0 and y % k == 0:
            mcd = k
            break
    return mcd

print(mcd(15, 20))
print()
# 2 minimo coumun mulplo
def mcm(x,y):
    z = max(x,y)
    
    while True:
        if (z % x == 0) and (z % y == 0):
            return z
    
        z +=1
    
print(mcm(13, 8))
print()
# 3 cadena de caracteres a diccionario



def cuentaPalabras(texto):
    palabras = texto.split(" ")
    palabrasContadas = {}
    contador = 0
    longitud = len(palabras)
    
    for i in range (0,longitud):
        primera = palabras[i]
        
        for j in range(0 , longitud):
            segunda = palabras[j]
            if primera == segunda:
                contador += 1
        palabrasContadas[primera] = contador    
        contador = 0
    return palabrasContadas    
    
    
texto = "hoy es un lindo dia y ha salido el sol lindo dia y ha salido el sol dia dia"    
    
cuentaPalabra = cuentaPalabras(texto)
print(cuentaPalabra)    
print()
# 4 una tupla con la palabra mas repetida   

def palabraMasRepetidad(cuentaPalabra):
    palabra = max(zip(cuentaPalabra.values(),cuentaPalabra.keys()))
    print('la palabra mas repetida es: {} '.format(palabra))
    
palabraMasRepetidad(cuentaPalabra)
print()

# 5 ValueError

def get_int_iterativo():
    while True:
        try:
            valor = int(input("Ingresa un numero: "))
            return valor
        except ValueError:
            print("El numero ingresado no es valido. Inténtalo de nuevo.")

def get_int_recursivo():
    try:
        valor = int(input("Ingresa un numero: "))
        return valor
    except ValueError:
        print("El numero ingresado no es valido. Inténtalo de nuevo.")
        return get_int_recursivo()



# 6 clase persona

class Persona:
    
    
    def __init__(self,nombre="", edad=0, dni="" ):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    
    
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,edad):
        if edad < 0:
            print("edad incorrecta")
            self.__edad = 0
        else:
            self.__edad = edad
            
        
        
        
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,dni):
        
            self.__dni = dni
        
    def mostrar(self):
        return "nombre: "+ self.nombre +"\nedad: "+ str(self.edad) + "\nD.N.I: "+ self.dni 
        
    def Es_mayor_de_edad(self):
        print("¿ Es mayor de edad ?")
        return self.edad >= 18
            
        
    
        
""" persona1 = Persona("carlos", 23, "334567891" )


persona1.nombre = "guilllermo"
persona1.edad = 19
persona1.dni = "30456445"

print(persona1.mostrar())

print(persona1.Es_mayor_de_edad()) """



class Cuenta:
    
    def __init__(self,titular,cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
        
    @property
    def titular(self):
        return self.__titular
    
    @property
    def titular(self,titular):
        self.__titular = titular
        
    @property
    def cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        return "Cuenta: \n" + "Titular: " + "nombre: "+ self.titular.nombre +"\nedad: "+ str(self.titular.edad) + "\nD.N.I: "+ self.titular.dni  + "\nCantidad: " + str(self.cantidad)
        
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self,cantidad): 
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad



class CuentaJoven(Cuenta):

    def __init__(self,titular,cantidad=0,bonificacion=0):
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion

    def mostrar(self):
        return "Cuenta Joven\n"+"Titular:"+self.titular.mostrar()+"\nCantidad:"+str(self.cantidad)+ "\nBonificación:"+str(self.bonificacion)+"%"
   
    def esTitularValido(self):
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()
    
    def retirar(self,cantidad):
        if not self.esTitularValido():
            print ("No puedes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)
