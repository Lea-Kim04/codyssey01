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

    def find_wav_files(self):
        wav_files = [f for f in self.folder_path.glob('*.wav')]
        return wav_files

    def save_to_csv(self, file_path: Path, text: str):
        csv_path = file_path.with_suffix('.csv')
        try:
            with open(csv_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["파일명", "음성 인식 결과"])
                writer.writerow([file_path.name, text])
            print(f"✅ 결과가 다음 파일에 저장되었습니다: {csv_path.name}")
        except Exception as e:
            print(f"❌ CSV 파일 저장 실패: {e}")

    def transcribe(self):
        wav_files = self.find_wav_files()
        
        if not wav_files:
            print("🚨 경고: 지정된 폴더에서 .wav 파일을 찾을 수 없습니다.")
            print("         'WAV_FOLDER' 변수의 경로를 확인해 주세요.")
            return

        print("="*25)
        print("음성 인식 프로세스를 시작합니다.")
        print("="*25)

        for wav_file in wav_files:
            print(f"\n▶️ 파일 처리 중: {wav_file.name}")
            try:
                with sr.AudioFile(str(wav_file)) as source:
                    audio_data = self.recognizer.record(source)
                
                text = self.recognizer.recognize_google(audio_data, language='ko-KR')
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

if __name__ == "__main__":
    transcriber = WavTranscriber(WAV_FOLDER)
    transcriber.transcribe()