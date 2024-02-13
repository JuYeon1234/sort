import random
import time

def generate_unique_numbers():
    # 1부터 10000까지의 숫자 중에서 1000개의 겹치지 않는 랜덤 숫자를 생성합니다.
    unique_numbers = random.sample(range(1, 10001), 1000)
    return unique_numbers


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# 생성된 숫자들을 출력합니다.
if __name__ == "__main__":
    unique_numbers = generate_unique_numbers()
    
    # 버블 정렬 전 시간 측정
    start_time = time.time()

    # 버블 정렬 실행
    sorted_arr = bubble_sort(unique_numbers)

    # 버블 정렬 후 시간 측정
    end_time = time.time()

    print(f"버블 정렬 실행 시간 : {end_time - start_time} 초")
    
    
    # 버블 정렬 전 시간 측정
    start_time = time.time()

    # 버블 정렬 실행
    sorted_arr = quick_sort(unique_numbers)

    # 버블 정렬 후 시간 측정
    end_time = time.time()

    print(f"퀵 정렬 실행 시간 : {end_time - start_time} 초")
