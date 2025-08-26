import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont 

class Calculator:
    def __init__(self):
        self.current = ''  
        self.total = 0.0   
        self.operator = '' 
        self.waiting_for_new_operand = True 
        self.has_decimal = False 

        self.reset() 

    def reset(self):
        self.current = '0'
        self.total = 0.0
        self.operator = ''
        self.waiting_for_new_operand = True
        self.has_decimal = False
        return self.current

    def negative_positive(self):
        if self.current and self.current != '0' and self.current != "Error":
            if self.current.startswith('-'):
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
        return self._format_result(self.current)

    def percent(self):
        if self.current and self.current != '0' and self.current != "Error":
            try:
                value = float(self.current) / 100
                self.current = str(value)
            except ValueError:
                self.current = "Error" 
        return self._format_result(self.current)

    def input_number(self, num):
        if self.current == "Error": 
            self.reset()
            self.current = str(num)
            self.waiting_for_new_operand = False
        elif self.waiting_for_new_operand: 
            self.current = str(num)
            self.waiting_for_new_operand = False
            self.has_decimal = False 
        elif self.current == '0' and num != '.': 
            self.current = str(num)
        else: 
            self.current += str(num)
        return self._format_result(self.current)

    def input_dot(self):
        if self.current == "Error": 
            self.reset()
            self.current = '0.'
            self.waiting_for_new_operand = False
            self.has_decimal = True
        elif self.waiting_for_new_operand: 
            self.current = '0.'
            self.waiting_for_new_operand = False
            self.has_decimal = True
        elif '.' not in self.current:
            if not self.current: 
                self.current = '0.'
            else:
                self.current += '.'
            self.has_decimal = True
        return self._format_result(self.current)

    def _set_operator_internal(self, op):
        if self.current == "Error":
            return self.current 
        
        if not self.waiting_for_new_operand:
            self._calculate_intermediate()
            if self.current == "Error": 
                return self.current
        
        self.operator = op 
        self.waiting_for_new_operand = True 
        self.has_decimal = False 
        return self._format_result(self.total) 

    def add(self):
        return self._set_operator_internal('+')

    def subtract(self):
        return self._set_operator_internal('-')

    def multiply(self):
        return self._set_operator_internal('x')

    def divide(self):
        return self._set_operator_internal('÷')

    def equal(self):
        if self.current == "Error":
            return self.current

        self._calculate_intermediate()
        if self.current == "Error": 
            return self.current
            
        self.operator = '' 
        self.waiting_for_new_operand = True 
        self.has_decimal = False 

        result_to_display = self._format_result(self.total)
        self.current = str(self.total) 
        return result_to_display

    def _calculate_intermediate(self):
        if self.current == "Error": 
            self.total = 0.0
            return
            
        if self.current == '': 
            return
        
        try:
            current_float = float(self.current)
            if self.operator == '': 
                self.total = current_float
            else: 
                if self.operator == '+':
                    self.total += current_float
                elif self.operator == '-':
                    self.total -= current_float
                elif self.operator == 'x':
                    self.total *= current_float
                elif self.operator == '÷':
                    if current_float == 0:
                        raise ZeroDivisionError("Cannot divide by zero")
                    self.total /= current_float
            
            self.current = ''
        except (ValueError, ZeroDivisionError, TypeError):
            self.current = "Error" 
            self.total = 0.0
            self.operator = ''
            self.waiting_for_new_operand = True
            self.has_decimal = False

    def _format_result(self, value):
        if value == "Error":
            return "Error"
        
        try:
            val_float = float(value)
            if val_float == int(val_float):
                formatted_val = str(int(val_float))
            else:
                formatted_val = f"{val_float:.10g}" 
            
            if len(formatted_val) > 12: 
                return "Error"
            return formatted_val
        except (ValueError, TypeError):
            return "Error" 

class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator() 
        self.setWindowTitle("iPhone Calculator")
        self.setGeometry(100, 100, 375, 700)
        self.setStyleSheet("background-color: black;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.grid_layout = QGridLayout()
        self.main_layout.addStretch() 

        self.display = QLineEdit()
        self.display.setReadOnly(True) 
        self.display.setAlignment(Qt.AlignRight) 
        self.display.setStyleSheet("font-size: 80px; font-weight: 300; color: white; border: none; background-color: black;")
        self.display.setText(self.calculator.current) 
        self.main_layout.addWidget(self.display)
        self.main_layout.addLayout(self.grid_layout)

        self.buttons = [
            ('AC', 'light-grey'), ('+/-', 'light-grey'), ('%', 'light-grey'), ('÷', 'orange'),
            ('7', 'dark-grey'), ('8', 'dark-grey'), ('9', 'dark-grey'), ('x', 'orange'),
            ('4', 'dark-grey'), ('5', 'dark-grey'), ('6', 'dark-grey'), ('-', 'orange'),
            ('1', 'dark-grey'), ('2', 'dark-grey'), ('3', 'dark-grey'), ('+', 'orange'),
            ('0', 'dark-grey'), ('.', 'dark-grey'), ('=', 'orange')
        ]
        self.create_buttons() 

    def create_buttons(self):
        row = 0
        col = 0
        for button_text, color in self.buttons:
            button = QPushButton(button_text)
            button.setFixedSize(80, 80) 
            
            if color == 'light-grey':
                button.setStyleSheet("QPushButton { background-color: #D4D4D2; color: black; border-radius: 40px; font-size: 30px; }")
            elif color == 'orange':
                button.setStyleSheet("QPushButton { background-color: #FF9500; color: white; border-radius: 40px; font-size: 30px; }")
            else:
                button.setStyleSheet("QPushButton { background-color: #505050; color: white; border-radius: 40px; font-size: 30px; }")

            button.clicked.connect(lambda _, text=button_text: self.on_button_click(text))

            if button_text == '0':
                self.grid_layout.addWidget(button, row, col, 1, 2)
                button.setFixedSize(QSize(170, 80)) 
                col += 2
            else:
                self.grid_layout.addWidget(button, row, col)
                col += 1
            
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, text):
        result = "" 
        if text.isdigit():
            result = self.calculator.input_number(text)
        elif text == '.': 
            result = self.calculator.input_dot()
        elif text == 'AC': 
            result = self.calculator.reset()
        elif text == '+/-': 
            result = self.calculator.negative_positive()
        elif text == '%': 
            result = self.calculator.percent()
        elif text == '+':
            result = self.calculator.add()
        elif text == '-':
            result = self.calculator.subtract()
        elif text == 'x':
            result = self.calculator.multiply()
        elif text == '÷':
            result = self.calculator.divide()
        elif text == '=': 
            result = self.calculator.equal()
        
        self.display.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorUI()
    window.show() 
    sys.exit(app.exec_())