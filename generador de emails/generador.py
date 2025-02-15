import sys


class GeneradorEmail:

    def __init__(self):
        print('----- Generador de emails -----')
        self.correo = ''
        self.secciones = ['ventas', 'marketing', 'contabilidad', 'soporte']
        self.num_correo=0

    def menu(self):

        while True:
            print('----- Generador de emails -----')
            print('1. Introduce tu nombre y apellidos')
            print('2. Introduce la seccion a la que perteneces')
            print('3. Salir')

    def crear_correo(self):
        print('Por favor, introduce los siguientes datos: ')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')

        self.correo = f'{nombre}.{apellido}.{self.elegir_puesto()}@empresa.com'

        return self.correo

    def elegir_puesto(self):

        while True:
            seccion = input(f'Elige una seccion {self.secciones}: ')
            if seccion not in self.secciones:
                print('Seccion no valida, elige una correcta, por favor.')
            else:
                return seccion

    def guardar_correos(self):
        correo_generado = self.crear_correo()  # Guardamos el correo generado en una variable

        if correo_generado:  # Verificamos que el correo se haya generado
            with open('correos.txt', 'a', encoding='utf8') as archivo:
                self.num_correo += 1
                archivo.write(f'{self.num_correo}.' + correo_generado + '\n')  # Usamos la variable correo_generado
            print('Correo guardado correctamente.')
            sys.exit('Cerrando')  # Termina el programa después de guardar
        else:
            print('No hay correo para guardar. Genera uno primero.')


prueba = GeneradorEmail()
prueba.guardar_correos()
