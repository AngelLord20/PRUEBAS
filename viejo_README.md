# Sistema de Compras - Universidad

## Descripción
Este es un sistema de compras desarrollado en Python que implementa el flujo de compra hasta el paso 6, utilizando estructuras de datos como listas, pilas y colas. El sistema incluye una interfaz gráfica con Tkinter y persiste la información en archivos CSV.

## Flujo de Compra Implementado
1. **Cliente selecciona un ítem** - Interfaz gráfica para seleccionar productos
2. **Ítem se agrega al Carrito de Compras** - Lista para manejar items del carrito
3. **Se envían los detalles al Checkout** - Transferencia de información
4. **Cliente procede al Checkout** - Formulario de información del cliente
5. **En Collect Payment se procesa el pago** - Procesamiento de pagos
6. **Sistema envía información a Compañía de Tarjeta** - Simulación de envío

## Estructuras de Datos Implementadas

### 1. Lista - Carrito de Compras
- **Clase**: `Carrito`
- **Archivo**: `carrito.py`
- **Funcionalidad**: Maneja los items del carrito usando una lista
- **Operaciones**: Agregar, eliminar, modificar, vaciar, calcular total

### 2. Pila - Órdenes de Compra
- **Clase**: `PilaOrdenes`
- **Archivo**: `orden.py`
- **Funcionalidad**: Maneja las órdenes usando una pila (LIFO)
- **Operaciones**: Push, pop, peek, verificar si está vacía

### 3. Cola - Pagos Pendientes
- **Clase**: `ColaPagos`
- **Archivo**: `cola_pagos.py`
- **Funcionalidad**: Maneja los pagos usando una cola (FIFO)
- **Operaciones**: Enqueue, dequeue, peek, procesar siguiente pago

## Características del Sistema

### Interfaz Gráfica (Tkinter)
- **Panel de Productos**: Lista de productos disponibles con opciones para agregar al carrito
- **Panel del Carrito**: Visualización del carrito con opciones para modificar
- **Panel de Estructuras**: Visualización gráfica de las estructuras de datos
- **Panel de Checkout**: Formulario para información del cliente y pago

### Persistencia de Datos (CSV)
- **productos.csv**: Almacena información de productos
- **ordenes.csv**: Almacena historial de órdenes con fechas

### Funcionalidades Principales
- ✅ Agregar productos al carrito
- ✅ Modificar cantidades
- ✅ Eliminar items del carrito
- ✅ Vaciar carrito completo
- ✅ Procesar pagos
- ✅ Generar órdenes
- ✅ Visualizar estructuras de datos
- ✅ Manejo de fechas
- ✅ Persistencia en CSV

## Instalación y Uso

### Requisitos
- Python 3.6 o superior
- Tkinter (incluido en la mayoría de instalaciones de Python)

### Ejecución
```bash
python main.py
```

### Archivos del Proyecto
```
├── main.py              # Archivo principal con interfaz gráfica
├── producto.py          # Clase Producto
├── carrito.py           # Clase Carrito (Lista)
├── orden.py             # Clase Orden y PilaOrdenes (Pila)
├── pago.py              # Clase Pago
├── cola_pagos.py        # Clase ColaPagos (Cola)
├── productos.csv        # Datos de productos (se crea automáticamente)
├── ordenes.csv          # Historial de órdenes (se crea automáticamente)
└── README.md            # Este archivo
```

## Uso del Sistema

### 1. Seleccionar Productos
- En el panel izquierdo, seleccione un producto de la lista
- Haga clic en "Agregar al Carrito"
- El producto aparecerá en el panel del carrito

### 2. Gestionar el Carrito
- **Eliminar Item**: Seleccione un item y haga clic en "Eliminar Item"
- **Modificar Cantidad**: Seleccione un item y haga clic en "Modificar Cantidad"
- **Vaciar Carrito**: Haga clic en "Vaciar Carrito"

### 3. Procesar Compra
- Complete la información del cliente (nombre, email)
- Complete la información de pago (tarjeta, CVV, fecha)
- Haga clic en "Procesar Pago" para simular el pago
- Haga clic en "Generar Orden" para crear la orden

### 4. Visualizar Estructuras
- Use las pestañas en el panel inferior para ver:
  - **Lista de Productos**: Productos disponibles
  - **Pila de Órdenes**: Órdenes generadas (última arriba)
  - **Cola de Pagos**: Pagos procesados (primero en salir arriba)

## Estructura de Datos Detallada

### Lista (Carrito)
```python
# Agregar producto
carrito.agregar_producto(producto, cantidad)

# Eliminar item
carrito.eliminar_item(index)

# Modificar cantidad
carrito.modificar_cantidad(index, nueva_cantidad)

# Calcular total
total = carrito.calcular_total()
```

### Pila (Órdenes)
```python
# Agregar orden
pila.push(orden)

# Sacar última orden
ultima_orden = pila.pop()

# Ver última orden sin sacar
orden_actual = pila.peek()
```

### Cola (Pagos)
```python
# Agregar pago
cola.enqueue(pago)

# Procesar siguiente pago
pago_procesado = cola.dequeue()

# Ver siguiente pago sin procesar
siguiente_pago = cola.peek()
```

## Archivos CSV

### productos.csv
```csv
id,nombre,precio,descripcion,stock
1,Laptop HP,899.99,Laptop HP 15 pulgadas,10
2,Mouse Inalámbrico,25.50,Mouse inalámbrico Logitech,50
...
```

### ordenes.csv
```csv
id_orden,fecha,cliente,producto,cantidad,precio_unitario,subtotal,total_orden
1,2024-01-15 10:30:00,Juan Pérez,Laptop HP,1,899.99,899.99,899.99
...
```

## Notas Técnicas

- **Manejo de Fechas**: Se utiliza `datetime` para timestamps precisos
- **Validación**: Se incluyen validaciones básicas en formularios
- **Persistencia**: Los datos se guardan automáticamente en CSV
- **Interfaz Responsiva**: La interfaz se adapta al tamaño de la ventana
- **Manejo de Errores**: Incluye manejo básico de errores y validaciones

## Extensibilidad

El sistema está diseñado para ser fácilmente extensible:
- Agregar nuevas estructuras de datos
- Implementar más funcionalidades de pago
- Conectar con bases de datos reales
- Agregar reportes y estadísticas
- Implementar sistema de usuarios