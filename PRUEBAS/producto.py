class Producto:
    """Clase para representar un producto en el sistema"""
    
    def __init__(self, id, nombre, precio, descripcion, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.stock = stock
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"
    
    def __repr__(self):
        return f"Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio})"
