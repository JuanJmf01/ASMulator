from trueTables.And import AndGate
from trueTables.Or import OrGate
from trueTables.XOR import XorGate
from trueTables.Not import NotGate
from trueTables.RegisterA import RegisterA
from trueTables.RegisterD import RegisterD

class ALU:
    def __init__(self):
        self.register_A = RegisterA()
        self.register_D = RegisterD()

    def perform_operation(self, operation, input1, input2):
        if operation == "ADD":
            self.register_D.set_value(self.add(input1, input2))
        elif operation == "SUB":
            self.register_D.set_value(self.subtract(input1, input2))
        elif operation == "AND":
            self.register_D.set_value(self.perform_and(input1, input2))
        elif operation == "OR":
            self.register_D.set_value(self.perform_or(input1, input2))
        elif operation == "XOR":
            self.register_D.set_value(self.perform_xor(input1, input2))
        else:
            raise ValueError("Unsupported operation")
        
    def add(self, input1, input2):
        if len(input1) != 16 or len(input2) != 16:
            raise ValueError("Inputs must be 16-bit binary numbers")

        sum_result = ""
        carry = '0'

        for i in range(15, -1, -1):
            bit_input1 = input1[i]
            bit_input2 = input2[i]

            # Realizar la suma bit a bit utilizando compuertas logicas XOR y AND para el acarreo
            bit_sum = XorGate.perform_xor(bit_input1, bit_input2)
            current_bit_result = XorGate.perform_xor(bit_sum, carry)

            # Calcular el acarreo para el siguiente bit
            carry = OrGate.perform_or(
                AndGate.perform_and(bit_sum, carry),
                AndGate.perform_and(bit_input1, bit_input2)
            )

            # Construir el resultado bit a bit
            sum_result = current_bit_result + sum_result

        return sum_result



    def subtract(self, input1, input2):
        if len(input1) != 16 or len(input2) != 16:
            raise ValueError("Inputs must be 16-bit binary numbers")

        # Invertir el segundo numero (utilizando la operacion NOT)
        inverted_input2 = ""
        not_gate = NotGate()
        for bit in input2:
            inverted_input2 += not_gate.perform_not(bit)

        # Sumar el primer numero con la representacion invertida del segundo numero
        # Esto es igual a restar, ya que la suma de input1 + (-input2) es lo mismo que input1 - input2
        temp_result = self.add(input1, inverted_input2)

        # Agregar 1 al resultado para tener en cuenta el bit de signo
        one = '0000000000000001'
        final_result = self.add(temp_result, one)

        return final_result[-16:]

    def perform_and(self, input1, input2):
        # Implementacion de la operacion AND utilizando la compuerta logica AndGate
        and_gate = AndGate()
        and_gate.set_inputs(input1, input2)
        return and_gate.perform_and()

    def perform_or(self, input1, input2):
        # Implementacion de la operacion OR utilizando la compuerta logica OrGate
        or_gate = OrGate()
        or_gate.set_inputs(input1, input2)
        return or_gate.perform_or()

    def perform_xor(self, input1, input2):
        # Implementacion de la operacion XOR utilizando la compuerta logica XorGate
        xor_gate = XorGate()
        xor_gate.set_inputs(input1, input2)
        return xor_gate.perform_xor()
