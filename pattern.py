#pattern 1

"""
i = 0
j = 0

while i<4:
    j=0
    while j<4:
        print("# ", end="")
        j+=1
    print()
    i+=1
"""

#pattern 2
#same pattern with for loop

""""

for i in range(4):
    for j in range(4):
        print("#", end="")
    print()

"""

#pattern 3

"""
for i in range(4):
    for j in range(i+1):
        print("#", end="")
    print()

"""

#pattern4


for i in range(4):
    for j in range(4,i,-1):
        print('#', end="")

    print()

