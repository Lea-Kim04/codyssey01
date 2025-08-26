import cv2
from pathlib import Path
from ultralytics import YOLO # YOLOv8 모델을 사용하기 위한 라이브러리

class ImageLoader:
    def __init__(self, folder_path: str):
        self.folder_path = Path(folder_path)
        # 이미지 파일 확장자 목록을 추가하여 JPG 외 다른 형식도 로드
        self.image_files = sorted([
            f for f in self.folder_path.glob('*') 
            if f.suffix.lower() in ['.jpg', '.png', '.jpeg', '.bmp']
        ])
        if not self.image_files:
            print(f"경로 {folder_path}에 이미지 파일이 없습니다. 경로를 확인하세요.")

    def print_names(self):
        if not self.image_files:
            return
        print("=="*8 + "이미지 파일 목록" + "=="*8)
        for f in self.image_files:
            print(f.name)

class PersonDetector:
    def __init__(self, image_folder: str):
        self.image_folder = Path(image_folder)
        self.images = sorted([
            f for f in self.image_folder.glob('*') 
            if f.suffix.lower() in ['.jpg', '.png', '.jpeg', '.bmp']
        ])
        
        # YOLOv8 모델 로드
        # 'yolov8n.pt'는 YOLOv8의 가장 작은(nano) 모델입니다.
        # 더 큰 모델(yolov8s.pt, yolov8m.pt 등)은 정확도는 높지만 속도가 느려질 수 있습니다.
        self.model = YOLO('yolov8n.pt') 

        # YOLO 모델이 인식하는 클래스 이름을 가져옵니다.
        # 'person' 클래스의 인덱스를 찾아두면 나중에 검출 결과를 필터링하기 쉽습니다.
        self.person_class_id = None
        if 'person' in self.model.names:
            self.person_class_id = list(self.model.names.keys())[list(self.model.names.values()).index('person')]
        
        if self.person_class_id is None:
            print("경고: YOLOv8 모델에 'person' 클래스가 없습니다. 사람이 인식되지 않을 수 있습니다.")


    def detect_and_draw(self, image):
        """
        이미지에서 사람을 검출하고 빨간 사각형을 표시합니다.
        YOLOv8 모델을 사용하여 정확도를 높입니다.
        """
        # YOLO 모델로 객체 검출 실행
        # conf=0.5: 50% 이상의 확신을 가진 객체만 검출
        # classes=[self.person_class_id]: 'person' 클래스만 필터링
        results = self.model(image, conf=0.5, classes=self.person_class_id, verbose=False)
        
        # 검출된 각 객체에 대해 바운딩 박스 그리기
        for r in results:
            # detections는 Detection 객체 리스트를 포함합니다.
            # xyxy: [x1, y1, x2, y2] 형식의 바운딩 박스 좌표
            # conf: 검출된 객체의 확신도
            # cls: 검출된 객체의 클래스 ID (여기서는 'person'만 필터링했으므로 대부분 person)
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0]) # 좌표를 정수로 변환
                confidence = box.conf[0] # 확신도
                class_id = int(box.cls[0]) # 클래스 ID

                # 'person' 클래스이고, 충분히 높은 확신도일 때만 그리기
                if self.person_class_id is not None and class_id == self.person_class_id:
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2) # 빨간색 사각형
                    # 검출된 객체 위에 클래스 이름과 확신도 표시
                    label = f"{self.model.names[class_id]}: {confidence:.2f}"
                    cv2.putText(image, label, (x1, y1 - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # 초록색 텍스트
        return image

    def search_images(self):
        """폴더 내 이미지를 순차적으로 검색하고 사람 검출 후 화면 출력"""
        if not self.images:
            print("검출할 이미지가 없습니다.")
            return

        print("\n" + "=="*8 + "사람 검출 시작" + "=="*8)
        print("엔터(또는 아무 키)를 누르면 다음 이미지로 넘어갑니다. ESC를 누르면 종료됩니다.")
        
        for img_path in self.images:
            image = cv2.imread(str(img_path))
            if image is None:
                print(f"경고: {img_path.name} 이미지를 로드할 수 없습니다. 건너뜁니다.")
                continue

            # 원본 이미지 크기 출력
            # print(f"처리 중인 이미지: {img_path.name}, 크기: {image.shape[1]}x{image.shape[0]}")

            image_with_boxes = self.detect_and_draw(image.copy()) # 원본 이미지 훼손 방지를 위해 .copy() 사용
            
            # 윈도우 크기 조절 (선택 사항)
            # 너무 큰 이미지는 화면에 다 안 들어올 수 있으므로, 적절히 조절
            # display_height = 720
            # if image_with_boxes.shape[0] > display_height:
            #     scale = display_height / image_with_boxes.shape[0]
            #     image_with_boxes = cv2.resize(image_with_boxes, (int(image_with_boxes.shape[1] * scale), display_height))

            cv2.imshow("Person Detection (YOLOv8)", image_with_boxes)

            # 키 입력 대기 (ESC = 종료)
            key = cv2.waitKey(0) # 0은 무한정 대기. 아무 키나 누르면 다음으로.
            if key == 27: # ESC 키
                break

        cv2.destroyAllWindows()
        print("\n모든 이미지 검색이 끝났습니다.")


if __name__ == "__main__":
    # TODO: 여기에 실제 이미지 폴더 경로를 정의해주세요.
    # 예시:
    # folder_path = "C:\\Users\\jin_y\\Downloads\\codyssey\\C02\\P09\\CCTV"
    # 또는 누워있는 우주인 이미지가 있는 폴더 경로
    folder_path = "C:\\Users\\jin_y\\Downloads\\codyssey\\C02\\P09\\CCTV" # 실제 경로로 변경 필요!

    # 이미지 파일 목록 확인
    loader = ImageLoader(folder_path)
    loader.print_names()

    # 사람 검출 실행 (YOLOv8 사용)
    detector = PersonDetector(folder_path)
    detector.search_images()