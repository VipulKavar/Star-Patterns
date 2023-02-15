n = 5

print("# STAR PATTERN - 1")   # STAR PATTERN - 1
#method-1
for i in range(n):
    print("*"*(i+1), end='\n')

#method-2
for i in range(n):
    for j in range(i+1):
        print("*", end='')
    print("\n", end='')

#OUTPUT
"""
*
**
***
****
*****
"""

print("--X--X--X--X--X--X--X--X--X--X--X--")
print("# STAR PATTERN - 2")  # STAR PATTERN - 2
#method-1
for i in range(n):
    print("*"*(n-i), end='\n')

#method-2
for i in range(n):
    for j in range(n-i):
        print("*", end='')
    print("\n", end='')

#OUTPUT
"""
*****
****
***
**
*
"""

print("--X--X--X--X--X--X--X--X--X--X--X--")
print("# STAR PATTERN - 3")  # STAR PATTERN - 3
#method-1
for i in range(n):
    print(f"{(i+1)}" * (i+1), end='\n')

#method-2
for i in range(n):
    for j in range(i+1):
        print(f"{i+1}", end='')
    print("\n", end='')

#OUTPUT
"""
1
22
333
4444
55555
"""

print("--X--X--X--X--X--X--X--X--X--X--X--")
print("# STAR PATTERN - 3-A")  # STAR PATTERN - 3-A
#method-1
for i in range(n):
    print(f"{(i+1)} " * (n-i), end='\n')

#method-2
for i in range(n):
    for j in range(n-i):
        print(f"{i+1}", end=' ')
    print("\n", end='')

#OUTPUT
"""
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
"""

print("--X--X--X--X--X--X--X--X--X--X--X--")
print("# STAR PATTERN - 3-B")  # STAR PATTERN - 3-B
#method-1
for i in range(n):
    num=0
    while num<=i:
        print(f"{(num+1)}", end='')
        num+=1
    print("\n", end='')
#method-2
for i in range(n):
    for j in range(i+1):
        print(f"{j+1}", end='')
    print("\n", end='')

#OUTPUT
"""
1
12
123
1234
12345
"""

print("--X--X--X--X--X--X--X--X--X--X--X--")
print("# STAR PATTERN - 3-C")  # STAR PATTERN - 3-C
#method-1
num=1
for i in range(n):
    k=0
    while k<=i:
        print(f"{(num)}", end=' ')
        num+=1
        k+=1
    print("\n", end='')
#method-2
num=1
for i in range(n):
    for j in range(i+1):
        print(f"{num}", end=' ')
        num+=1
    print("\n", end='')

#OUTPUT
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

print("--X--X--X--X--X--X--X--X--X--X--X--")
print("# STAR PATTERN - 4")  # STAR PATTERN - 4
#method-1
for i in range(n):
    print(f"{(i+1)}" * (n-i), end='\n')

#method-2
for i in range(n):
    for j in range(n-i):
        print(f"{i+1}", end='')
    print("\n", end='')

#OUTPUT
"""
11111
2222
333
44
5
"""

print("--X--X--X--X--X--X--X--X--X--X--X--")

print("# STAR PATTERN - 5")   # STAR PATTERN - 5
#method-1
for i in range(n):
    print(f"{(n-i)}" * (i+1), end='\n')

#method-2
for i in range(n):
    for j in range(i+1):
        print(f"{n-i}", end='')
    print("\n", end='')

#OUTPUT
"""
5
44
333
2222
11111
"""

print("--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--")
print("# STAR PATTERN - 6")   # STAR PATTERN - 6
#method-1
for i in range(n):
    print(f" " * (n-i-1), end='')
    print("*" * (i+1), end="\n")

#method-2
for i in range(n):
    for j in range(n):
        if j >= n-i-1:
            print(f"*", end='')
        else:
            print(" ", end='')
    print("\n", end='')

#OUTPUT
"""
    *
   **
  ***
 ****
*****
"""
print("--X--X--X--X--X--X--X--X--X--X--X--")

print("# STAR PATTERN - 7")   # STAR PATTERN - 7
#method-1
for i in range(n):
    print(f" " * (n-i-1), end='')
    print("*" * (2*i+1), end="\n")

#method-2
for i in range(n):
    for j in range(n+i):
        if j >= n-i-1:
            print(f"*", end='')
        else:
            print(" ", end='')
    print("\n", end='')

#OUTPUT
"""
    *
   ***
  *****
 *******
*********
"""
print("--X--X--X--X--X--X--X--X--X--X--X--")

print("# STAR PATTERN - 8")   # STAR PATTERN - 8
#method-1
for i in range(n):
    print(f" " * (n-i-1), end='')
    print("* " * (i+1), end="\n")

#method-2
for i in range(n):
    for j in range(n):
        if j >= n-i-1:
            print("* ", end="")
        else:
            print(" ",end='')
    print("\n",end='')

#OUTPUT
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
print("--X--X--X--X--X--X--X--X--X--X--X--")

print("# STAR PATTERN - 8-A")   # STAR PATTERN - 8-A
#method-1
for i in range(n):
    print(f" " * (i), end='')
    print("* " * (n-i))

#method-2
for i in range(n):
    print(" " * i, end='')
    for j in range(n-i):
        print("* ", end="")
    print("\n",end='')

#OUTPUT
"""
* * * * *
 * * * *
  * * *
   * *
    *
"""
print("--X--X--X--X--X--X--X--X--X--X--X--")

print("# STAR PATTERN - 9")   # STAR PATTERN - 9
#method-1
num=65
for i in range(n):
    print(f"{chr(num)}" * (i+1), end='')
    print(" " * (n-i-1), end="\n")
    num+=1

#method-2
num=65
for i in range(n):
    for j in range(i+1):
        print(f"{chr(num)}", end="")
    num+=1    
    print("\n",end='')

#OUTPUT
"""
A
BB
CCC
DDDD
EEEEE
"""
print("--X--X--X--X--X--X--X--X--X--X--X--")

print("# STAR PATTERN - 9-A")   # STAR PATTERN - 9-A
#method-1
num=65
for i in range(n):
    k=0
    while k<=i:
        print(f"{chr(num)}", end=' ')
        k+=1
        num+=1
    print("\n", end="")

#method-2
num=65
for i in range(n):
    for j in range(i+1):
        print(f"{chr(num)}", end=" ")
        num+=1    
    print("\n",end='')

#OUTPUT
"""
A
B C
D E F
G H I J
K L M N O
"""
print("--X--X--X--X--X--X--X--X--X--X--X--")

print("# STAR PATTERN - 10")   # STAR PATTERN - 10
#method-1
for i in range(n):
    print(" " * i, end='')
    print("* " * (n-i))
for i in range(n-1):
    print(" " * (n-i-2), end='')
    print("* " * (i+2), end='\n')

#method-2
for i in range(n):
    print(" " * (i), end='')
    for j in range(n-i):
        print(f"* ", end="")  
    print("\n",end='')
for i in range(n-1):
    print(" " * (n-i-2), end='')
    for j in range(i+2):
        print("* ", end='')
    print("\n", end='')

#OUTPUT
"""
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
"""
print("--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--")
