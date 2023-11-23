from CPU.ALU import ALU
from RAM.RAM import RAM


class InstructionDecoder:
    def __init__(self):
        """
        Initializes the InstructionDecoder with an ALU and RAM.

        Returns:
        None
        """
        self.operation = None
        self.alu = ALU()
        self.ram = RAM(16)

    def decode(self, instruction, registerA, registerD):
        """
        Decodes the given instruction and performs the corresponding operation on the CPU.

        Args:
        - instruction (str): The instruction to be decoded and executed.
        - registerA (RegisterA): The register containing operand A.
        - registerD (RegisterD): The register containing operand D.

        Returns:
        None
        """
        if instruction == "ADD":
            self.alu.perform_operation(instruction, registerA, registerD)
        elif instruction == "SUB":
            self.alu.perform_operation(instruction, registerA, registerD)
        elif instruction == "LOAD_D":
            # Display current memory values to the user
            print("Your values stored in memory: \n")
            self.ram.show_memory_status()

            address = input(
                "Enter an address from 0 to 15 to store the value of register D: "
            )
            self.ram.write(int(address), registerD.get_value())
            registerD.set_value("0000000000000000")
        elif instruction == "READ_D":
            # Display current memory values to the user
            print("Your values stored in memory: \n")
            self.ram.show_memory_status()
            address = input(
                "Enter an address from 0 to 15 to read a value from memory into register D: "
            )

            # Assign the value obtained from memory to register D
            new_value_D = self.ram.read(int(address))
            registerD.set_value(new_value_D)
        elif instruction == "NEGATE_D":
            self.alu.perform_operation(instruction, registerA, registerD)
        elif instruction == "NEGATE_A":
            self.alu.perform_operation(instruction, registerA, registerD)
        elif instruction == "PLUSONE_D":
            self.alu.perform_operation(instruction, registerA, registerD)
        else:
            print(
                "Invalid input. Make sure to enter a valid operation (ADD/SUB/LOAD_D/READ_D/NEGATE_D/NEGATE_A/PLUSONE_D)."
            )

    def get_operation(self):
        """
        Returns the last decoded operation.

        Returns:
        str: The last decoded operation.
        """
        return self.operation
