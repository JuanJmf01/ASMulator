class RegisterD:

    def __init__(self):
        self.value = '0000000000000000'

    def set_value(self, new_value):
        if len(new_value) != 16:
            raise ValueError("Value must be a 16-bit binary number RegisterD")
        
        self.value = new_value

    def get_value(self):
        return self.value