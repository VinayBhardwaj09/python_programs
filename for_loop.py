# l=[1,2,3,4]
# for i in l :
#     print(i**2)

# names =['uma','umar','deepak','nidhi']
# for i in names:
#     if len(i)%2==0:
#         print(i)

#1.wap to print the number form 1 -20 segreate even and odd number into list
# even=[]
# odd=[]
# for i in range(1,21):
#     if i%2==0:
#         even.append(i)
#     elif i%2!=0:
#         odd.append(i)
# print(even ,odd)

#2.wap to extract vowels and digits in a string
# a=input("Enter string:")
# for i in a:
#     if i in ('aeiouAEIOU') or i in ('0123456789'):
#         print(i)

#3.wap to capitilize only the first letter of every word in the given list use .upper().
#.capitalize(): it converts the firstletter of a string into uppercase by default.
# up=[]
# l=["vaidegi","rahul","shivam","kapil","patil"]
# for i in l :
#     up.append(i.capitalize())  # up.append(i[0].upper()+i[1:])
# print(up)

#4.wap to extract only individual datatypes form the list
# a=[]
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# for i in l:
#     if type(i) in [int ,float,complex,bool]:
#         a.append(i)
# print(a)

#5.wap to extract only individual datatypes from the list and sum all the individual datatypes
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# a=[]
# for i in l:
#     if type(i) in [int ,float,complex,bool]:
#         a=a[i]+a.append(i)
# print(a)


#6.wap to print the count of alphabets and numbers and space in the given string
# s="india got the independence in the year 1947"
# alpha=0
# space=0
# for i in s:
#     if 'A'<=i<='Z' or 'a'<=i<='z':
#         alpha+=1
#     elif i ==' ':
#         space+=1
# print(alpha,space)

#7.wap to check how many words are present in the given sentence
# s="hello world sentence"
# count=0
# for i in s:
#     if 'a'<=i<='z' or 'A'<=i<='Z':
#         count+=1
# print(count)


#8.wap to create a dictionary and print the characters and its Ascii value pair
# s="hello world"
# out={}
# for i in s:
#         out[i]=ord(i)
# print(out)



#9.wap to create a dictionary and traverse into it and if the length is even print as it else reverse 
# itnames=["apple","google","yahoo","microsoft","gmail","walmart"]
# out={}
# for i in itnames:
#     if len(i)%2==0:
#         out[i]=i
#     elif len(i)%2!=0:
#         out[]=[::-1]                  
# print(out)

#10.wap to print series of factorial(take user input)
# num=int(input("Enter num:"))
# fact=1
# for i in range (1,num+1):
#     fact=fact*i
# print(fact)

#11.wap to create a dictionary with element and its count pair
# l=["yellow","red","black","pink","orannge","green","red","pink","yellow"]
# out={}
# for i in l:
#     out[i]=l.count(i)
# print(out)

#12.wap to find the length of the string without useing inbuilt function
# s="Never Give Up"
# count=0
# for i in s:
#     count+=1
# print(count)

#13.wap to reverse a string without using inbuilt function
# x="you did it guys"
# rev=''
# for i in x:
#     rev=i+rev
# print(rev)

#14.wap to print alternative character from a given string
# s="hello python"
# for i in range(0, len(s),2):
#     print(s[i])

#15.wap to replace all the character with "-" if the characters occurs more than once in a string
# s="hellohai"
# for i in s:




#16.wap to get  output:--->1234 in below question
# t=("1","2","3","4")


#17.wap to Sum of numbers
# s = 'Sony12India567pvt21ltd'
# count=0
# for i in s:
#     if i in '0123456789' :
#         count+=int(i)
# print(count)

#18.WAP to print sum of internal and extrtenal list
# l = [[1,2,3], [4,5,6], [7,8,9]]
# ext_sum=0
# int_sum=0
# for i in l:
#     for j in i:
#         int_sum+=j
#     print(int_sum)
#     int_sum=0
#     ext_sum+=
# print(ext_sum)

#19. WAP to remove duplicates from the list without using set or empty list
# d=[1,2,3,4,5,6,7,1,2,3,4]
# for i in d:
#     if d.count(i)>1:
#         d.remove(i)
# print(d)
    

#20.Print all the missing numbers from 1-10 in the below list
# l = [1, 2, 3, 4, 6, 7, 10]
# f=[]
# for i in range(1,11):
#     if i 









# out=[]      
# names=['Vinay','Akhil','Shanti','neeraj']
# for i in names:
#     ans=''
#     for j in i:
#         if j in 'AEIOUaeiou':
#             ans+=j
#     out.append(ans)
# print(out)


# for i in range(1,3):
#     for j in range(1,4):
#         print(i,j)

# 15.wap to create a dictionary of characters and its indicies pair o/p:-->{"h":[0,9],"e":1..........}
s="hello python"

