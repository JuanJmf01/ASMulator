class NotGate:
  
    @staticmethod
    def perform_not(input_bit):
        if input_bit not in ['0', '1']:
            raise ValueError("Input must be a binary digit (0 or 1)")

        if input_bit == '0':
            return '1'
        else:
            return '0'