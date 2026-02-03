
# -16 -15 -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
#  M   a   c   h   i   n   e       L   e   a   r   n   i   n   g
#  0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15

s = "Machine Learning"

#Learn, chin, earn, enih,  nraeL, ahn er, ia i

print(s[8:13]) #Learn
print(s[2:6]) #chin
print(s[9:13]) #earn
print(s[6:2:-1]) #enih
print(s[12:7:-1]) #nraeL
print(s[1:12:2]) #ahn er
print(s[-3:-16:-3]) #ia i

print("==================================================================================================================")
print("==================================================================================================================")
#==================================================================================================================
#==================================================================================================================
#==================================================================================================================
#==================================================================================================================

'''
Task 1: String Slicing

"ABCDEFGHIJKL"

1) CEGI
2) KJIHGFED
3) KJIHGFEDCB
4) KIGE
5) AEI
'''
a = "ABCDEFGHIJKL"
print("task 1 output\n")
print(a[2:10:2]) #CEGI
print(a[10:2:-1]) #KJIHGFED
print(a[10:0:-1]) #KJIHGFEDCB
print(a[10:3:-2]) #KIGE
print(a[0:10:4]) #AEI

print("==============================================================================================")

##########################################################################################################################
##########################################################################################################################

'''
task 2: string slicing "Python String Slicing Example"
1) gnirtS nohtyP
2) Slicing Example
3) emEni iS oy
4) Potgigae
5) elpmaxE
6) gtoP

'''

b = "Python String Slicing Example"
print("task 2 output\n")
print(b[12::-1]) #gnirtS nohtyP
print(b[-15::1]) #Slicing Example
print(b[-1::-3]) #emEni iS oy
print(b[0::4]) #Potgigae
print(b[-1:-8:-1]) #elpmaxE
print(b[12::-4]) #gtoP

print("==============================================================================================")

##########################################################################################################################
##########################################################################################################################

'''
task 3: string slicing "Python is easy to learn"
1) easy
2) rae
3) es ola
4) si nohtyP
5) tnsa  a
6) nhy
7) easy to learn
8) ot ysae

'''

c = "Python is easy to learn"
print("task 3 output\n")
print(c[10:14:1]) #easy
print(c[-2:-5:-1]) #rae
print(c[10:21:2]) #es ola
print(c[8::-1]) #si nohtyP
print(c[2:21:3]) #tnsa  a
print(c[5::-2]) #nhy
print(c[10::1]) #easy to learn
print(c[-7:-15:-1]) #ot ysae

print("==============================================================================================")

##########################################################################################################################
##########################################################################################################################

'''
task 4: string slicing "One of the world's spectacular bridge is Tower Bridge"
1) Tower Bridge
2) wordl's spectacular
3) egdirb
4) ooho'paare ere
5) rasleo

'''

d = "One of the world's spectacular bridge is Tower Bridge"
print("task 4 output\n")
print(d[-12:]) #Tower Bridge
print(d[11:30]) #wordl's spectacular
print(d[36:30:-1]) #egdirb
print(d[::4]) #Ooho'paare ere
print(d[29::-5]) #rasleo

print("==============================================================================================")

##########################################################################################################################
##########################################################################################################################

'''
task 5: "DATASTRUCTURESANALYSIS"
Print the first and last character using index values.
Print the character at index 7.
Print the character at index -5.
Print characters from index 4 to 13.
Print the string without the first 4 characters.
Print every second character starting from index 0.
Print characters at even index positions only.
Print the entire string in reverse order.
Print characters from index 15 to index 5 in reverse.
Print the middle 6 characters using indexing.

'''
x = "DATASTRUCTURESANALYSIS"
print("task 5 output\n")
print(x[0], x[-1])
print(x [7])
print(x[-5])
print(x[4:14])
print(x[4:])
print(x[0::2])
print(x[::2])
print(x[::-1])
print(x[15:4:-1])
mid = len(x) // 2
print(x[mid-3:mid+3])   

print("==============================================================================================")

##########################################################################################################################
##########################################################################################################################

'''
task 6: "LogicalThinking"

a) Thinking
b) gniknihTlacigoL
c) LglTiki
d) lacigo
e) giTk

'''
y = "LogicalThinking"
print("task 6 output\n")
print(y[7:]) #Thinking
print(y[::-1]) #gniknihTlacigoL
print(y[0::2]) #LglTiki
print(y[6:0:-1]) #lacigo
print(y[5:10:2]) #giTk

print("==============================================================================================")

##########################################################################################################################
##########################################################################################################################
