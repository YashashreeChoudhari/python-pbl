#1. Find second largest element in array
arr=[1,12,31,4]
print(sorted(arr)[-2])

max=arr[0]
smax=arr[0]
for i in arr:
    if(i>max):
        smax=max
        max=i
    if(i>max and smax!=max):
        smax=i
print(smax)
    
#2. Remove duplicates from array
arr=[1,2,3,4,5,1,2]
new_arr=[]
for i in arr:
    if i not in new_arr:
        new_arr.append(i)
print(new_arr)

#3. Move all zeros to end of array
arr=[0,1,0,3,12]
zero_arr=[]
zero_element=[]
for i in arr:
    if i!=0:
        zero_arr.append(i)
    else:
        zero_element.append(i)
print(zero_arr+zero_element) # concatenenation of 2 list

#4. Count even and odd numbers in array
arr=[1,2,3,4,5,6,45,23]
even_count=0
odd_count=0
for i in arr:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even count is",even_count,"even count is",odd_count)

#5. Find frequency of each element
arr=[1,2,3,2,1,23]
freq={}   
for i in arr:
    if i in freq:# 1  2  4
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

#or

arr = [1, 2, 2, 3, 3, 3, 4,4,4]
arr.sort()

count = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]: #checks if current element is same as previous element
        count += 1
    else:                   #Because when we enter the else block, it means:arr[i] != arr[i-1]
        print(arr[i-1], count) #prints the previous element and its count
        count = 1

print(arr[-1], count)
