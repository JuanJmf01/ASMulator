class Mux16:

    def execute(self, input1, input2, sel):
        output = 0  # Inicializamos la salida
        
        for i in range(16):
            if (sel >> i) & 1 == 0:
                output |= (input1 >> i) & 1 << i  # Usamos bits de input1
            else:
                output |= (input2 >> i) & 1 << i  # Usamos bits de input2
        
        return output
