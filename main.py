from CPU.ALU import ALU
from CPU.RegisterA import RegisterA
from CPU.RegisterD import RegisterD
from CPU.InstructionDecoder import InstructionDecoder


def main():
    """
    Main function for the CPU simulator.

    Initializes the ALU, RegisterA, RegisterD, and InstructionDecoder.
    Allows the user to perform various operations using the CPU simulator.

    Returns:
    None
    """
    alu = ALU()
    registerA = RegisterA()
    registerD = RegisterD()
    instructionDecoder = InstructionDecoder()

    while True:
        print("Current D: ", registerD.get_value())
        print("Current A: ", registerA.get_value())
        currentRegisterD = registerD.get_value()
        print("Enter two 16-bit binary numbers and the operation ('exit' to quit): \n")

        # User defines the operation to be performed
        print("Operations: ")
        print("     Addition:                       'ADD'")
        print("     Subtraction:                    'SUB'")
        print("     Store D value in RAM:           'LOAD_D'")
        print("     Assign D a value from RAM:      'READ_D'")
        print("     Negate D:                       'NEGATE_D'")
        print("     Negate A:                       'NEGATE_A'")
        print("     Add 1 to D:                     'PLUSONE_D' \n")

        operation = input("Operation: ")

        if operation.upper() not in [
            "ADD",
            "SUB",
            "LOAD_D",
            "READ_D",
            "NEGATE_D",
            "NEGATE_A",
            "PLUSONE_D",
        ]:
            print("Invalid input. Make sure to enter valid operations.")
            continue
        else:
            if (
                operation != "LOAD_D"
                and operation != "READ_D"
                and operation != "NEGATE_D"
                and operation != "NEGATE_A"
                and operation != "PLUSONE_D"
            ):
                # Save user-input values in registers A and D respectively
                registerA.set_value(input("Value for register A (16 bits): "))

                if currentRegisterD == "0000000000000000":
                    registerD.set_value(input("Value for register D (16 bits): "))

            # Access user-input values in registers A and D respectively
            input1 = registerA.get_value()
            input2 = registerD.get_value()

            if len(input1) != 16 or len(input2) != 16:
                print("Invalid input. Make sure to enter two 16-bit binary numbers.")

            if (
                input1.lower() == "exit"
                or input2.lower() == "exit"
                or operation.lower() == "exit"
            ):
                break

            instructionDecoder.decode(operation, registerA, registerD)

        result = registerD.get_value()
        print(
            f"Result of {operation.upper()} between {input1} and {input2}: {result} \n"
        )


if __name__ == "__main__":
    main()
