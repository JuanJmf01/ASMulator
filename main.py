from CPU.ALU import ALU
from CPU.RegisterA import RegisterA
from CPU.RegisterD import RegisterD
from CPU.InstructionDecoder import InstructionDecoder

def main():
    alu = ALU()
    registerA = RegisterA()
    registerD = RegisterD()
    intructionDecoder = InstructionDecoder()


    while True:
        print("Nuevo D: ", registerD.get_value())
        actualRegisterD = registerD.get_value()
        print("Ingrese dos números binarios de 16 bits y la operación ('exit' para salir): \n")



        # El usuario define la operacion a realizar
        print("Operaciones: ")
        print("     Suma:                            'ADD'")
        print("     Resta:                           'SUB'")
        print("     Guardar valor de D en RAM:       'LOAD_D'")
        print("     Asignar a D un valor de la RAM:  'READ_D' \n")

        operation = input("Operación: ")

        if operation.upper() not in ['ADD', 'SUB', 'LOAD_D', 'READ_D']:
            print("Entrada invalida. Asegurese de ingresar las operaciones validas.")
            continue
        else:
            if  operation != 'LOAD_D' and operation != 'READ_D':
                # Guardamos los valores ingresados por el usuario en los registros A y D respectivamente
                registerA.set_value(input("Valor para registro A (16 bits): "))

                if actualRegisterD == '0000000000000000': 
                    registerD.set_value(input("Valor para registro D (16 bits): "))


            # Accedemos a los valores ingresados por el usuario en los registros A y D respectivamente
            input1 = registerA.get_value()
            input2 = registerD.get_value()

            if len(input1) != 16 or len(input2) != 16:
                print("Entrada invalida. Asegurese de ingresar dos numeros binarios de 16 bits.")

            



            if input1.lower() == 'exit' or input2.lower() == 'exit' or operation.lower() == 'exit':
                break

        
            intructionDecoder.decode(operation, registerA, registerD)

        



        resultado = registerD.get_value()
        print(f"Resultado de {operation.upper()} entre {input1} y {input2}: {resultado} \n")


if __name__ == "__main__":
    main()
