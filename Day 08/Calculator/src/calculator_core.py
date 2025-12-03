class CalculatorCore:
    def __init__(self):
        self.result = 0
        self.history = []

    def calculate(self, tokens):
        if not tokens:
            return 0

        if tokens == ['clear']:
            self.result = 0
            self.history = []
            return 0
        if tokens == ['ce']:
            self.result = 0
            # More sophisticated CE logic would involve clearing the last entered number/operand,
            # but for this basic implementation, we'll reset the result.
            return 0

        # Simple calculation logic for now, without full Shunting-yard or RPN
        # This will be expanded in later tasks to handle order of operations
        try:
            expression = " ".join(tokens)
            # Basic evaluation, will be replaced by proper parser/evaluator
            self.result = eval(expression)
            self.history.append(f"{expression} = {self.result}")
            return self.result
        except ZeroDivisionError:
            raise ValueError("Error: Division by zero")
        except Exception as e:
            raise ValueError(f"Error in calculation: {e}")

