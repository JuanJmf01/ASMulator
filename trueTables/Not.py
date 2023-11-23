class NotGate:
    @staticmethod
    def perform_not(input_bit):
        """
        Performs the NOT operation on a binary digit.

        Args:
        - input_bit (str): The binary digit ('0' or '1').

        Raises:
        - ValueError: If the input is not a binary digit.

        Returns:
        str: The result of the NOT operation.
        """
        if input_bit not in ["0", "1"]:
            raise ValueError("Input must be a binary digit (0 or 1)")

        if input_bit == "0":
            return "1"
        else:
            return "0"
