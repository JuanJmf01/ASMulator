class RAM:
    def __init__(self, size):
        """
        Initializes RAM with the specified size and sets all memory locations to '0000000000000000'.

        Args:
        - size (int): The size of the RAM.

        Returns:
        None
        """
        self.size = size
        self.memory = ["0000000000000000"] * size

    def write(self, address, data):
        """
        Writes the specified 16-bit binary data to the specified memory address.

        Args:
        - address (int): The memory address to write to.
        - data (str): The 16-bit binary data to write.

        Raises:
        - ValueError: If the address is outside the valid range or if the data is not a 16-bit binary number.

        Returns:
        None
        """
        if address < 0 or address >= self.size:
            raise ValueError("Invalid memory address")
        if len(data) != 16:
            raise ValueError("Data must be a 16-bit binary number")
        self.memory[address] = data

    def read(self, address):
        """
        Reads the 16-bit binary data from the specified memory address.

        Args:
        - address (int): The memory address to read from.

        Raises:
        - ValueError: If the address is outside the valid range.

        Returns:
        str: The 16-bit binary data read from the specified memory address.
        """
        if address < 0 or address >= self.size:
            raise ValueError("Invalid memory address")
        return self.memory[address]

    def show_memory_status(self):
        """
        Displays the current values in all memory positions.

        Returns:
        None
        """
        print("Your values in their respective positions:")
        for address, data in enumerate(self.memory):
            print(f"Address {address}: Value {data}")
