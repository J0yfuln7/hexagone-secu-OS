a=1
b=1
c=0
d=0
f= not(a and (not b) and (a or b)) or (not a and b) and not (a or (not b) or (not c))
g= not((c or d) and a and not (c) and d and ((not a) and c or (not d)))

s1 = a and (a or b)
s2 = (a or b) and ((not a) or b)
s3 = (a and (not b) or c) and (a or (not b))
s4 = (a and b) or c and (not a) or (b and c) and (not b)
s5 = (a or b or c) and (not a or b or c) or (a and b) or c and d
s6 = a or b or (not c) and b or (a or not c) or not ((not a) or b or ((not a) and c))

'''
s1 = 1
s2 = 1 and 1 donc s2 = 1
s3 = 0 and 1 donc s3 = 0
s4 = 1 or 0 and 0 or 0 and 0
= 1 or 0 or 0
=1
s5 = 1 and 1 or 1 or 0 and 0
= 1 or 1 or 0
= 1
s6 = 1 or 1 or 1 and 1 or 1 or (1 or 0)
= 				1
= 1 or 1 or 1 or 1 or 1
= 1 
'''

print(s1,s2,s3,s4,s5,s6)
