import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont

class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()
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
        self.display.setText("0")
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
            
            # 버튼 스타일 적용
            if color == 'light-grey':
                button.setStyleSheet("QPushButton { background-color: #D4D4D2; color: black; border-radius: 40px; font-size: 30px; }")
            elif color == 'orange':
                button.setStyleSheet("QPushButton { background-color: #FF9500; color: white; border-radius: 40px; font-size: 30px; }")
            else: # dark-grey
                button.setStyleSheet("QPushButton { background-color: #505050; color: white; border-radius: 40px; font-size: 30px; }")

            # 버튼 클릭 이벤트 연결
            button.clicked.connect(lambda _, text=button_text: self.on_button_click(text))

            # '0' 버튼은 두 칸을 차지하도록 설정
            if button_text == '0':
                self.grid_layout.addWidget(button, row, col, 1, 2)
                button.setFixedSize(QSize(170, 80))
                col += 2
            else:
                self.grid_layout.addWidget(button, row, col)
                col += 1
            
            # 다음 행으로 넘어가는 로직
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, text):
        current_text = self.display.text()
        
        if text.isdigit():
            if current_text == "0":
                self.display.setText(text)
            else:
                self.display.setText(current_text + text)
        elif text == '.':
            if '.' not in current_text:
                self.display.setText(current_text + text)
        elif text == 'AC':
            self.display.setText("0")
        else:
            # 이번 과제에서는 계산 기능은 구현하지 않음
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorUI()
    calculator.show()
    sys.exit(app.exec_())