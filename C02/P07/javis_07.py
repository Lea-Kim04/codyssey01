import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("C:\\Users\\jin_y\\Downloads\\codyssey\\C02\\P07").resolve()
RECORD_DIR = BASE_DIR / "records"
RECORD_DIR.mkdir(exist_ok=True)


def record_audio(seconds=10, fs=44100): #녹음
    print("start recording...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()
    print("recording complete")

    #파일 명 설정 (년월일 - 시간분초)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = RECORD_DIR / f"{timestamp}.wav"
    #저장
    write(str(filename), fs, recording)
    print(f"저장 완료: {filename}")
    return filename

def list_records(start_date=None, end_date=None): #리스트 누적
    files = sorted(RECORD_DIR.glob("*.wav"))
    filtered = []
    #보너스 - 날짜 필터링
    s_date = datetime.strptime(start_date, "%Y%m%d").date() if start_date else None
    e_date = datetime.strptime(end_date, "%Y%m%d").date() if end_date else None

    for file in files:
        date_str = file.stem.split("-")[0]#YYYYMMDD
        file_date = datetime.strptime(date_str, "%Y%m%d").date()

        if (not s_date or file_date >= s_date) and (not e_date or file_date <= e_date):
            filtered.append(file)

    print("==== 녹음 파일 목록 ====")
    for f in filtered:
        print(f.name)
    return filtered

if __name__ == "__main__":
    new_file = record_audio(5) #예시 5초

    start = input("시작 날짜 입력 (YYYYMMDD, 없으면 엔터): ").strip() or None
    end = input("끝 날짜 입력 (YYYYMMDD, 없으면 엔터): ").strip() or None

    if not start and not end:
        # 엔터만 눌렀을 때 → 새로 저장된 파일 출력
        print("\n=== 새로 저장된 녹음 파일 ===")
        print(new_file.name)
    else:
        # 기간 입력 → 기간 내 파일 출력
        list_records(start, end)
print("파이썬 파일 폴더:", BASE_DIR)
print("records 폴더 경로:", RECORD_DIR)
