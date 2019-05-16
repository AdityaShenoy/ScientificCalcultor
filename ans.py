def root(s):
	f = s.find(chr(8730))
	while(f != -1):
		c = s.count('(', f+1, s.find(')', f+1))
		j = f+1
		for i in range(c-1):
			j = s.find('(', j+1)
		for i in range(c):
			j = s.find(')', j+1)
		s = s[:f] + s[f+1:j+1] + '**0.5' + s[j+1:]
		f = s.find(chr(8730))
	return s
	
def logarithm(s):
	f = s.find('log_')
	while(f != -1):
		c = s.count('(', f+1, s.find(')', f+1))
		j = f+1
		for i in range(c-1):
			j = s.find('(', j+1)
		for i in range(c):
			j = s.find(')', j+1)
		s = s[:f] + '1/ln' + s[f+4:j+1] + '*ln' + s[j+1:]
		f = s.find('log_')
	return s
	
def integral(s):
	f = s.find(chr(643))
	if(f != -1):
		f1 = s.find('**',f+1)
		s1 = s[f+3 : f1-1]
		low = eval(s1)
		f2 = s.find(')(', f1+2)
		s2 = s[f1+3 : f2]
		high = eval(s2)
		f3 = s.find(')dx', f2+1)
		s3 = s[f2+2:f3]
		i = low
		ans = 0
		while(i <= high):
			ans += eval(s3.replace('X', str(i)))*0.00001
			i += 0.00001
		s = s[:f] + str(ans) + s[f3+3:]
	return s