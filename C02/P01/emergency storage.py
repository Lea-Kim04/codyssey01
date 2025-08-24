# door_hacking.py
import zipfile
import itertools
import string
import time
from multiprocessing import Pool, cpu_count
from datetime import datetime

zip_filename = r"C:\Users\jin_y\Downloads\codyssey\C02\P01\emergency_storage_key.zip"

chars = string.ascii_lowercase + string.digits
max_length = 6

def try_password(password):
    """ZIP 파일에 암호 시도"""
    try:
        with zipfile.ZipFile(zip_filename) as zf:
            zf.extractall(pwd=password.encode('utf-8'))
        return password
    except:
        return None

def generate_passwords():
    """모든 6자리 조합 생성"""
    for combo in itertools.product(chars, repeat=max_length):
        yield ''.join(combo)

def unlock_zip():
    """ZIP 암호 브루트포스, 진행 상황 출력, password.txt 저장"""
    start_time = time.time()
    print(f"[{datetime.now()}] 암호 찾기 시작")
    
    attempt_count = 0
    found = None
    chunksize = 10000  # 한 번에 처리하는 암호 수, 성능과 출력 빈도 조절

    with Pool(processes=cpu_count()) as pool:
        for result in pool.imap_unordered(try_password, generate_passwords(), chunksize=chunksize):
            attempt_count += 1
            # 1000회마다 진행 상황 출력
            if attempt_count % 1000 == 0:
                elapsed = time.time() - start_time
                print(f"[{datetime.now()}] 시도 횟수: {attempt_count}, 경과 시간: {elapsed:.2f}초")
            
            if result:
                found = result
                elapsed = time.time() - start_time
                print(f"[{datetime.now()}] 암호 찾음: {found}, 총 시도: {attempt_count}, 경과 시간: {elapsed:.2f}초")
                pool.terminate()
                break

    if found:
        with open("password.txt", "w") as f:
            f.write(found)
        print("암호가 password.txt에 저장되었습니다.")
    else:
        print("암호를 찾지 못했습니다.")

if __name__ == "__main__":
    unlock_zip()
