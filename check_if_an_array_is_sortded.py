# Check if an Array is Sorted
list =[1,1,1,1,90]
flag=0
for i in range(len(list)-1):
    if list[i]<=list[i+1]:
        continue
    else:
        flag=1
        print("ARRAY IS NOT SORTED")
        break

if flag==0:
    print("Array is sorted")