import sys
l1 = ['a','b','c']
l2 = [1,2,3]
result = {}
num = []
for item in l2:
	num.append(item)
	result[1] = num
#print(l2.pop(1))

result[1].append(l1)


print('\033[91m',result,'"\033[0m"')
print( '\033[1;30mGray like Ghost\033[1;m')



class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print (color.BOLD + 'Hello World !' + color.END)

print("\033[1;32;40m Bright Green  \n")