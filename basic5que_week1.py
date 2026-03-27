#1.  number is even or odd
num=int(input("Enter the value of num"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")
   
#2.number is prime or not
flag=0
num=int(input("Enter the value"))
for i in range(2,num):
    if num%i==0:
        flag=1
        
if flag==1:
    print("not prime")
else:
    print("prime")
 
# 3.reverse number
num = int(input("Enter the value"))
rev=0
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print(rev)

#4. Pallindrome number
num = int(input("Enter the value"))
temp=num
rev=0
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
    
if rev==temp:
    print("palindrome number")
else:
    print("not palindrome")






    
    









