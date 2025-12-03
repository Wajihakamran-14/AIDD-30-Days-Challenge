from src.utils import format_number, handle_division_by_zero, handle_overflow_underflow

class DisplayManager:
    def __init__(self):
        self.current_display = "0"

    def update_display(self, value):
        self.current_display = format_number(value)
        print(f"Result: {self.current_display}")

    def show_error(self, message):
        print(f"Error: {message}")
        self.current_display = "Error"

    def clear_display(self):
        self.current_display = "0"
        print("Display cleared.")

