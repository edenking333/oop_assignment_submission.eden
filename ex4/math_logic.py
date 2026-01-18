class MathLogic:
    def is_multiple(self, num1: int, num2: int) -> bool:
        if num1 == 0 or num2 == 0:
            return False
        return (num1 % num2 == 0) or (num2 % num1 == 0)