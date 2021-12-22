num = int(input('소수인지 궁금한 숫자 입력 : '))

is_prime_num = True

for i in range(2, num):
    # 2 ~ 입력한 숫자 직전까지 돌면서, 하나라도 나눠지면 소수가 아니라고 할 예정