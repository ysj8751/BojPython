lst = []
maxNum = -1
row = 0 # 행
col = 0 # 열

for i in range(9):
    tmp = list(map(int, input().split()))
    lst.append(tmp)

    for j in range(9):
        if lst[i][j] > maxNum:
            maxNum = lst[i][j]
            row = i
            col = j

print(maxNum)
print(row + 1, col + 1, end=" ")