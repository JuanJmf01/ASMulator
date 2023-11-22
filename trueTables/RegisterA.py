class RegisterA:
    def __init__(self):
        self.value = 0  # Inicializamos el registro A en 0 al inicio
    
    def set_value(self, new_value):
        self.value = new_value  # Actualiza el valor del registro A
    
    def get_value(self):
        return self.value  # Obtiene el valor actual del registro A
