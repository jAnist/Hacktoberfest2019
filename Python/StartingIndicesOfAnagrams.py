#Python Code
#For a Word W and String S, find all the starting indices of string S which are anagrams of W.

W = input("Enter any word to search : ")
S = input("Enter any string : ")

w = []
s = []
a = []
s1 = []

for i in W:
	w.append(i)
for i in S:
	s.append(i)

n = len(w)
m = len(s)
w.sort()

if m >= n:
	for i in range(0,n):
		s1.append(s[i])
	if s1 == w:
		print(0)
	for i in range(1,m-n+1):
		s2 = []
		del s1[0]
		s1.append(s[i+n-1])
		for j in s1:
			s2.append(j)
		s2.sort()
		if(s2 == w):
			print(i)
else:
	print("Word is bigger than string")
