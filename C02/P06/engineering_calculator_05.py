import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont 

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
        self.display.setText("0")
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

            #공학UI
            if color == 'light-grey':
                button.setStyleSheet(f"QPushButton {{ background-color: #D4D4D2; color: black; border-radius: {button_size/2}px; font-size: 25px; }}")
            elif color == 'orange':
                button.setStyleSheet(f"QPushButton {{ background-color: #FF9500; color: white; border-radius: {button_size/2}px; font-size: 25px; }}")
            elif color == 'dark-grey-func':
                button.setStyleSheet(f"QPushButton {{ background-color: #303030; color: white; border-radius: {button_size/2}px; font-size: 25px; }}")
            else:
                button.setStyleSheet(f"QPushButton {{ background-color: #505050; color: white; border-radius: {button_size/2}px; font-size: 25px; }}")

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

    def on_button_click(self, text): #버튼 클릭 시
        current_text = self.display.text()
        
        if current_text == "Error": #초기화
            current_text = "0"

        if text == 'AC':
            self.display.setText("0")
        elif text.isdigit():
            if current_text == "0":
                self.display.setText(text)
            else:
                self.display.setText(current_text + text) #숫자누적
        elif text == '.':
            if '.' not in current_text:
                self.display.setText(current_text + text)
        else:
            self.display.setText(current_text + text) #연산자 누적


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Engineering_cal_UI()
    window.show()
    sys.exit(app.exec_())