# for letter in range(ord('A'), ord('Z')+1):
#     print(chr(letter))


# for i in range(ord('A'), ord('Z')+1):
#     for j in range(ord('A'), i+1):
#         print(chr(j), end=" ")
#     print()

# https://www.codespeedy.com/python-program-to-print-alphabetical-pattern/


for i in range (65,91):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()
