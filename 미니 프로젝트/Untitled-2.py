import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
# QLabel: 문제 표시
# QLineEdit: 사용자 입력
# QPushButton + Signal & Slot: 클릭 시 답 체크
# QMessageBox: 정답/오답 알림
from datetime import datetime

# 문제 리스트
problems = [
    {"question": "세상에서 가장 빠른 닭은?", "answer": "후다닥"},
    {"question": "병아리가 가장 잘 먹는 약은?", "answer": "삐약"},
    {"question": "왕이 넘어지면?", "answer": "킹콩"},
    {"question": "왕이 외출할 때 타는 차?", "answer": "킹카"},
    {"question": "7 * 8 = ?", "answer": "56"}  
]

score = 0
current_index = 0

def check_answer():
    global score, current_index #점수, 몇 번째 문제인지 (함수 안에서 값을 바꿔야 하므로 global로 선언.)
    user_answer = answer_input.text().strip()
    
    if user_answer == problems[current_index]["answer"]:
        QMessageBox.information(window, "결과", "정답! 🎉")
        score += 1
    else:
        QMessageBox.warning(window, "결과", f"틀렸습니다 😢 정답: {problems[current_index]['answer']}")
    
    current_index += 1
    if current_index < len(problems): 
        problem_label.setText(problems[current_index]["question"]) # 문제 라벨(problem_label)에 다음 문제의 질문 표시.
        answer_input.clear() #입력 창 비움
    else:
        QMessageBox.information(window, "퀴즈 종료", f"퀴즈가 끝났습니다! 점수: {score}/{len(problems)}")
        save_score()  # 점수 파일 저장
        window.close()

def save_score():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 현재 날짜와 시간
    with open("scores.txt", "a") as f:
        f.write(f"[{now}] 점수: {score}/{len(problems)}\n")
        
# 앱과 최상위 창 만들기
app = QApplication(sys.argv) # PyQt 앱 엔진(이벤트 루프)을 한 번만 만드는 줄
window = QWidget() # 최상위 창
window.setWindowTitle("퀴즈 프로그램")
window.setGeometry(100, 100, 400, 200) # x, y, 가로, 세로

# 위젯(라벨/입력/버튼) 배치
problem_label = QLabel(problems[current_index]["question"], window) # 텍스트 표시 위젯
problem_label.move(20, 20) # 창 내부 좌표(왼쪽 위 모서리)

answer_input = QLineEdit(window) # 한 줄 입력
answer_input.move(20, 60) # 좌표 지정
answer_input.resize(200, 30) # 크기를 직접 지정

submit_button = QPushButton("제출", window) # 클릭 가능한 버튼
submit_button.move(240, 60)
submit_button.clicked.connect(check_answer) # 시그널-슬롯 연결: 버튼 클릭

# 화면 표시 + 이벤트 루프
window.show() # 창을 화면에 나타내는 호출
sys.exit(app.exec_()) # 종료








