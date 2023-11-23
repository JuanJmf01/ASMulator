from trueTables.And import AndGate
from trueTables.Or import OrGate
from trueTables.XOR import XorGate
from trueTables.Not import NotGate

class ALU:

    def perform_operation(self, operation, registerA, registerD):

        input1 = registerA.get_value()
        input2 = registerD.get_value()

        if operation == "ADD":
            registerD.set_value(self.add(input1, input2))
        elif operation == "SUB":
            registerD.set_value(self.subtract(input2, input1))
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
    
