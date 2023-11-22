from trueTables.Or import Or
from trueTables.And import And
from trueTables.Not import Not
from trueTables.Mux16 import Mux16
from trueTables.XOR import XOR
from trueTables.RegisterA import RegisterA
from trueTables.RegisterD import RegisterD

class ALU:
    def __init__(self):
        self.register_a = RegisterA()
        self.register_d = RegisterD()
        self.not_gate = Not()
        self.or_gate = Or()
        self.and_gate = And()
        self.xor_gate = XOR()
        #self.mux = Mux16()



    def execute(self, input_a, input_d, instruction):
        self.register_a.set_value(input_a)
        self.register_d.set_value(input_d)

        # Realizar operaciones segun la instruccion
        if instruction == "0":  # Operacion A=D
            self.register_a.set_value(self.register_d.get_value())
        elif instruction == "1":  # Operacion D=A
            self.register_d.set_value(self.register_a.get_value())
        elif instruction == "-1":  # Operacion D=!A
            self.not_gate.execute(self.register_a.get_value())
            self.register_d.set_value(self.not_gate.execute(self.register_a.get_value()))
        elif instruction == "D":  # Operacion D=-A
            self.register_d.set_value(-self.register_a.get_value())
        elif instruction == "A+1":  # Operacion D=A+1
            self.increment_a()
        elif instruction == "D+1":  # Operacion D=D+1
            self.increment_d()
        elif instruction == "A-1":  # Operacion D=A-1
            self.decrement_a()
        elif instruction == "D-1":  # Operacion D=D-1
            self.decrement_d()
        elif instruction == "A+D":  # Operacion D=A+D
            for i in range(self.register_a.get_value()):
                self.increment_d()
        elif instruction == "A-D":  # Operacion D=A-D
            for i in range(self.register_a.get_value()):
                self.decrement_d()
        elif instruction == "D-A":  # Operacion D=D-A
            self.register_d.set_value(self.register_d.get_value() - self.register_a.get_value())
        elif instruction == "A&D":  # Operacion D=A&D
            self.register_d.set_value(self.and_gate.execute(self.register_a.get_value(), self.register_d.get_value()))
        elif instruction == "A|D":  # Operacion D=A|D
            self.register_d.set_value(self.or_gate.execute(self.register_a.get_value(), self.register_d.get_value()))
        else:
            raise ValueError("Instruccion no reconocida")
        
        return self.register_d.get_value()


    
    def increment_a(self):
        new_value = self.increment(self.register_a.get_value())
        self.register_d.set_value(new_value)  
        #print(self.register_d.get_value())


    def increment_d(self):
        new_value = self.increment(self.register_d.get_value())
        self.register_d.set_value(new_value)

    def decrement_a(self):
        new_value = self.decrement(self.register_a.get_value())
        self.register_d.set_value(new_value)

    def decrement_d(self):
        new_value = self.decrement(self.register_d.get_value())
        self.register_d.set_value(new_value)



    def increment(self, value):
        # Convertimos el valor de D a una lista de bits
        d_bits = [(value >> i) & 1 for i in range(16)]
        
        # Implementacion de la logica booleana para sumar 1 a D
        carry = 1  # Inicializamos el acarreo en 1
        
        for i in range(16):
            # Sumador completo de un bit
            temp_sum = self.xor_gate.execute(d_bits[i], carry)
            carry = d_bits[i] & carry  # Generacion de acarreo AND
            d_bits[i] = temp_sum  # Asignacion del resultado a la posicion del bit
        
        # Convertimos la lista de bits nuevamente a un valor entero
        new_value = sum(d_bits[i] << i for i in range(16))
        
        return new_value
        
        
    def decrement(self, value):
        # Convertimos el valor de D a una lista de bits
        d_bits = [(value >> i) & 1 for i in range(16)]
        
        # Implementacion de la logica booleana para restar 1 a D
        carry = 1  # Inicializamos el acarreo en 1
        
        for i in range(16):
            # Restador de un bit
            temp_diff = self.xor_gate.execute(d_bits[i], carry)
            borrow = self.and_gate.execute(self.not_gate.execute(d_bits[i]), carry)
            carry = borrow  # Generacion de acarreo (o prastamo en una resta)
            d_bits[i] = temp_diff  # Asignacion del resultado a la posicion del bit
        
        # Convertimos la lista de bits nuevamente a un valor entero
        new_value = sum(d_bits[i] << i for i in range(16))
        
        return new_value
