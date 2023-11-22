class AndGate:

    @staticmethod
    def perform_and(input1, input2):
        if input1 not in ['0', '1'] or input2 not in ['0', '1']:
            raise ValueError("Inputs must be binary digits (0 or 1)")

        if input1 == '1' and input2 == '1':
            return '1'
        else:
            return '0'
