import cv2              # 영상 처리
import numpy as np      # 색상 범위 설정

cap = cv2.VideoCapture(0)  # 카메라 연결

# 색상 범위
# Red
lower_red1 = np.array([0, 120, 70])      # 빨강 하한값(첫 번째 구간)
upper_red1 = np.array([10, 255, 255])    # 빨강 상한값(첫 번째 구간)
lower_red2 = np.array([170, 120, 70])    # 빨강 하한값(두 번째 구간)
upper_red2 = np.array([180, 255, 255])   # 빨강 상한값(두 번째 구간)

# Green
lower_green = np.array([40, 40, 40])     # 초록 하한값
upper_green = np.array([70, 255, 255])   # 초록 상한값

# Blue
lower_blue = np.array([100, 150, 0])     # 파랑 하한값
upper_blue = np.array([140, 255, 255])   # 파랑 상한값

# 실시간 색상 추적
while True:  
    ret, frame = cap.read()  # 카메라에서 한 프레임 읽기
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # BGR 이미지 → HSV 색공간 변환

    # Red mask
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)  # 첫 번째 빨강 구간 마스크
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)  # 두 번째 빨강 구간 마스크
    mask_red = mask_red1 | mask_red2                       # 두 구간 합쳐서 최종 빨강 마스크

    # Green mask
    mask_green = cv2.inRange(hsv, lower_green, upper_green)  # 초록 색 범위 마스크

    # Blue mask
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)     # 파랑 색 범위 마스크

    # --- 전체 마스크 합치기 ---
    mask = mask_red | mask_green | mask_blue  # 빨강, 초록, 파랑 마스크 합치기

    # --- 색상 추적 결과 이미지 만들기 ---
    result = cv2.bitwise_and(frame, frame, mask=mask)  # 마스크된 부분만 원본에서 추출

    # --- 조건문으로 색상 감지 ---
    color_name = "None"  # 기본값: 감지된 색 없음
    if cv2.countNonZero(mask_red) > 500:   # 빨강 픽셀이 일정 개수 이상이면
        color_name = "Red"                  # 색상 이름 "Red"로 설정
    elif cv2.countNonZero(mask_green) > 500:  # 초록 픽셀 수가 일정 이상이면
        color_name = "Green"                   # 색상 이름 "Green"으로 설정
    elif cv2.countNonZero(mask_blue) > 500:   # 파랑 픽셀 수가 일정 이상이면
        color_name = "Blue"                    # 색상 이름 "Blue"로 설정

    # --- 영상에 감지된 색상 이름 표시 ---
    cv2.putText(result, f"Detected: {color_name}", (10, 50),      # 위치 (x=10, y=50)
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)  # 글꼴, 크기, 색상, 두께

    # --- 영상 출력 ---
    cv2.imshow("Original", frame)         # 원본 영상 출력
    cv2.imshow("Color Tracking", result)  # 색상 추적 결과 영상 출력

    # --- 종료 조건 ---
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 반복문 종료
        break

# --- 자원 해제 ---
cap.release()             # 카메라 해제
cv2.destroyAllWindows()   # 모든 OpenCV 창 닫기
