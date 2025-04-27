#---------------------------------------------------------DATE 30/01/2025---------------------------------------------------------
#WAP to print 20 times 'I AM BEST' 
# i=0
# while i <=20:
#     print("I am best.",i)
#     i+=1

#WAP to print first 10 natural numbers.
# i=1
#  while i<=10:
#    print(i,end='')
#     i+=1

#WAP to print even num 1 to 100
# i=2
# while i<=100:
#     print(i,end=' ')
#     i+=2

#WAP to print num which are diviseble by 5 from m to n 
# m=10
# while m<=50:
#     if m%5==0:
#         print(m,end=' ')
#     m+=1

# m=0
# n=int(input("enter num:"))
# while m<n:
#     if m%5==0:
#         print(m)
#     m+=1


#WAP if a num is divisible by 3, 5 print square of it.
# i=0
# while i<=100:
#     if i%15==0:
#         print(i**2)
#     i+=1


#---------------------------------------------------DATE 04/02/2025------------------------------------------------------------
#WAP to print the sum of first 10 natural number 
# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)
    
#WAP to print the product of first 10 natural number 
# i=1
# product=1
# while i<=10:
#     product*=i
#     i+=1
#     print(product)

#WAP to reverse the number.
# num=int(input("Enter the num:"))
# rev=0
# while num!=0:
#     ld=num%10
#     rev=rev*10+ld
#     num=num//10
# print("Reverse of num is:",rev)


#-----------------------------------------------------DATE 05/02/2025------------------------------------------------------------
#WAPP to extract all the uppercase from the given string.
# a=input("Enter string:")
# i=0
# out=''
# c=0
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         out+=a[i]
#         c+=1
#     i+=1
# print(out+str(c))


#WAP to extract all the special character from email id.
# a=input("Enter Email:")
# i=0
# out=''
# while i<len(a):
#     if a[i] in '!@#$%^&*()_' :
#         out+=a[i]
#     i+=1
# print(out)

#WAP to extract all the vowels from te given strings and count them.
# a=input("Enter string:")
# i=0
# count=0
# out=''
# while i<len(a):
#     if a[i] in 'AEIOUaeiou' :
#         out+=a[i]
#         count+=1
#     i+=1
# print(out,count)


#WAP where to take a string which is a mixture of uppar and lower case if len of uppar case > len of lower case in the string
#  print string as it is other wise print the product of upper case with len of lower case.
# a=input("Enter mixture of  string:")
# i=0
# low=''
# upper=''
# c=0
# d=0
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         upper+=a[i]
#         c+=1
#     elif 'a'<=a[i]<='z':
#         low+=a[i]
#         d+=1
#     i+=1
# if c>d:
#     print(a)
# elif c<d :
#     print(upper*d) 


#-------------------------------------------------------------------------DATE 06/02/2025-----------------------------------------------
# a='aabacabaadad'
# out={}
# i=0
# while i< len(a):
#     out[a[i]]=a.count(a[i])
#     i+=1
# print(out)


#WAP to extract all the integer from given list.
# a=[1,2,3,4,5,'hello']
# b=[]
# i=0
# while i<len(a):
#     if type(a[i])==int:
#         b+=[(a[i])]
#     i+=1
# print(b)




# a=[1,2,3,4,5,'hello']
# b=[]
# i=0
# while i<len(a):
#     if isinstance(a[i],int):
#         b+=[(a[i])]
#     i+=1
# print(b)


#-------------------------------------------------------------DATE 07/02/2025---------------------------------------------------------------------
#WAP of input = 'python is very easy' output {'python' :'nohtyp', 'is','si','very','yrev','easy',' }
# a='python is very easy'.split()
# out={}
# i=0
# while i< len(a):
#     out[a[i]]=a[i][::-1]
#     i+=1
# print(out)


#WAP of input = 'python is very easy' output {'python' :'nohtyp6', 'is','si','very4','yrev','easy',' }
# a='python is very easy'.split()
# out={}
# i=0
# while i< len(a):
#     if i%2==0:
#         out[a[i]]=a[i][::-1]+str(len(a[i]))
#     else:
#         out[a[i]]=a[i][::-1]
#     i+=1
# print(out)

# #WAP a=['hello', 3+5j,10.[1,2,3],9.8]
# a=['hello', 3+5j,10,[1,2,3],9.8]
# out=[]
# i=0
# while i<len(a):
#     if type(a[i]) in [str,list , tuple , set , dict]:
#         out+=[len(a[i])]
#     else:
#         out.append(1)
#     i+=1
# print(out)


n=int(input("Enter the num:"))
comp=n
out=0
while n>0:
    r=n%10
    fact=1
    for i in range(1,r+1):
        fact*=i
    out+=fact
    n=n//10
if comp == out:
    print("strong")
else:
    print("not strong")


