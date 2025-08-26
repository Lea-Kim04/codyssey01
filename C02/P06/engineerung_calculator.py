import sys
import math
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont 

from calculator import Calculator
from engineering_calculator_05 import Engineering_cal_UI

# 괄호: ( , )
# 메모리: mc, m+, m-, mr
# 기본: AC, +/-, %, ÷, ×, -, +, =, ., 0–9
# 지수/거듭제곱: 2ⁿᵈ, x², x³, xʸ, eˣ, 10ˣ
# 역수/루트: 1/x, ²√x, ³√x, ʸ√x
# 로그: ln, log10
# 팩토리얼: x!
# 삼각함수: sin, cos, tan
# 쌍곡선함수: sinh, cosh, tanh
# 상수: e, π
# 표기: EE
# 단위: Deg (라디안 ↔ 도)
# 난수: Rand

class EngineeringCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.memory = 0.0
        self.is_degree = True  # 기본은 Degree 모드

    def sin(self):  # sin
        try:
            val = float(self.current)
            if self.is_degree:
                val = math.radians(val)
            self.current = str(math.sin(val))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def cos(self):  # cos
        try:
            val = float(self.current)
            if self.is_degree:
                val = math.radians(val)
            self.current = str(math.cos(val))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def tan(self):  # tan
        try:
            val = float(self.current)
            if self.is_degree:
                val = math.radians(val)
            self.current = str(math.tan(val))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    
    def sinh(self):  # sinh
        try:
            self.current = str(math.sinh(float(self.current)))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def cosh(self):  # cosh
        try:
            self.current = str(math.cosh(float(self.current)))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def tanh(self):  # tanh
        try:
            self.current = str(math.tanh(float(self.current)))
        except:
            self.current = "Error"
        return self._format_result(self.current)

    def square(self):  # x²
        try:
            self.current = str(float(self.current) ** 2)
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def cube(self):  # x³
        try:
            self.current = str(float(self.current) ** 3)
        except:
            self.current = "Error"
        return self._format_result(self.current)

    def pi(self):  # π
        self.current = str(math.pi)
        return self._format_result(self.current)

    # --- 메모리 기능 ---
    def memory_clear(self):#mc 
        #보너스 문제) mc = 메모리에 저장된 값을 지우는 역할
        self.memory = 0.0
    def memory_add(self):#m+
        try:
            self.memory += float(self.current)
        except:
            self.current = "Error"
    def memory_subtract(self):#m-
        try:
            self.memory -= float(self.current)
        except:
            self.current = "Error"
    def memory_recall(self):#mr
        self.current = str(self.memory)
        return self._format_result(self.current)
    # --- 기타 거듭제곱/루트 ---
    def power_y(self, y):  # xʸ
        try:
            self.current = str(float(self.current) ** y)
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def exp(self):  # eˣ
        try:
            self.current = str(math.exp(float(self.current)))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def ten_power(self):  # 10ˣ
        try:
            self.current = str(10 ** float(self.current))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def inverse(self):  # 1/x
        try:
            val = float(self.current)
            if val == 0:
                raise ZeroDivisionError
            self.current = str(1 / val)
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def sqrt(self):  # √x
        try:
            val = float(self.current)
            if val < 0:
                raise ValueError
            self.current = str(math.sqrt(val))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def cbrt(self):  # ³√x
        try:
            self.current = str(float(self.current) ** (1/3))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def nth_root(self, n):  # ⁿ√x
        try:
            self.current = str(float(self.current) ** (1/float(n)))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    # --- 로그 ---
    def ln(self):  # ln(x)
        try:
            val = float(self.current)
            if val <= 0:
                raise ValueError
            self.current = str(math.log(val))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    def log10(self):  # log10(x)
        try:
            val = float(self.current)
            if val <= 0:
                raise ValueError
            self.current = str(math.log10(val))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    # --- 팩토리얼 ---
    def factorial(self):  # x!
        try:
            val = int(float(self.current))
            if val < 0:
                raise ValueError
            self.current = str(math.factorial(val))
        except:
            self.current = "Error"
        return self._format_result(self.current)
    # --- 상수 ---
    def e_constant(self):  # e
        self.current = str(math.e)
        return self._format_result(self.current)
    # --- EE (과학적 표기 입력용) ---
    def ee(self, exponent):  # EE
        try:
            val = float(self.current) * (10 ** int(exponent))
            self.current = str(val)
        except:
            self.current = "Error"
        return self._format_result(self.current)
    # --- Deg <-> Rad 변환 ---
    def toggle_deg_rad(self):  # Deg ↔ Rad
        self.is_degree = not self.is_degree
        return "DEG" if self.is_degree else "RAD"
    # --- 난수 ---
    def rand(self):  # Rand
        self.current = str(random.random())
        return self._format_result(self.current)

class Engineering_cal_UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPhone Scientific Calculator")
        self.setGeometry(100, 100, 750, 700)
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
        
#로직 객체를 생성.
        self.calc = EngineeringCalculator() 
        self.display.setText(self.calc.current)
        
        self.main_layout.addWidget(self.display)
        self.main_layout.addLayout(self.grid_layout)

        self.buttons = [
            ('(', 'light-grey'), (')', 'light-grey'), ('mc', 'light-grey'), ('m+', 'light-grey'), ('m-', 'light-grey'), ('mr', 'light-grey'), ('AC', 'light-grey'), ('+/-', 'light-grey'), ('%', 'light-grey'), ('÷', 'orange'),
            ('2ⁿᵈ', 'dark-grey-func'), ('x²', 'dark-grey-func'), ('x³', 'dark-grey-func'), ('xʸ', 'dark-grey-func'), ('eˣ', 'dark-grey-func'), ('10ˣ', 'dark-grey-func'), ('7', 'dark-grey'), ('8', 'dark-grey'), ('9', 'dark-grey'), ('x', 'orange'),
            ('1/x', 'dark-grey-func'), ('²√x', 'dark-grey-func'), ('³√x', 'dark-grey-func'), ('ʸ√x', 'dark-grey-func'), ('ln', 'dark-grey-func'), ('log10', 'dark-grey-func'), ('4', 'dark-grey'), ('5', 'dark-grey'), ('6', 'dark-grey'), ('-', 'orange'),
            ('x!', 'dark-grey-func'), ('sin', 'dark-grey-func'), ('cos', 'dark-grey-func'), ('tan', 'dark-grey-func'), ('e', 'dark-grey-func'), ('EE', 'dark-grey-func'), ('1', 'dark-grey'), ('2', 'dark-grey'), ('3', 'dark-grey'), ('+', 'orange'),
            ('Deg', 'dark-grey-func'), ('sinh', 'dark-grey-func'), ('cosh', 'dark-grey-func'), ('tanh', 'dark-grey-func'), ('π', 'dark-grey-func'), ('Rand', 'dark-grey'), ('0', 'dark-grey'), ('.', 'dark-grey'), ('=', 'orange')
        ]
        self.create_buttons()

    def create_buttons(self):
        row_pos = 0
        col_pos = 0
        button_size = 70

        for button_text, color in self.buttons:
            button = QPushButton(button_text)
            button.setFixedSize(button_size, button_size)

            if color == 'light-grey':
                button.setStyleSheet(f"QPushButton {{ background-color: #D4D4D2; color: black; border-radius: {button_size/2}px; font-size: 25px; }}")
            elif color == 'orange':
                button.setStyleSheet(f"QPushButton {{ background-color: #FF9500; color: white; border-radius: {button_size/2}px; font-size: 25px; }}")
            elif color == 'dark-grey-func':
                button.setStyleSheet(f"QPushButton {{ background-color: #303030; color: white; border-radius: {button_size/2}px; font-size: 25px; }}")
            else:
                button.setStyleSheet(f"QPushButton {{ background-color: #505050; color: white; border-radius: {button_size/2}px; font-size: 25px; }}")

# 버튼 클릭 시 on_button_click 메서드 호출
            button.clicked.connect(lambda _, text=button_text: self.on_button_click(text))

            if button_text == '0':
                self.grid_layout.addWidget(button, row_pos, col_pos, 1, 2)
                button.setFixedSize(QSize(button_size * 2 + 10, button_size))
                col_pos += 2
            else:
                self.grid_layout.addWidget(button, row_pos, col_pos)
                col_pos += 1
            
            if col_pos > 9:
                col_pos = 0
                row_pos += 1

    def on_button_click(self, text):
# 계산기 로직
        result = "" 
# method 호출
        if text.isdigit():
            result = self.calc.input_number(int(text))
        elif text == '.':
            result = self.calc.input_dot()
        elif text == 'AC':
            result = self.calc.reset()
        elif text == '=':
            result = self.calc.equal()
        elif text == '+':
            result = self.calc.add()
        elif text == '-':
            result = self.calc.subtract()
        elif text == 'x':
            result = self.calc.multiply()
        elif text == '÷':
            result = self.calc.divide()
        elif text == '+/-':
            result = self.calc.negative_positive()
        elif text == '%':
            result = self.calc.percent()
        elif text == 'π':
            result = self.calc.pi()
        elif text == 'x²':
            result = self.calc.square()
        elif text == 'x³':
            result = self.calc.cube()
        elif text == 'sin':
            result = self.calc.sin()
        elif text == 'cos':
            result = self.calc.cos()
        elif text == 'tan':
            result = self.calc.tan()
        elif text == 'sinh':
            result = self.calc.sinh()
        elif text == 'cosh':
            result = self.calc.cosh()
        elif text == 'tanh':
            result = self.calc.tanh()
        elif text == 'mc':
            result = self.calc.memory_clear()
        elif text == 'm+':
            result = self.calc.memory_add()
        elif text == 'mr':
            result = self.calc.memory_recall()
        elif text == 'Deg':
            result = self.calc.toggle_mode()
#반환 된 값 디스플레이에 표시
        self.display.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Engineering_cal_UI()
    window.show()
    sys.exit(app.exec_())