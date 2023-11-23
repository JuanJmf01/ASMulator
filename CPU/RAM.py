class RAM:
    def __init__(self, size):
        self.size = size
        self.memory = ['0000000000000000'] * size

    def write(self, address, data):
        if address < 0 or address >= self.size:
            raise ValueError("Invalid memory address")
        if len(data) != 16:
            raise ValueError("Data must be a 16-bit binary number")
        self.memory[address] = data

    def read(self, address):
        if address < 0 or address >= self.size:
            raise ValueError("Invalid memory address")
        return self.memory[address]
    
    def show_memory_status(self):
        print("Tus valores en sus respectivas posiciones:")
        for address, data in enumerate(self.memory):
            print(f"Dirección {address}: Valor {data}")