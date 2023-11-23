class RegisterD:
    def __init__(self):
        """
        Initializes RegisterD with a default value of '0000000000000000'.

        Returns:
        None
        """
        self.value = "0000000000000000"

    def set_value(self, new_value):
        """
        Sets the value of RegisterD to the specified 16-bit binary number.

        Args:
        - new_value (str): The new 16-bit binary value for RegisterD.

        Raises:
        - ValueError: If the new value is not a 16-bit binary number.

        Returns:
        None
        """
        if len(new_value) != 16:
            raise ValueError("Value must be a 16-bit binary number for RegisterD")

        self.value = new_value

    def get_value(self):
        """
        Returns the current value of RegisterD.

        Returns:
        str: The 16-bit binary value of RegisterD.
        """
        return self.value
