class AndGate:
    @staticmethod
    def perform_and(input1, input2):
        """
        Performs the AND operation on two binary digits.

        Args:
        - input1 (str): The first binary digit ('0' or '1').
        - input2 (str): The second binary digit ('0' or '1').

        Raises:
        - ValueError: If inputs are not binary digits.

        Returns:
        str: The result of the AND operation.
        """
        if input1 not in ["0", "1"] or input2 not in ["0", "1"]:
            raise ValueError("Inputs must be binary digits (0 or 1)")

        if input1 == "1" and input2 == "1":
            return "1"
        else:
            return "0"
