from CPU.ALU import ALU
from CPU.RegisterA import RegisterA
from CPU.RegisterD import RegisterD
from CPU.InstructionDecoder import InstructionDecoder

def main():
    alu = ALU()
    registerA = RegisterA()
    registerD = RegisterD()
    intructionDecoder = InstructionDecoder()

    band = True


    while True:
        print("Nuevo D: ", registerD.get_value())

        # Accedemos a los valores ingresados por el usuario en los registros A y D respectivamente
        input1 = registerA.get_value()
        input2 = registerD.get_value()

        # El usuario define la operacion a realizar
        print("Operaciones: ")
        print("     Suma:                            'ADD'")
        print("     Resta:                           'SUB'")
        print("     Guardar valor de D en RAM:       'LOAD_D'")
        print("     Asignar a D un valor de la RAM:  'READ_D' \n")

        operation = input("Operación: ")

        if input1.lower() == 'exit' or input2.lower() == 'exit' or operation.lower() == 'exit':
            break

        if len(input1) != 16 or len(input2) != 16 or operation.upper() not in ['ADD', 'SUB', 'LOAD_D', 'READ_D']:
            print("Entrada invalida. Asegurese de ingresar dos numeros binarios de 16 bits y la operación (ADD/SUB).")
            continue
        else:
            intructionDecoder.decode(operation, registerA, registerD)


        
        print("Ingrese dos números binarios de 16 bits y la operación ('exit' para salir): \n")

        # Guardamos los valores ingresados por el usuario en los registros A y D respectivamente
        registerA.set_value(input("Número 1 (16 bits): "))

        if band: 
            registerD.set_value(input("Número 2 (16 bits): "))
            band = False

        



        resultado = registerD.get_value()
        print(f"Resultado de {operation.upper()} entre {input1} y {input2}: {resultado}")


if __name__ == "__main__":
    main()
