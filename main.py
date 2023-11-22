from trueTables.ALU import ALU  # Importa la clase ALU desde tu archivo correspondiente
from trueTables.XOR import XOR  # Importa la clase ALU desde tu archivo correspondiente

def main():
    # Crear una instancia de la ALU
    alu = ALU()
    nott = XOR()

    # Probar diferentes operaciones con valores de entrada
    result = alu.execute(0, 1, "A-1")  # Suma los valores de entrada de A y D
    print("Resultado de A+D:", result)

    result = alu.execute(7, 3, "A|D")  # Realiza la operacion AND entre A y D
    print("Resultado de A&D:", result)

    # Puedes seguir probando mas operaciones aqui
    result = nott.execute(2,8)
    print("Resultado de not:", result)


if __name__ == "__main__":
    main()
