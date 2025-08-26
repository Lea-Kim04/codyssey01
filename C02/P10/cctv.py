import cv2
from pathlib import Path


class ImageLoader:
    def __init__(self, folder_path: str):
        self.folder_path = Path(folder_path)
        self.image_files = sorted(self.folder_path.glob("*.jpg"))  # JPG만

    def print_names(self):
        for f in self.image_files:
            print(f.name)

class PersonDetector:
    def __init__(self, image_folder): 
        self.image_folder = Path(image_folder)
        self.images = sorted([f for f in self.image_folder.glob('*') if f.suffix.lower() in ['.jpg', '.png', '.jpeg']])
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect_and_draw(self, image): #사각형 표시
        boxes, _ = self.hog.detectMultiScale(image, winStride=(8,8), padding=(8,8), scale=1.05)
        for (x, y, w, h) in boxes:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        return image

    def search_images(self): #사람검출
        for img_path in self.images:
            image = cv2.imread(str(img_path))
            if image is None:
                continue

            image_with_boxes = self.detect_and_draw(image)
            cv2.imshow("Person Detection", image_with_boxes)

            key = cv2.waitKey(0)
            if key == 27:
                break

        cv2.destroyAllWindows()
        print("모든 이미지 검색이 끝났습니다.")

if __name__ == "__main__":
    folder_path = "C:\\Users\\jin_y\\Downloads\\codyssey\\C02\\P09\\CCTV"

    loader = ImageLoader(folder_path) #목록확인
    loader.print_names()

    detector = PersonDetector(folder_path) #사람검출
    detector.search_images()