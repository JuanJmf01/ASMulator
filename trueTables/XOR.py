class XorGate:
    @staticmethod
    def perform_xor(input1, input2):
        """
        Performs the XOR operation on two binary digits.

        Args:
        - input1 (str): The first binary digit ('0' or '1').
        - input2 (str): The second binary digit ('0' or '1').

        Raises:
        - ValueError: If inputs are not binary digits.

        Returns:
        str: The result of the XOR operation.
        """
        if input1 not in ["0", "1"] or input2 not in ["0", "1"]:
            raise ValueError("Inputs must be binary digits (0 or 1)")

        if input1 != input2:
            return "1"
        else:
            return "0"
