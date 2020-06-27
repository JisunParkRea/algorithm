import sys

cnt = 0 # 사이클의 길이
num = int(sys.stdin.readline().rstrip()) # 숫자 읽어오기(input함수보다 빠름)
num_str = str(num) # 문자열로 변환
while True: # 무한루프
    cnt += 1 # 사이클 1 더하기
    sumOfDigits = sum(map(int, num_str)) # 문자열 각자리 수 더하기
    num_str = num_str[-1] + str(sumOfDigits)[-1] # 원래 문자열의 마지막 문자와 새로 만든 문자열의 마지막 문자 합치기
    if int(num_str)==num: # 처음 받아온 숫자와 새로 만든 숫자가 같으면
        print(cnt) # 사이클 길이 출력
        break # while문 빠져나오기
