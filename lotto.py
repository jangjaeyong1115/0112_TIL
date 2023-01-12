import random

numbers = range(1,46)
lucky = sorted(random.sample(numbers,6))
print(lucky)

def get_lotto(n):
    # input : n 로또 번호
    # output : 
        # 오늘 지른 로또 금액
    result = []
    for i in range(n):
        result.append(sorted(random.sample(range(1,46), 6)))

    return result

print(get_lotto(2))