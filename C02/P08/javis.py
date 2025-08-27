import sys
import os
import csv
import speech_recognition as sr
from pathlib import Path


WAV_FOLDER = r'C:\\Users\\jin_y\\Downloads\\codyssey\\C02\\P07\\records'

class WavTranscriber:
    def __init__(self, folder_path: str):
        self.folder_path = Path(folder_path)
        self.recognizer = sr.Recognizer()

    def find_wav_files(self): #폴더 내 wav 파일 찾기
        wav_files = [f for f in self.folder_path.glob('*.wav')]
        print("=== 발견된 음성 파일 목록 ===")
        for f in wav_files:
            print(f.name)
        return wav_files

    def transcribe(self): #음성인식
        wav_files = self.find_wav_files()
        
        if not wav_files:
            print("🚨 경고: 지정된 폴더에서 .wav 파일을 찾을 수 없습니다.")
            print("         'WAV_FOLDER' 변수의 경로를 확인해 주세요.")
            return

        print("=" * 8 + " 음성 인식 프로세스를 시작합니다. " + "=" * 8)

        for wav_file in wav_files:
            print(f"\n▶️ 파일 처리 중: {wav_file.name}")
            try:
                with sr.AudioFile(str(wav_file)) as source:
                    audio_data = self.recognizer.record(source)
                
                text = self.recognizer.recognize_google(audio_data, language='ko-KR') #STT(음성 → 텍스트 변환)
                print(f"✅ 인식 성공: {text}")
                self.save_to_csv(wav_file, text)
            except sr.UnknownValueError:
                text = "[음성 인식 실패: 오디오를 이해할 수 없습니다.]"
                print(f"❌ 인식 실패: {text}")
                self.save_to_csv(wav_file, text)
            except sr.RequestError as e:
                text = f"[API 오류: {e}]"
                print(f"❌ API 오류: {e}")
                self.save_to_csv(wav_file, text)
            except Exception as e:
                text = f"[알 수 없는 오류: {e}]"
                print(f"❌ 알 수 없는 오류: {e}")
                self.save_to_csv(wav_file, text)

    def save_to_csv(self, file_path: Path, text: str): #csv 저장
        csv_path = file_path.with_suffix('.csv')
        try:
            with open(csv_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["파일명", "음성 인식 결과"])
                writer.writerow([file_path.name, text])
            print(f"✅ 결과가 다음 파일에 저장되었습니다: {csv_path.name}")
        except Exception as e:
            print(f"❌ CSV 파일 저장 실패: {e}")


if __name__ == "__main__":
    transcriber = WavTranscriber(WAV_FOLDER)
    transcriber.transcribe()