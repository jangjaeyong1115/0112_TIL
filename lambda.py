numbers = ['1','2','3']
# [1,2,3]으로 바꾸고 싶어?
# int : 함수

new_numbers = list(map(int,numbers))
print(new_numbers)

numbers = [[2,1],[1,3]]

print(list(map(sorted,numbers)))

numbers = [2,4]

def div_2(n):
    return n//2
print(list(map(div_2,numbers)))
print(list(map(lambda n : n//2, numbers)))
print([ n//2 for n in numbers])


new_numbers = []
for n in numbers:
    new_numbers.append(n//2)
print(new_numbers)