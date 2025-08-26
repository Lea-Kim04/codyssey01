import zipfile
from pathlib import Path
import cv2

class MasImageHelper: 
    def __init__(self, zip_path: str, extract_folder_name: str = "CCTV"):
        self.zip_path = Path('C:\\Users\\jin_y\\Downloads\\codyssey\\C02\\P09\\cctv.zip')
        self.extract_folder = self.zip_path.parent / extract_folder_name
        self.image_files = []
        self.index = 0

        self._extract_zip() # ZIP 압축 해제
        self._load_images() # 목록 load

    def _extract_zip(self):
        try:
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.extract_folder)
            print(f"압축 해제 완료! '{self.extract_folder}' 폴더에 파일이 저장되었습니다.")
        except Exception as e:
            print(f"압축 해제 실패: {e}")

    def _load_images(self):
        try:
            self.image_files = sorted(
                list(self.extract_folder.glob("*.jpg")) + list(self.extract_folder.glob("*.png"))
            )
        except Exception as e:
            self.image_files = []
            print(f"이미지 로드 실패: {e}")

    def show_viewer(self):
        if not self.image_files:
            return
        while True:
            img = cv2.imread(str(self.image_files[self.index]))
            if img is None:
                self.index = (self.index + 1) % len(self.image_files)
                continue

            cv2.imshow("CCTV Viewer", img)

            key = cv2.waitKeyEx(0)

            if key == 27:  # ESC → 종료
                break
            elif key == 2424832:  # 왼쪽 방향키
                self.index = (self.index - 1) % len(self.image_files)
            elif key == 2555904:  # 오른쪽 방향키
                self.index = (self.index + 1) % len(self.image_files)

        cv2.destroyAllWindows()

    def get_current_image_path(self):
        if not self.image_files:
            return None
        return self.image_files[self.index]

    def get_all_image_paths(self):
        return self.image_files or []


if __name__ == "__main__":
    helper = MasImageHelper(r"C:\\Users\\jin_y\Downloads\\CCTV.zip")
    helper.show_viewer()
