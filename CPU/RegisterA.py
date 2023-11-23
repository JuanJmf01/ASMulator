class RegisterA:
    def __init__(self):
        """
        Initializes RegisterA with a default value of '0000000000000000'.

        Returns:
        None
        """
        self.value = "0000000000000000"

    def set_value(self, new_value):
        """
        Sets the value of RegisterA to the specified 16-bit binary number.

        Args:
        - new_value (str): The new 16-bit binary value for RegisterA.

        Raises:
        - ValueError: If the new value is not a 16-bit binary number.

        Returns:
        None
        """
        if len(new_value) != 16:
            raise ValueError("Value must be a 16-bit binary number for RegisterA")

        self.value = new_value

    def get_value(self):
        """
        Returns the current value of RegisterA.

        Returns:
        str: The 16-bit binary value of RegisterA.
        """
        return self.value
