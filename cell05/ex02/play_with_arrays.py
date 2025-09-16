arrays = [2, 8, 9, 48, 8, 22, -12, 2]
arr_new = []

for i in range(len(arrays)):
    if arrays[i] > 5:
        arr_new.append(arrays[i] + 2)

print(arrays) 
print(arr_new)
