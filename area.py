# Programa en Python utilizando POO para calcular el área de un cuadrado.
# Utiliza una clase para representar un cuadrado y calcula su área a partir del valor del lado.


#Clase para representar el cuadrado y calcular su área.
class Cuadrado:

    #Constructor para inicializar la longitud del lado del cuadrado
    def __init__(self, longitud_lado: float):
        self.longitud_lado = longitud_lado

    #Verifica que la longitud sea positiva
    def es_valido(self) -> bool:
        #return: True si el lado es mayor que 0, False en caso contrario
        return self.longitud_lado > 0

    #Calcula el área del cuadrado.
    def calcular_area(self) -> float:
        #return: Área del cuadrado (float)
        return self.longitud_lado * self.longitud_lado

# Función principal que controla el flujo del programa
def main():
    # Mensaje de bienvenida (tipo string)
    mensaje_bienvenida: str = "Bienvenido al programa para calcular el área de un cuadrado."
    print(mensaje_bienvenida)

    # Solicitar al usuario la longitud del lado
    entrada_usuario: str = input("Por favor, ingrese la longitud del lado del cuadrado (en metros): ")

    # Convertimos a tipo float
    longitud_lado: float = float(entrada_usuario)

    # Creamos una instancia de la clase Cuadrado
    cuadrado = Cuadrado(longitud_lado)

    # Validamos y mostramos el área si es válido
    if cuadrado.es_valido():
        area: float = cuadrado.calcular_area()
        print(f"El área del cuadrado es: {area} metros cuadrados.")
    else:
        print("Error: la longitud del lado debe ser un número positivo.")

# Ejecutar solo si el archivo se corre directamente
if __name__ == "__main__":
    main()
