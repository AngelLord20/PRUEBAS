#from Cliente import Cliente
from Producto import Producto
from estructuras.Lista import Lista
#from Inventario import inventario

class ItemCarrito:
    """Clase para representar un item en el carrito"""
    
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
    
    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad
    
    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} = ${self.calcular_subtotal():.2f}"

class Carrito:
    def __init__(self, id):
        self.id = id
        self.productos = Lista()
        
    def agregar_producto(self, producto):
        id_producto = producto.getIdProducto()
        busqueda = self.productos.buscar(producto)
        if busqueda == -1:
            self.productos.agregar(producto)
            return True
        return False
          
    def eliminar_producto(self, producto):
        id_producto = producto.getIdProducto()
        busqueda = self.productos.buscar(producto)
        if busqueda != -1:
            self.productos.eliminar(producto)
            return True
        return False
    
    def mostrar_carrito(self):
        if not self.productos.esta_vacia():
            return self.productos
        return None

    def vaciar_carrito(self):
        """
        Vacía el carrito eliminando todos los productos.
        """
        self.productos.limpiar()
        return True

    # Métodos adicionales para compatibilidad con el sistema de pruebas
    def agregar_producto_con_cantidad(self, producto, cantidad=1):
        """Agregar un producto al carrito con cantidad específica"""
        # Verificar si el producto ya está en el carrito
        elementos = self.productos.obtener_elementos()
        for item in elementos:
            if hasattr(item, 'producto') and item.producto.getIdProducto() == producto.getIdProducto():
                item.cantidad += cantidad
                return True
        
        # Si no está, agregar nuevo item
        nuevo_item = ItemCarrito(producto, cantidad)
        self.productos.agregar(nuevo_item)
        return True
    
    def eliminar_item(self, index):
        """Eliminar un item del carrito por índice"""
        elementos = self.productos.obtener_elementos()
        if 0 <= index < len(elementos):
            item_a_eliminar = elementos[index]
            self.productos.eliminar(item_a_eliminar)
    
    def modificar_cantidad(self, index, nueva_cantidad):
        """Modificar la cantidad de un item"""
        elementos = self.productos.obtener_elementos()
        if 0 <= index < len(elementos) and nueva_cantidad > 0:
            elementos[index].cantidad = nueva_cantidad
    
    def vaciar(self):
        """Vaciar todo el carrito"""
        self.vaciar_carrito()
    
    def calcular_total(self):
        """Calcular el total del carrito"""
        total = 0
        for item in self.productos.obtener_elementos():
            if hasattr(item, 'calcular_subtotal'):
                total += item.calcular_subtotal()
            else:
                # Si es un producto directo (sin ItemCarrito)
                total += item.precio
        return total
    
    def obtener_cantidad_items(self):
        """Obtener la cantidad total de items en el carrito"""
        return self.productos.obtener_tamaño()
    
    def esta_vacio(self):
        """Verificar si el carrito está vacío"""
        return self.productos.esta_vacia()
    
    def __str__(self):
        if self.esta_vacio():
            return "Carrito vacío"
        
        items_str = "\n".join([str(item) for item in self.productos.obtener_elementos()])
        return f"Carrito:\n{items_str}\nTotal: ${self.calcular_total():.2f}"
    
    def __len__(self):
        return self.productos.obtener_tamaño()

        