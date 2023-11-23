from CPU.ALU import ALU
from CPU.RAM import RAM

class InstructionDecoder:
    def __init__(self):
        self.operation = None
        self.alu = ALU()
        self.ram = RAM(16)

    def decode(self, instruction, registerA, registerD):
        # Aquí analizamos la instruccion y establecemos la operación a realizar en la CPU

        if instruction == 'ADD':
            self.alu.perform_operation(instruction, registerA, registerD)
        elif instruction == 'SUB':
            self.alu.perform_operation(instruction, registerA, registerD)
        elif instruction == 'LOAD_D':
            # Le mostramos al usuario loas valores de memoria actuales
            print("Tus valores guardados en: \n")
            self.ram.show_memory_status()

            direccion = input("Ingresa una direccion desde 0 a 15 para guardar el valor del registro D: ")
            self.ram.write(int(direccion), registerD.get_value())
            registerD.set_value('0000000000000000')
        elif instruction == 'READ_D':
            # Le mostramos al usuario loas valores de memoria actuales
            print("Tus valores guardados en: \n")
            self.ram.show_memory_status()
            direccion = input("Ingresa una direccion desde 0 a 15 para guardar en registro D una valor de memoria: ")

            # Asigamos el valor obtenido de memoria al registro D
            newValueD = self.ram.read(int(direccion))
            registerD.set_value(newValueD)
            


        else:
            print("Entrada invalida. Asegurese de ingresar dos numeros binarios de 16 bits y la operación (ADD/SUB).")



    def get_operation(self):
        return self.operation
