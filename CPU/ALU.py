from trueTables.And import AndGate
from trueTables.Or import OrGate
from trueTables.XOR import XorGate
from trueTables.Not import NotGate


class ALU:
    def perform_operation(self, operation, registerA, registerD):
        """
        Performs the specified ALU operation on the given registers.

        Args:
        - operation (str): The operation to be performed ("ADD", "SUB", "NEGATE_D", "NEGATE_A", "PLUSONE_D").
        - registerA (Register): The register containing operand A.
        - registerD (Register): The register containing operand D.

        Raises:
        - ValueError: If an unsupported operation is provided.

        Returns:
        None
        """
        input1 = registerA.get_value()
        input2 = registerD.get_value()

        if operation == "ADD":
            registerD.set_value(self.add(input1, input2))
        elif operation == "SUB":
            registerD.set_value(self.subtract(input2, input1))
        elif operation == "NEGATE_D":
            registerD.set_value(self.negate(input2))
        elif operation == "NEGATE_A":
            registerA.set_value(self.negate(input1))
        elif operation == "PLUSONE_D":
            registerD.set_value(self.plusOne(input2))
        else:
            raise ValueError("Unsupported operation")

    def add(self, input1, input2):
        """
        Performs binary addition on two 16-bit binary numbers.

        Args:
        - input1 (str): The first 16-bit binary number.
        - input2 (str): The second 16-bit binary number.

        Raises:
        - ValueError: If inputs are not 16-bit binary numbers.

        Returns:
        str: The result of the binary addition.
        """
        if len(input1) != 16 or len(input2) != 16:
            raise ValueError("Inputs must be 16-bit binary numbers")

        sum_result = ""
        carry = "0"

        for i in range(15, -1, -1):
            bit_input1 = input1[i]
            bit_input2 = input2[i]

            # Perform bit-wise addition using XOR and AND logic gates for carry
            bit_sum = XorGate.perform_xor(bit_input1, bit_input2)
            current_bit_result = XorGate.perform_xor(bit_sum, carry)

            # Calculate carry for the next bit
            carry = OrGate.perform_or(
                AndGate.perform_and(bit_sum, carry),
                AndGate.perform_and(bit_input1, bit_input2),
            )

            # Build the result bit by bit
            sum_result = current_bit_result + sum_result

        return sum_result

    def subtract(self, input1, input2):
        """
        Performs binary subtraction on two 16-bit binary numbers.

        Args:
        - input1 (str): The first 16-bit binary number.
        - input2 (str): The second 16-bit binary number.

        Raises:
        - ValueError: If inputs are not 16-bit binary numbers.

        Returns:
        str: The result of the binary subtraction.
        """
        if len(input1) != 16 or len(input2) != 16:
            raise ValueError("Inputs must be 16-bit binary numbers")

        # Invert the second number (using the NOT operation)
        inverted_input2 = "".join([NotGate.perform_not(bit) for bit in input2])

        # Sum the first number with the inverted representation of the second number
        # This is equivalent to subtraction, as input1 + (-input2) is the same as input1 - input2
        temp_result = self.add(input1, inverted_input2)

        # Add 1 to the result to account for the sign bit
        one = "0000000000000001"
        final_result = self.add(temp_result, one)

        return final_result[-16:]

    def negate(self, input):
        """
        Negates a 16-bit binary number.

        Args:
        - input (str): The 16-bit binary number to be negated.

        Returns:
        str: The result of the binary negation.
        """
        # Invert each bit of input using the NOT operation
        inverted = "".join([NotGate.perform_not(bit) for bit in input])

        # Return the result of the negation
        return inverted

    def plusOne(self, input2):
        """
        Adds one to a 16-bit binary number.

        Args:
        - input2 (str): The 16-bit binary number.

        Returns:
        str: The result of adding one to the input number.
        """
        one = "0000000000000001"
        resultPlus1 = self.add(input2, one)
        return resultPlus1
