# l=['apple','banana','cherry''kiwi','mango','orange','peach']
# b=[len(i) for i in l]
# print(b)


# b=[i for i in range(1,21) ]
# print(b)


# b=[len(i) for i in l if len(i)%2!=0]
# print(b)

# 2.wap to extract vowels and digits in a string
# s="hello123"
# b=[i for i in s if i in 'aeiouAEIOU' or i.isdigit()]
# print(b)


# 3.wap to capitilize only the first letter of every word in the given list
# l=["vaidegi","rahul","shivam","kapil","patil"]
# use .upper().
# .capitalize(): it converts the firstletter of a string into uppercase by default.

# b=[i.capitalize() for i in l]
# print(b)


# 4.wap to extract only individual datatypes form the list
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# b=[i for i in l if type(i) in [str,int,float,complex,bool]]
# print(b)


# 5.wap to extract only individual datatypes from the list and sum all the individual datatypes
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# b=sum(i for i in l if type(i) in [int,float,bool])
# print(b)



# 6.wap to print the count of alphabets and numbers and space in the given string
# s="india got the independence in the year 1947"
# b=[s.count(i) for i in s if 'a'<=i<='z' or 'A'<=i<='Z']
# c=[s.count(j) for j in s if '0'<=j<='9']
# d=[s.count(k) for k in s if k==' ']
# print(b,c,d)


# 7.wap to check how many words are present in the given sentence
# s="hello world sentence"
# b=[s.count(i) for i in s if "a"<=i<="z" or "A"<=i<="Z"]
# print(b)

#----------------------------------------------------28/04/2025---------------------------------
#1.wap to check even numbers in a list and return a list containing only even numbers
# l=[2,32,1,52,31,24,56,75]
# a=[i for i in l if i%2==0]
# print(a)


# 2.wap to check elements inside the collection are even or odd,if it is even
# make it square of that numbers,if it is odd make it as cube of that numbers
# l=[2,3,5,1,7,2,3]
# a=[i**2 if  i%2==0 else i**3 for i in l]
# print(a)

# 3.wap to return a list containing 10 multiples of 2


#--------------------------------------------------------SET COMPREHENSION---------------------
# v=['vinay','kumar','bhardwaj']
# a={c for b in v for c in b if c in 'aeiou'}
# print(a)



#3.wap to return a list containing 10 multiples of 2
# a=[i*num for i in range(1,11) ]

# l=[2,3,4,2,5,6,2,3]
# a={i for i in l }
# print(a)

#2.wap to take two lists and return a set by adding elements present same index
# l1=[2,3,4,5,6,7,8,9]
# l2=[5,6,7,8,9,1,2,3]
# a={i+j for i ,j  in zip(l1,l2) }
# print(a)
