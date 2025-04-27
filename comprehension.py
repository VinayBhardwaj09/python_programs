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
s="hello world sentence"
b=[s.count(i) for i in s if "a"<=i<="z" or "A"<=i<="Z"]
print(b)