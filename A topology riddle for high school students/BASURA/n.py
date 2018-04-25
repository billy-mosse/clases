import sys
import time

def inv(s):
	temp = ""
	ret = ""
	for index,c in enumerate(reversed(s)):
		if c != "*":
			temp = c + temp
			if temp=="^(-1)":
				temp=""
			else:
				if "a_" in temp:
					t = temp + "^(-1)"
					if index == len(s) - 1:
						ret += t
					else:
						ret += t + "*"
					temp=""

	return ret




def formula(n):
	if n==2:
		return "a_1*a_2*a_1^(-1)*a_2^(-1)"
	else:
		s = formula(n-1)
		return s + "*a_%d*" % n + inv(s) + "*a_%d^(-1)" % n

def main(nn, s):
	n = int(nn)
	if s=="debug":
		for i in range(2,n):
			print "For %s variables:" % i
			print formula(int(i))
			print('\n' * 3)
			time.sleep(1)
	else:
		print formula(n)




if __name__=="__main__":
	if(len(sys.argv)>= 3):
		main(sys.argv[1],sys.argv[2])
	else:
		main(sys.argv[1], "")
