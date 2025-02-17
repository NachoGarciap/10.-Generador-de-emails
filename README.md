📧 Generador de Emails para Empresas
Este proyecto es una aplicación en Python que permite generar correos electrónicos empresariales de manera interactiva. El usuario ingresa su nombre, apellido y elige una sección (por ejemplo, ventas, marketing, contabilidad o soporte) para formar el correo. Además, el programa guarda cada correo generado en un archivo de texto (correos.txt) y asigna un ID único que se incrementa de forma persistente (continúa desde el último número guardado en el archivo).

🚀 Características
Interfaz de línea de comandos: Interactúa con el usuario a través de un menú.

Generación de correos: Combina nombre, apellido y sección para formar el correo.

Persistencia de IDs: Lee el archivo correos.txt para determinar el último ID y lo incrementa al guardar nuevos correos.

Manejo de errores: Valida entradas y gestiona casos en los que el archivo no existe.