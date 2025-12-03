import sys
sys.path.append('.')
from src.input_parser import InputParser
from src.calculator_core import CalculatorCore
from src.display_manager import DisplayManager

def main():
    print("Simple Calculator App")
    parser = InputParser()
    calculator = CalculatorCore()
    display = DisplayManager()

    while True:
        try:
            user_input = input("Enter expression (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break

            tokens = parser.parse(user_input)

            if not tokens:
                continue

            if tokens[0] == 'clear':
                calculator.calculate(['clear'])
                display.clear_display()
                continue
            if tokens[0] == 'ce':
                calculator.calculate(['ce'])
                display.clear_display() # Display cleared message or current state
                continue

            result = calculator.calculate(tokens)
            display.update_display(result)

        except ValueError as e:
            display.show_error(str(e))
        except EOFError:
            break
        except Exception as e:
            display.show_error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
