list1 = []
n = int(input("Enter the limit:"))
print("Enter the list of first names:")
for i in range(0, n):
    ele = input()
    list1.append(ele)
print(list1)
count = 0
for i in list1:
    for j in i:
        if (j == "a" or j == "A"):
            count = count + 1
print("The number of 'a' in list are:", count)
