from datetime import datetime

class Orden:
    """Clase para representar una orden de compra"""
    
    def __init__(self, id, items, total, fecha, cliente):
        self.id = id
        self.items = items
        self.total = total
        self.fecha = fecha
        self.cliente = cliente
        self.estado = "Pendiente"
    
    def procesar_orden(self):
        """Procesar la orden"""
        self.estado = "Procesada"
        return True
    
    def __str__(self):
        return f"Orden #{self.id} - {self.cliente} - ${self.total:.2f} - {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def __repr__(self):
        return f"Orden(id={self.id}, cliente='{self.cliente}', total={self.total})"

class PilaOrdenes:
    """Clase para manejar una pila de órdenes"""
    
    def __init__(self):
        self.ordenes = []  # Pila para almacenar las órdenes
    
    def push(self, orden):
        """Agregar una orden a la pila"""
        self.ordenes.append(orden)
    
    def pop(self):
        """Sacar la última orden de la pila"""
        if not self.esta_vacia():
            return self.ordenes.pop()
        return None
    
    def peek(self):
        """Ver la última orden sin sacarla"""
        if not self.esta_vacia():
            return self.ordenes[-1]
        return None
    
    def esta_vacia(self):
        """Verificar si la pila está vacía"""
        return len(self.ordenes) == 0
    
    def tamanio(self):
        """Obtener el tamaño de la pila"""
        return len(self.ordenes)
    
    def obtener_todas(self):
        """Obtener todas las órdenes de la pila"""
        return self.ordenes.copy()
    
    def __str__(self):
        if self.esta_vacia():
            return "Pila de órdenes vacía"
        
        ordenes_str = "\n".join([f"  {orden}" for orden in reversed(self.ordenes)])
        return f"Pila de Órdenes (última arriba):\n{ordenes_str}"
    
    def __len__(self):
        return len(self.ordenes)
