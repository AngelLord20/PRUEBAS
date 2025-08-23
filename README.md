---------------------------------------------------------------------------------------------------------------------
prompt usado en la version 1.1:
Quiero que me ayudes para un proyecto universitario basado en el siguiente flujo de compra (solo hasta el paso 6):

1. El proceso inicia con el **Cliente** que selecciona un ítem.
2. El ítem se agrega al **Carrito de Compras**.
3. Se envían los detalles del ítem al paso de **Checkout**.
4. El cliente procede al **Checkout**.
5. En **Collect Payment**, se procesa el pago.
6. El sistema envía la información de pago a la **Compañía de Tarjeta de Crédito**.
7. La compañía recibe el dinero y confirma el pago.
8. Una vez confirmado, se emite la orden en **Order Issue**.
9. El sistema envía la información de orden al **Departamento de Contabilidad**.
10. También se envía una solicitud de envío al **Inventario**.
11. El **Inventario** prepara el producto.
12. El producto es enviado al **Cliente**.
13. Paralelamente, el sistema envía un recibo electrónico al **Cliente**."


**Requisitos técnicos: de todos los puntos(1-6)**

* Lenguaje: **Python**.
* Debe implementar **estructuras de datos** de los temas vistos en clase: listas, pilas, colas, etc. (mínimo una de cada tipo).
* Debe permitir **añadir, modificar, borrar y consultar artículos** en el carrito.
* La información debe persistir en un archivo **.CSV** con nombres de campos descriptivos.
* Debe manejar **fechas** (ej. fecha de compra).
* Se debe usar una interfaz gráfica con **Tkinter** (ej. campos de texto, botones, visualización de carrito).
* Se debe mostrar gráficamente el contenido de **una lista, una pila y una cola** relacionadas con el flujo (ej. lista de artículos, pila de órdenes, cola de pagos).


Importante:
El resultado debe ser código en Python, funcional y sin errores, siguiendo las reglas del documento del proyecto.
Por ahora centrémonos en el Cliente, y únicamente lo esencia para que esta funcione

---------------------------------------------------------------------------------------------------------------------




---------------------------------------------------------------------------------------------------------------------
v1.2
se movio los archivos a una carpeta llamada pruebas, funcionan correctamente
---------------------------------------------------------------------------------------------------------------------




---------------------------------------------------------------------------------------------------------------------
v2.0
se agrego el codigo de los archivos de pruebas a los archivos originales, y luego se areglaron error, el principal error era
 
 
 un from Cliente import Cliente que no se usaba 
el error generaba esto:
Traceback (most recent call last):
  File "c:\Users\Angel\Documents\UNIVERSIDAD\2025-UNA\2 ciclo\ESTRUCTURAS DE DATOS\PRUEBAS_V1\PRUEBAS\Src\main.py", line 12, in <module>
    from Carrito import Carrito
  File "c:\Users\Angel\Documents\UNIVERSIDAD\2025-UNA\2 ciclo\ESTRUCTURAS DE DATOS\PRUEBAS_V1\PRUEBAS\Src\Carrito.py", line 1, in <module>
    from Cliente import Cliente
  File "c:\Users\Angel\Documents\UNIVERSIDAD\2025-UNA\2 ciclo\ESTRUCTURAS DE DATOS\PRUEBAS_V1\PRUEBAS\Src\Cliente.py", line 4, in <module>
    from Carrito import Carrito
ImportError: cannot import name 'Carrito' from 'Carrito' (consider renaming 'c:\\Users\\Angel\\Documents\\UNIVERSIDAD\\2025-UNA\\2 ciclo\\ESTRUCTURAS DE DATOS\\PRUEBAS_V1\\PRUEBAS\\Src\\Carrito.py' if it has the same name as a library you intended to import)



el promt usado para mover el codigo: 
Hay archivos que se encuentran en la carpeta llamada pruebas que funcionan correctamente, quiero que transfieras el código de esos archivos a sus archivos originales que se encuentran en la carpeta llamada Src, y los archivos csv a la carpeta llamada Data y las colas y similares en la carpeta llamada estructuras, es importante que no borres nada de los archivos en Src, solo implementa el nuevo código, además ten en cuenta la diferencia entre mayúsculas y minúsculas, y no olvides que ya que vas a mover el código, si se hacen llamadas a archivos cámbialos a sus respectivas nuevas rutas

Si hay casos como

producto en pruebas:self.id = id
producto original: self.id_producto = id_producto

manten el original y modifica el resto de los archivos para adaptarse a ello 

además si es posible trata de usar la las funciones ya implementas en el original como el agregar_producto que es diferente del de la prueba y el original, si esto ocasiona errores no lo hagas
---------------------------------------------------------------------------------------------------------------------




---------------------------------------------------------------------------------------------------------------------
