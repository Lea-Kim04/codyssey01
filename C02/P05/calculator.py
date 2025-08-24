import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont # QFont는 여기서는 사용되지 않지만, 폰트 설정을 위해 가져올 수 있습니다.

class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPhone Scientific Calculator")
        # 가로 모드 아이폰 계산기처럼 너비를 넓게 설정합니다.
        self.setGeometry(100, 100, 750, 700) # 가로 750px, 세로 700px
        self.setStyleSheet("background-color: black;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.grid_layout = QGridLayout()
        self.main_layout.addStretch() # 화면 상단에 여백 추가 (아이폰 계산기 레이아웃 유사하게)

        self.display = QLineEdit()
        self.display.setReadOnly(True) # 읽기 전용
        self.display.setAlignment(Qt.AlignRight) # 오른쪽 정렬
        # 아이폰 계산기 스타일 폰트 및 크기, 색상
        self.display.setStyleSheet("font-size: 80px; font-weight: 300; color: white; border: none; background-color: black;")
        self.display.setText("0") # 초기 화면 값을 '0'으로 설정
        self.main_layout.addWidget(self.display)
        self.main_layout.addLayout(self.grid_layout)

        # 공학용 계산기 버튼 배치 (5행 10열에 맞춰서 정의)
        # 아이폰 계산기의 일반적인 버튼들을 최대한 반영했습니다.
        self.buttons = [

            # Row 0
            ('(', 'light-grey'), (')', 'light-grey'), ('mc', 'light-grey'), ('m+', 'light-grey'), ('m-', 'light-grey'), ('mr', 'light-grey'), ('AC', 'light-grey'), ('+/-', 'light-grey'), ('%', 'light-grey'), ('÷', 'orange'),
            # Row 1
            ('2ⁿᵈ', 'dark-grey-func'), ('x²', 'dark-grey-func'), ('x³', 'dark-grey-func'), ('xʸ', 'dark-grey-func'), ('eˣ', 'dark-grey-func'), ('10ˣ', 'dark-grey-func'), ('7', 'dark-grey'), ('8', 'dark-grey'), ('9', 'dark-grey'), ('x', 'orange'),
            # Row 2
            ('1/x', 'dark-grey-func'), ('∛x', 'dark-grey-func'), ('²√x', 'dark-grey-func'), ('ʸ√x', 'dark-grey-func'), ('ln', 'dark-grey-func'), ('log₁₀', 'dark-grey-func'), ('4', 'dark-grey'), ('5', 'dark-grey'), ('6', 'dark-grey'), ('-', 'orange'),
            # Row 3
            ('x!', 'dark-grey-func'), ('sin', 'dark-grey-func'), ('cos', 'dark-grey-func'), ('tan', 'dark-grey-func'), ('e', 'dark-grey-func'), ('EE', 'dark-grey-func'), ('1', 'dark-grey'), ('2', 'dark-grey'), ('3', 'dark-grey'), ('+', 'orange'),
            # Row 4 (0 버튼은 2칸 차지, 나머지 1칸씩)
            ('Deg', 'dark-grey-func'), ('sinh', 'dark-grey-func'), ('cosh', 'dark-grey-func'), ('tanh', 'dark-grey-func'), ('π', 'dark-grey-func'), ('Rand', 'dark-grey'), ('0', 'dark-grey'), ('.', 'dark-grey'), ('=', 'orange')
        ]
        self.create_buttons() # 버튼 생성 및 배치

    def create_buttons(self):
        """버튼을 생성하고 GridLayout에 배치합니다."""
        row_pos = 0
        col_pos = 0
        # 버튼의 기본 크기
        button_size = 70 # 아이폰 가로 모드에 맞춰 버튼 크기 조정

        for button_text, color in self.buttons:
            button = QPushButton(button_text)
            button.setFixedSize(button_size, button_size) # 버튼 고정 크기
            
            # 버튼 스타일에 따라 색상 및 폰트 적용
            if color == 'light-grey':
                button.setStyleSheet(f"QPushButton {{ background-color: #D4D4D2; color: black; border-radius: {button_size/2}px; font-size: 25px; }}")
            elif color == 'orange':
                button.setStyleSheet(f"QPushButton {{ background-color: #FF9500; color: white; border-radius: {button_size/2}px; font-size: 25px; }}")
            elif color == 'dark-grey-func': # 공학용 함수 버튼 색상 (어두운 회색)
                button.setStyleSheet(f"QPushButton {{ background-color: #303030; color: white; border-radius: {button_size/2}px; font-size: 25px; }}")
            else: # dark-grey (기본 숫자 버튼)
                button.setStyleSheet(f"QPushButton {{ background-color: #505050; color: white; border-radius: {button_size/2}px; font-size: 25px; }}")

            # 버튼 클릭 이벤트 연결: on_button_click 메소드 호출
            button.clicked.connect(lambda _, text=button_text: self.on_button_click(text))

            # '0' 버튼은 가로로 2칸을 차지하도록 특별 처리
            if button_text == '0':
                self.grid_layout.addWidget(button, row_pos, col_pos, 1, 2)
                button.setFixedSize(QSize(button_size * 2 + 10, button_size)) # 가로 2칸에 맞는 크기 (10은 간격)
                col_pos += 2
            else:
                self.grid_layout.addWidget(button, row_pos, col_pos)
                col_pos += 1
            
            # 10개 열을 채우면 다음 행으로 이동
            if col_pos > 9:
                col_pos = 0
                row_pos += 1

    def on_button_click(self, text):
        """버튼 클릭 이벤트 발생 시 호출되는 메소드입니다.
        이번 과제에서는 계산 기능은 구현하지 않고, 단순히 화면에 텍스트를 표시합니다."""
        current_text = self.display.text()
        
        if text == 'AC': # 'AC' 버튼은 화면을 '0'으로 초기화
            self.display.setText("0")
        elif text.isdigit(): # 숫자 버튼
            if current_text == "0" or current_text == "Error": # '0'이거나 에러 상태이면 숫자로 교체
                self.display.setText(text)
            else: # 기존 숫자에 이어서 숫자 추가
                self.display.setText(current_text + text)
        elif text == '.': # 소수점 버튼
            if '.' not in current_text: # 현재 숫자에 소수점이 없으면 추가
                self.display.setText(current_text + text)
        else: # 그 외 모든 연산자 및 공학용 함수 버튼 (x, ÷, +, -, sin, cos 등)
            # 현재 텍스트가 '0'이거나 에러 상태이면 버튼 텍스트로 교체
            # 아니면 기존 텍스트에 이어서 버튼 텍스트 추가
            if current_text == "0" or current_text == "Error":
                self.display.setText(text)
            else:
                self.display.setText(current_text + text)


# ===== 프로그램 실행 =====
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorUI()
    window.show() # 계산기 창 표시
    sys.exit(app.exec_()) # 이벤트 루프 시작