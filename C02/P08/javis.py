from pathlib import Path
import speech_recognition as sr

class WavTranscriber:
    def __init__(self, folder_path: str):
        self.folder_path = Path(folder_path)
        self.recognizer = sr.Recognizer()
        self.wav_files = []

    def find_lists(self):
        self.wav_files = list(self.folder_path.rglob('*.wav'))
        if not self.wav_files:
            print("No .wav files found. Please check the path.")
        else:
            print("="*8 + "File List" + "="*8)
            for wav_file in self.wav_files:
                print(wav_file.name)
    
    def transcribe(self):
        """Transcribes the found .wav files and prints the results."""
        self.find_wav_files()
        
        if not self.wav_files:
            return

        print("\n" + "="*8 + "Transcription Results" + "="*8)
        for wav_file in self.wav_files:
            try:
                with sr.AudioFile(str(wav_file)) as source:
                    audio_data = self.recognizer.record(source)
                
                text = self.recognizer.recognize_google(audio_data, language='ko-KR')
                print(f"[{wav_file.name}] => {text}")
            except sr.UnknownValueError:
                print(f"[{wav_file.name}] => Could not recognize speech.")
            except sr.RequestError as e:
                print(f"[{wav_file.name}] => STT service error: {e}")


if __name__ == "__main__":
    transcriber = WavTranscriber(r'C:\\Users\\jin_y\\Downloads\\codyssey\\C02\\P07')
    transcriber.transcribe()