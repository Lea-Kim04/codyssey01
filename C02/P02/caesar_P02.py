import sys

sys.path.append('C:\\Users\\jin_y\\Downloads\\codyssey\\C02\\P02\\password.txt')

with open("password.txt", "r", encoding="utf-8") as f:
    password = f.read().strip()

def caesar_cipher_decode(target_text):
    results = []  
    # 모든 shift 해독 결과 출력
    for shift in range(26):
        decoded_text = ""
        for char in target_text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decoded_text += chr((ord(char) - base - shift) % 26 + base)
            else:
                decoded_text += char
        results.append(decoded_text) 
        print(f"[{shift}] {decoded_text}")

    try:
        choice = int(input("\n올바른 해독 결과의 shift 번호를 입력하세요: "))
        if 0 <= choice < 26:
            with open("result.txt", "w", encoding="utf-8") as f:
                f.write(results[choice])
            print(f"\n✅ 선택한 결과가 result.txt에 저장되었습니다! (Shift={choice})")
        else:
            print("❌ 0부터 25 사이의 번호만 입력하세요.")
    except ValueError:
        print("❌ 숫자를 입력해야 합니다.")

if __name__ == "__main__":
    cipher = "Khoor Zruog"
    caesar_cipher_decode(cipher)
