T = int(input())

case = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} 

for test_case in range(1, T + 1):
    test = input() 
    year = test[0:4] 
    month = test[4:6]
    day = test[6:8]
    if 0 < int(month) < 13 and 0 < int(day) <= case[int(month)]:
        print(f'#{test_case} {year}/{month}/{day}')
    else:
        print(f'#{test_case} -1')