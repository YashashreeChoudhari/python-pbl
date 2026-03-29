# 6. Rotate array by K positions
#arr=[1,2,3,4,5,6]
#k=2
# After 1st rotation: Last element moves to front → [6, 1, 2, 3, 4, 5]
# After 2nd rotation: Again, last element to front → [5, 6, 1, 2, 3, 4]

arr = [1,2,3,4,5]
k = 4

for i in range(k):
    last = arr[-1]
    arr.insert(0, last)
    arr.pop()

print(arr)


# 7. Find missing number in array (1 to N)
arr = [1,2,4,5,9]
n = 5

total = n*(n+1)//2
sum_arr = 0

for i in arr:
    sum_arr += i

print("Missing:", total - sum_arr)

# 8. Find duplicate element in array
arr=[1,5,2,3,2,1,9]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print(arr[i])
        
# 9. Find pair with given sum (Two Sum)
a=[1,5,2,3,2,1,9]
target_sum=7
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target_sum:
            print(a[i],a[j])
            break
            
# 10. Check if array is sorted
sorted_flag = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        sorted_flag = False
        break

print(sorted_flag)

# 11. Merge two sorted arrays
arr=[1,2,3]
arr1=[4,5,6]
print(arr+arr1)

# or
arr2=[]
for i in arr:
    arr2.append(i)
    for i in arr1:
        arr2.append(i)
print(sorted(arr2))
    
#12. Find intersection of two arrays
a = [1,2,3,4]
b = [3,4,5,6]

for i in a:
    for j in b:
        if i == j:
            print(i)

#13. Find common elements in two arrays
a = [1,2,3,4]
b = [3,4,5,6]

for i in a:
    for j in b:
        if i == j:
            print(i)
            
# 14. Find maximum difference (j > i)
a = [1,2,3,4]
max_diff=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]-a[i]>max_diff:
            max_diff=a[j]-a[i]
print(max_diff)

# 15. Compute prefix sum array
# For an input array arr[] = [10, 20, 10, 5, 15]: 

arr=[10, 20, 10, 5, 15]
sum=0
prefix=[]
for i in arr:
    sum=sum+i
    prefix.append(sum)
print(prefix)

