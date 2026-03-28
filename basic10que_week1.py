# #1.  number is even or odd
# num=int(input("Enter the value of num"))
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")
   
# #2.number is prime or not
# flag=0
# num=int(input("Enter the value"))
# for i in range(2,num):
#     if num%i==0:
#         flag=1
        
# if flag==1:
#     print("not prime")
# else:
#     print("prime")
 
# # 3.reverse number
# num = int(input("Enter the value"))
# rev=0
# while num>0:
#     rem=num%10
#     rev=(rev*10)+rem
#     num=num//10
# print(rev)

# #4. Pallindrome number
# num = int(input("Enter the value"))
# temp=num
# rev=0
# while num>0:
#     rem=num%10
#     rev=(rev*10)+rem
#     num=num//10
    
# if rev==temp:
#     print("palindrome number")
# else:
#     print("not palindrome")


#5. Find factorial of a number
# for ex: 3=3*2*1
# num=int(input("Enter the number u want factorial of: "))
# fact=1

# for i in range(1,num+1):
#     fact=fact*i
# print("factorial of",num,"is",fact)
 
#6. Print Fibonacci series up to N terms
# n=int(input("Enter the number of terms u want to fibonacci series"))
# a=0
# b=1
# c=0

# print(a,b,end=" ")
# for i in range(2,n):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")
    
    
#7. Find sum of digits of a number
# num=int(input("enter the number whose digit sum need to be found"))
# sum=0
# while(num>0):
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(sum)

#8. Count number of digits
# num=int(input("enter the number whose digit count need to be found"))
# count=0

# while(num>0):
#     rem=num%10
#     num=num//10
#     count+=1
# print(count)

# #9. Swap two numbers (with/without temp)
# num1=int(input("enter the 1st number"))
# num2=int(input("enter the 2nd number"))
# print("Before swapping","a=",num1,"b=",num2)
# #with temp
# # swap=0
# # swap=num1
# # num1=num2
# # num2=swap
# # print("After swapping","a=",num1,"b=",num2)

# #without temp
# num1=num1+num2
# num2=num1-num2
# num1=num1-num2
# print("After swapping","a=",num1,"b=",num2)

#10. Find largest of 3 numbers
# num1=int(input("enter the 1st number"))
# num2=int(input("enter the 2nd number"))
# num3=int(input("enter the 3rd number"))
# if num1>num2 and num1>num3:
#     print(num1)
# if num2>num3:
#     print(num2)
# else:
#     print(num3)

#11. Print all elements of an array
# arr=[1,2,3,4,5]

# for i in arr:
#     print(i)
    
#12. Find maximum element in array
# arr=[1,2,9,4,5]
# max=arr[0]
# for i in arr:
#     if i>max:
#         max=i
# print(max)

# #13. Find minimum element in array
# arr=[12,2,9,1,5]
# max=arr[0]
# for i in arr:
#     if i<max:
#         max=i
# print(max)

#14. Find sum of array elements
# arr=[1,2,1,2,1]
# sum=0
# for i in arr:
#     sum+=i
# print(sum)

#15. Reverse an array
s=[51,2,41,25,17]
#with slicing
print(s[::-1])

#without slicing
op=[]
for i in range(len(s)-1,-1,-1): #
    op.append(s[i])
print(op)






    
    









