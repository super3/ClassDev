# Shawn Wilkison
# November 26, 2012

# Set Valid Literals
data = [ '3', '13.', '.328' '41.16', '+45.80' '+0', '-01', '-14.4',
'1e12', '+1.4e6', '-2.e+7', '01E-06', '-.4E-7', '00e0']

# Functions
def reg1(char):
	return char == '+' or char == '-' or reg2(char)

def reg2(char):
	return char.isdigit()

def reg3(char):
	return char == '.' or reg2(char)

def reg4(char):
	return char == 'e' or char == 'E' or reg1(char)

# Unit Tests Regular Expression 1
assert(reg1('+'))
assert(reg1('3'))
for i in range(10):
	assert(reg1((str(i))))

# Unit Tests Regular Expression 2
for i in range(10):
	assert(reg2((str(i))))

# Unit Tests Regular Expression 3
assert(reg3('.'))
for i in range(10):
	assert(reg2((str(i))))

# Unit Tests Regular Expression 4
assert(reg4('e'))
assert(reg4('E'))
for i in range(10):
	assert(reg4((str(i))))

# class RegTester:
# 	def __init__(self, lit):
# 		self.lit = lit
# 		self.flag = False
# 		self.seek = 0
# 		testLen = len(test)

# Single String Test
test = '+45.80'
flag = False
seek = 0
testLen = len(test)

# Check 1st Reg. Expression
if seek < testLen and reg1(test[seek]):
	print("1st Expression Passed.")
	seek += 1
else:
	flag = True

# Check 2nd Reg. Expression and Needs to do at least
# one iteration
if seek <= testLen and reg2(test[seek]):
	seek += 1
	print("2nd Expression Passed.")
	while(seek < testLen):
		if reg2(test[seek]):
			seek += 1
			print("2nd Expression Passed.")
		else: 
			break
else:
	flag = True

# Check 3nd Reg Expression
if seek < testLen and reg3(test[seek]):
	print("3rd Expression Passed.")
	seek += 1
else:
	flag = True

# Check 2nd Reg. Expression and Needs to do at least
# one iteration
if seek <= testLen and reg2(test[seek]):
	seek += 1
	print("2nd Expression Passed.")
	while(seek < testLen):
		if reg2(test[seek]):
			seek += 1
			print("2nd Expression Passed.")
		else: 
			break
else:
	flag = True

# Check 4th Reg Expression
if seek < testLen and reg4(test[seek]):
	print("4th Expression Passed.")
	seek += 1
else:
	flag = True