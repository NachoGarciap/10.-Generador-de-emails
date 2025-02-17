
class GeneradorEmail:

    def __init__(self):
        print('----- Generador de emails -----')
        self.correo = ''
        self.secciones = ['ventas', 'marketing', 'contabilidad', 'soporte']

        #para que el id aumente en el archivo .txt
        try:
            with open('correos.txt', 'r', encoding='utf8') as archivo:
                lineas = archivo.readlines()
                self.id_correo = len(lineas)
        except FileNotFoundError:
            self.id_correo = 0

    def menu(self):

        while True:
            print('----- Generador de emails -----')
            print('1. Crear email de empresa')
            print('2. Salir')

            try:
                opcion = int(input('Elige una opción: '))
            except ValueError:
                print('Elige una opcion correcta')
                continue

            if opcion == 1:
                self.crear_correo()
                self.guardar_correos()
            elif opcion==2:
                print('Saliendo del programa...')
                break
            else:
                print('Opcion no valida')

    def crear_correo(self):
        print('Por favor, introduce los siguientes datos: ')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        seccion = self.elegir_puesto()

        self.correo = f'{nombre}.{apellido}.{seccion}@empresa.com'

        return self.correo

    def elegir_puesto(self):

        while True:
            seccion = input(f'Elige una seccion {self.secciones}: ')
            if seccion not in self.secciones:
                print('Sección no valida, elige una correcta, por favor.')
            else:
                return seccion

    def guardar_correos(self):

        if self.correo:  # Verificamos que el correo ya se haya generado
            with open('correos.txt', 'a', encoding='utf8') as archivo:
                self.id_correo += 1
                archivo.write(f'{self.id_correo}. {self.correo}\n')
            print('Correo guardado correctamente.')
        else:
            print('No hay correo para guardar. Genera uno primero.')



prueba = GeneradorEmail()
prueba.menu()
