#1.  Wap to get the following output. without length function.
# S='power star'
# count=0
# for i in S:
#     if 'A'<=i<='Z' or  'a'<=i<='z' :
#         count+=1
# print(count)





# l=[100,200,35,40,60]
# sum=0
# out=[]
# for i in l:
#     sum+=i
# for j in l:
#     a=sum-j
#     out.append(a)
# print(out)



# inp='bacbcaabbaa'
# out=''
# for i in inp:
#     if i not in out:
#         out+=i()


# 7
# inp=[100,200,50,400,300]
# out=[]
# n=300
# for i in inp:
#     for j in inp:
#         if i+j==n:
#             out.extend([[j]])
# print(out+[n])


# 8.Wap to check whether the number is strong or not.
# num=int(input("Enter the num:"))
# sum=0
# temp=num
# while num>0:
#     ld=num%10
#     fact=1
#     for i in range(1,ld+1):
#         fact=fact*i
#     sum+=fact
#     num=num//10
# print(sum==temp)
# if temp==sum:
#     print("Yes, it is strong number")
# else:
#     print("No, it is not strong number")