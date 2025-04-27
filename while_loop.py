# 1. wap to print the names only if the length of the names is even 
# a=["vaidegi","ashwini","patil","srinidhi","susmitha","rahul","priyanka","usha"] 
# i=0
# while i<len(a):
#     if len(a[i]) %2==0:
#         print(a(i))
#     i+=1

# 2.wap to print the elements which in tuple,print only the if it is collection data types 
#values=(10,2.5,[10,20],"hero",True,(3,4,5),{2,7},{90:"super"}) 
# i = 0
# while i < len(values):
#     if isinstance(values[i], (list, tuple, set, dict)): 
#         print(values[i])
#     i += 1


#3. wap to extract only vowels and digits from the given string 
#a="hellopython123"
# i=0
# count=0
# out=''
# while i<len(a):
#     if a[i] in 'AEIOUaeiou' :
#         out+=a[i]
#         count+=1
#     i+=1
# print(out,count)


#4. wap to print the sum of n natural numbers.
# n=int(input("Enter the number:"))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

#5.wap to extract only vowels and digits from the given string 
# s="hellopython123" 
# i=0
# while i<len(s):
#     if s[i] in 'aeiouAEIOU':
#         print(s[i])
#     i+=1

#6. wap to print the sum of n natural numbers.
# num=int(input("Enter the num:"))
# i=1
# sum=0
# while i<=num:
#     sum+=i
#     i+=1
# print(sum)

#7. wap to find the factorial of a number. 
# num=int(input("Enter a num:"))
# i=1
# fact=1
# while i<=num:
#     fact=fact*i
#     i+=1
# print(fact)


#8. wap to extract all the lower case characters present in a string taken as input from the user. 
# a=input("Enter string:")
# i=0
# out=''
# c=0
# while i<len(a):
#     if 'a'<=a[i]<='z':
#         out+=a[i]
#         c+=1
#     i+=1
# print(out+str(c))


#9. wap tp extract all the special characters present in a string taken as input but the user.
# a=input("Enter string:")
# i=0
# out=''
# c=0
# while i<len(a):
#     if a(i) in ('!@#$%^&*()_?'):
#         out+=a[i]
#         c+=1
#     i+=1
# print(out)


#10. wap to extract all the digits present in the string taken as input from the user.
# a=input("Enter string:")
# i=0
# while i<len(a):
#     if a[i] in '1234567890' :
#         print(a[i])
#     i+=1


#11. wap to extract all the values at even index given in a list only if they are float values. 
# a=['vinay',101.1,234.2,45,66.3,34,54.4,5,3445,4.3,65]
# i=0
# while i< len(a):
#     if i%2==0 and type(a[i]) == float:
#         print(a[i])
#     i+=1

#12. wap wap to find the sum of all the integer numbers present inside given tuple.
# a=(1,'hello',2,3,4,5,6,6.6)
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==int:
#         sum+=a[i]
#     i+=1
# print(sum)

#13.wap to print a number which are divisible by 5 from a list 
# l=[63,20,67,55,85,31]
# i=0
# while i<len(l):
#     if l[i]%5==0:
#         print(l[i])
#     i+=1

#14.wap to print both upper and lower case characters.
# a=input("Enter string:")
# i=0
# low=''
# up=''
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         low+=a[i]
#     elif 'a'<=a[i]<='z':
#         up+=a[i]
#     i+=1
# print(low)
# print(up)

# Q22. Write a program to enter the numbers till the user wants and at the end it should 
# display the sum of all the numbers entered.



# Q24. Write a program to find the HCF of two numbers entered from the user. 

# # Taking input
# n = int(input("Enter 1st Number: "))
# s = int(input("Enter 2nd Number: "))

# # Euclidean Algorithm for HCF
# while s != 0:
#     n, s = s, n % s  # Swap n with s, and s with remainder

# print(f"The HCF is {n}")



# Q25. Write a program to convert Decimal to Binary. 
# Taking user input
# num = int(input("Enter a decimal number: "))

# binary = ""  # To store the binary result

# Edge case: If the number is 0, its binary is also 0
# if num == 0:
#     binary = "0"

# # While loop to convert decimal to binary
# while num > 0:
#     remainder = num % 2  # Get remainder when divided by 2
#     binary = str(remainder) + binary  # Append remainder to the left
#     num = num // 2  # Divide by 2 for the next iteration

# print(f"Binary equivalent: {binary}")



# 26. Write a program to convert Binary to Decimal.
# num = input("Enter a binary number: ")

# out=0
# i=0

# while num>0:
#     last=int(num)%10
#     dusra=last*2**
# print(dusra)















#n = int(input("ENter no"))
# i =1 
# while(i<=10):
#   print(n*i)
#   i+=1

# n = int(input("ENter no"))
# for i in range(1,11):
#   print(f"{n}X{i} = {n*i}")


# i = 1
# while(i<=10):
#   print(i,i*i)
#   i+=1

# i = 10
# l = []
# while(i<=300):
#   l.append(i)
#   i+=10
# print(l)


# i = 105
# l = []
# while(i>=7):
#   l.append(i)
#   i-=7
# print(l)


# # n*n+1/2
# n= int(input("Enter number"))
# sum = (n*(n+1))//2
# print(sum)







# i = 1
# count = 0
# while(i<=10):
#   count = i + count
#   i+=1
# print(count)

# i = 10
# while(i>=1):
#   print(i)
#   i-=1

# i = 1
# count = 0
# while(i<=10):
#   if(i%2 == 0):
#     count = i + count
#   i+=1
# print(count)
  
  
# Q12. Write a program to print all even numbers that falls between two numbers (exclusive 
# both numbers) entered from the user using while loop.

# a = int(input("Enter a number"))   
# b = int(input("Enter a number"))   

# i = a+1
# while(i<b):
#   if(i%2 == 0):
#     print(i) 
#   i+=1


# Q13. Write a program to check whether a number is prime or not. 


# num = int(input("Enter a number: "))

# if num < 2:
#     print(f"{num} is NOT a Prime Number")
# else:
#     prime = True
#     i = 2
#     while i * i <= num:  
#         if num % i == 0:
#             prime = False
#             break
#         i += 1

#     if prime:
#         print(f"{num} is a Prime Number")
#     else:
#         print(f"{num} is NOT a Prime Number")

    

# Q14. Write a program to find the sum of the digits of a number accepted from the user.

# a = int(input("Enter a number"))   
# v = 0
# while(a>0):
#    y = a%10
#    a = a//10
#  v+=y
  
   
# print(v)

# Reverse

# a = int(input("Enter a number"))   
# v = 0
# while(a>0):
#    y = a%10
#    a = a//10
#    v = v*10+y
# print(v)

# multiply

# a = int(input("Enter a number"))   
# v = 1
# while(a>0):
#    y = a%10
#    a = a//10 
#    v *= y
# print(v)

# Q17. Write a program to display the number names of the digits of a number entered by 
# user, for example if the number is 231 then output should be Two Three One 

# a = 123
# digit = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

# e = []

# while(a>0):
#   d = a%10
#   e.append(digit[d])
#   a = a//10

# e.reverse()
# print(" ".join(e))


# print(e)

# def digit_to_word(n):
#     digit_names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    
#     words = []
#     while n > 0:
#         digit = n % 10  # Extract last digit
#         words.append(digit_names[digit])  # Convert to word
#         n = n // 10  # Remove last digit
    
#     words.reverse()  # Reverse list to maintain original order
#     print(" ".join(words))

# # Input from user
# num = int(input("Enter a number: "))  

# # # Handle case when input is 0
# # if num == 0:
# #     print("Zero")
# # else:
# (digit_to_word(num))  


# class Book:
#   def _init_(self , title , authorname , isbn , available ):
#    self.title = title
#    self. author = authorname
#    self.isbn = isbn
#    self.available = True  
  
#   def get_details(self):
#     print(f"the Title of the book is {self.title} and the author name is{self.author} and isbn is{self.isbn} and book is {self.available}")
#   def mark_unavailble(self):
#     False 
#   def mark_availble(self):
#     True
  
  
# class Borrowowedbook(Book):
#     def _init_(self, borrowername , due_date ):
#       self.borrowername = borrowername
#       self.due_date = due_date
      
#     def borrow(self):
#         print(f"The book is borrow by  {self.borrowername} on the due date {self.due_date}")
#     def return_book(self):
      
#       print("The book is returned and the book is availble") 
      
      
#       18. Write a program to print the Fibonacci series till n terms (Accept n from user) using 
#       while loop.

# n = int(input("Enter Number"))
# num1 = 0
# num2 = 1
# next_num = num2
# count = 1
# while(count<=n):
#   print(num2 , end="")
#   next_num = num1+num2
#   num1 = num2
#   num2 = next_num
#   count+=1
# print()
  
# Factorial

# n = int(input("Enter Number"))
# count = 1
# b = 1
# while(count<=n):
#   b*=count
#   count+=1
  
# print(b)

# Q20. Write a program to check whether a number is Armstrong or not. (Armstrong number is 
# a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.) 
  
  
# n = 153
# a = 153
# b = 0

# while(a>0):
#   y = a%10
#   b+=(y**3)
#   a = a//10
 
# if(b==a):
#   print("This is a armanstrong")
# else:
#   print('not')
  
# Q21. Write a program to add first n terms of the following series using a while loop: 
# 1/1! + 1/2! + 1/3! + …….. + 1/n!