class Mux16:
    def execute(self, input1, input2, sel):
        """
        Executes a 16-to-1 multiplexer operation.

        Args:
        - input1 (int): The first 16-bit input.
        - input2 (int): The second 16-bit input.
        - sel (int): The 4-bit selection input.

        Returns:
        int: The result of the multiplexer operation.
        """
        output = 0  # Initialize the output

        for i in range(16):
            if (sel >> i) & 1 == 0:
                output |= (input1 >> i) & 1 << i  # Use bits from input1
            else:
                output |= (input2 >> i) & 1 << i  # Use bits from input2

        return output
