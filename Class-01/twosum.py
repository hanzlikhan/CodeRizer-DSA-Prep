arr = [5,4,7,2,11]
target = 9

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(f"Indices: {i}, {j} | Values: {arr[i]}, {arr[j]}")
            break
        
