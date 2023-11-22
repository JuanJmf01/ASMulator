from trueTables.ALU import ALU

def main():
    # Crear una instancia de la ALU
    alu = ALU()

    # Establecer dos numeros binarios de 16 bits para sumar
    num1 = "0000000000001111"
    num2 = "0000000000000011"

    try:
        # Establecer los valores en los registros A y D
        alu.register_A.set_value(num1)
        alu.register_D.set_value(num2)

        # Realizar la suma utilizando la ALU
        alu.perform_operation("SUB", alu.register_A.get_value(), alu.register_D.get_value())

        # Obtener el resultado de la suma desde el registro D
        resultado = alu.register_D.get_value()

        # Mostrar los numeros y el resultado de la suma
        print(f"Numero 1: {num1}")
        print(f"Numero 2: {num2}")
        print(f"Resultado: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
