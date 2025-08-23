from collections import deque
from datetime import datetime

class ColaPagos:
    """Clase para manejar una cola de pagos usando deque"""
    
    def __init__(self):
        self.pagos = deque()  # Cola para almacenar los pagos
    
    def enqueue(self, pago):
        """Agregar un pago al final de la cola"""
        self.pagos.append(pago)
    
    def dequeue(self):
        """Sacar el primer pago de la cola"""
        if not self.esta_vacia():
            return self.pagos.popleft()
        return None
    
    def peek(self):
        """Ver el primer pago sin sacarlo"""
        if not self.esta_vacia():
            return self.pagos[0]
        return None
    
    def esta_vacia(self):
        """Verificar si la cola está vacía"""
        return len(self.pagos) == 0
    
    def tamanio(self):
        """Obtener el tamaño de la cola"""
        return len(self.pagos)
    
    def obtener_todos(self):
        """Obtener todos los pagos de la cola"""
        return list(self.pagos)
    
    def procesar_siguiente_pago(self):
        """Procesar el siguiente pago en la cola"""
        if not self.esta_vacia():
            pago = self.dequeue()
            pago.procesar_pago()
            return pago
        return None
    
    def __str__(self):
        if self.esta_vacia():
            return "Cola de pagos vacía"
        
        pagos_str = "\n".join([f"  {pago}" for pago in self.pagos])
        return f"Cola de Pagos (primero en salir arriba):\n{pagos_str}"
    
    def __len__(self):
        return len(self.pagos)
