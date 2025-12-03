import re

class InputParser:
    def __init__(self):
        self.history = []

    def parse(self, user_input):
        if user_input.lower() == 'clear':
            return ['clear']
        if user_input.lower() == 'ce':
            return ['ce']

        # Tokenize the input, supporting numbers (int/float) and operators
        tokens = re.findall(r'\d+\.?\d*|[+\-*/()]|', user_input)
        # Clean up tokens: remove empty strings and strip whitespace
        tokens = [token.strip() for token in tokens if token.strip()]

        if not tokens: # Handle empty input after stripping
            return []

        self.history.append(user_input)
        return tokens
