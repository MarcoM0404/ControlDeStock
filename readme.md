# Sistema de Control de Stock

Este programa es un sistema de control de stock que te permite gestionar la información de productos, incluyendo su nombre, marca, precio, cantidad y códigos de barras únicos.
Luego vamos a agregarle una interfaz grafica con la librería gráfica "TKinder" así es más agradable el manejo del sistema.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python antes de ejecutar el programa:

- `cv2`
- `barcode_generator`
- `pyzbar`
- `pillow`
- `tk`

Puedes instalar estas bibliotecas utilizando el administrador de paquetes `pip`.

pip install barcode_generator
pip install pillow
pip install pyzbar
pip install opencv-python
pip install tk


# Cómo utilizar
Ejecuta el programa desde un entorno de Python.

Aparecerá un menú con las siguientes opciones: 
Ver todo el stock
Añadir producto
Modificar producto
Eliminar producto
Buscar producto por código
Buscar producto por nombre
Modificar cantidad del producto
Leer código de barra con ruta de imagen
Salir
Selecciona una opción ingresando el número correspondiente.

### Ver todo el stock
Esta opción muestra una tabla con todos los productos en el stock, incluyendo su código, nombre, marca, precio, cantidad y código de barras.

### Añadir producto
Puedes añadir un nuevo producto al stock ingresando su código, nombre, marca, precio y cantidad. El programa generará automáticamente un código de barras único para el producto.

### Modificar producto
Permite modificar la información de un producto existente en el stock, incluyendo su nombre, marca, precio y cantidad.

### Eliminar producto
Elimina un producto del stock después de confirmar la acción.

### Buscar producto por código
Busca un producto en el stock por su código y muestra su información.

### Buscar producto por nombre
Busca productos en el stock por nombre y muestra los resultados.

### Modificar cantidad del producto
Permite modificar la cantidad de un producto existente en el stock.

### Leer código de barra
Lee un código de barras a partir de una imagen o por su ruta de y muestra su información.

### Salir
Finaliza el programa.


# Lo que nos motivó
Nuestro proyecto fue inspirado por la idea de crear una solución práctica para gestionar el inventario de productos, permitiendo a los negocios los cuales se dediquen a la venta de productos, mantenerlos organizados.
Por otro lado, creemos que es un programa muy completo en el cual pudimos implementar todos los conocimientos que aprendimos a lo largo de la cursada y aprender otros nuevos importantes.
Por último, sabemos que este sistema es muy utilizado en diferentes comercios y esto nos puede ayudar a conseguir un empleo cuando lo subamos a nuestro repositorio.
