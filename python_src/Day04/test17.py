# date : 2024-01-18
# desc : 리스트, 문자열 연산(추가)

arr = [i for i in range(10)]
print(arr)

arr[4] = 56
print(arr)
print(len(arr))

arr.append(17)
print(len(arr))
print(arr)

arr.insert(3, 'Seven')
print(arr)

arr2 = [7, 9, 10]

new_arr = arr + arr2
print(new_arr)

arr.extend(arr2)
print(arr)

arr3 = [10, 4, 2, 5, 8, 3, 9, 7, 1]
print(arr3)
arr3.sort()
print(arr3)
arr3.sort(reverse=True)
print(arr3)