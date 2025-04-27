# n=int(input("Enter the num:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()



# n=int(input("Enter the num:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n-i,end=" ")
#     print() 


# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# n=int(input("Enter the num:"))
# for i in range (1,n+1):
#     print(" "*i,"*"*(n+1-i),end=" ")
#     print()


# for i in range(1,5):
#     for j in range(5):
#         print(i, end=" ")
#     print()


n = 5
for i in range(1, n + 1):
    for j in range(1, i+1):
        print(j, end="")
    print()
