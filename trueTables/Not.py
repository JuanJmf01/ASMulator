from trueTables.And import And

class Not:
    def __init__(self):
        self.and_gate = And() 

    def execute(self, input1):
        return self.and_gate.execute(~input1, 0xFFFF)  

