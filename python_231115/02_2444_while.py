#while문
#내가 풀었다..ㅠㅠ
star = int(input())

i =1
while i <star+1:
    print(" "*(star-i)+"*"*(2*i-1))
    i+=1

j=1
while j <star:
    print(" "*j + "*"* ((2*star)-(2*j+1)))
    j+=1

# i = 0

# while i < star :
#     print(" " * (star - i), "*" * (i * 2 + 1))
#     i += 1
    
# while i + 1 > star :
#     print(" " * (i + 1), "*" * ((2 * star -1) - (2 * i)))
#     i += 1

# #

# star = int(input())

# i = 1
# while i < star + 1 : 
#     print(" " *(star - i) + "*" * ((2 * i) - 1))
#     i += 1

# i -= 1

# while i > 0 :
#     print(" "*(star - i + 1) + "*" * (((i * 2) - 1) - 2))
#     i -= 1
    
#     #

# star = int(input())

# i = 1
# while i < star + 1:
#     print(" " * (star -1) + "*" * (2 * i - 1))
#     i += 1

# i = 1
# while i < star:
#     print(" " * i + "*" + ((2 * star - 1) - (2 * i)))
#     i += 1

