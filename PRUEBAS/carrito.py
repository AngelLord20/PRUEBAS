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
    """Clase para manejar el carrito de compras usando una lista"""
    
    def __init__(self):
        self.items = []  # Lista para almacenar los items del carrito
    
    def agregar_producto(self, producto, cantidad=1):
        """Agregar un producto al carrito"""
        # Verificar si el producto ya está en el carrito
        for item in self.items:
            if item.producto.id == producto.id:
                item.cantidad += cantidad
                return
        
        # Si no está, agregar nuevo item
        nuevo_item = ItemCarrito(producto, cantidad)
        self.items.append(nuevo_item)
    
    def eliminar_item(self, index):
        """Eliminar un item del carrito por índice"""
        if 0 <= index < len(self.items):
            del self.items[index]
    
    def modificar_cantidad(self, index, nueva_cantidad):
        """Modificar la cantidad de un item"""
        if 0 <= index < len(self.items) and nueva_cantidad > 0:
            self.items[index].cantidad = nueva_cantidad
    
    def vaciar(self):
        """Vaciar todo el carrito"""
        self.items.clear()
    
    def calcular_total(self):
        """Calcular el total del carrito"""
        total = 0
        for item in self.items:
            total += item.calcular_subtotal()
        return total
    
    def obtener_cantidad_items(self):
        """Obtener la cantidad total de items en el carrito"""
        return len(self.items)
    
    def esta_vacio(self):
        """Verificar si el carrito está vacío"""
        return len(self.items) == 0
    
    def __str__(self):
        if self.esta_vacio():
            return "Carrito vacío"
        
        items_str = "\n".join([str(item) for item in self.items])
        return f"Carrito:\n{items_str}\nTotal: ${self.calcular_total():.2f}"
    
    def __len__(self):
        return len(self.items)
