from trueTables.And import And
from trueTables.Or import Or
from trueTables.Not import Not


class XOR:
    def __init__(self):
        self.and_gate = And() 
        self.or_gate = Or()
        self.not_gate = Not()

    def execute(self, a, b):

        not_a = self.not_gate.execute(a)
        not_b = self.not_gate.execute(b)

        ab_and = self.and_gate.execute(a, not_b)
        not_a_b_and = self.and_gate.execute(not_a, b)

        xor_result = self.or_gate.execute(ab_and, not_a_b_and)
        return xor_result
