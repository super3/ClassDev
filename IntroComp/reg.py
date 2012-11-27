# Shawn Wilkison
# November 26, 2012

# Valid Literals
data = [ '3', '13.', '.328', '41.16', '+45.80' '+0', '-01', '-14.4',
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

# Class
class RegTester:
	def __init__(self, lit):
		self.lit = lit
		self.litLen = len(lit)
		self.flag = False
		self.seek = 0
	def check1(self):
		# Check 1st Reg. Expression
		if self.seek < self.litLen and reg1(self.lit[self.seek]):
			#print("1st Expression Passed.")
			self.seek += 1
			return True
		return False
	def check2(self):
		# Check 2nd Reg. Expression and Needs to do at least
		# one iteration
		if reg2(self.lit[self.seek]):
			self.seek += 1
			#print("2nd Expression Passed.")
			while(self.seek < self.litLen):
				if reg2(self.lit[self.seek]):
					self.seek += 1
					#print("2nd Expression Passed.")
				else: 
					break
		else:
			return False
		return True
	def check3(self):
		# Check 3nd Reg Expression
		if self.seek < self.litLen and reg3(self.lit[self.seek]):
			#print("3rd Expression Passed.")
			self.seek += 1
			return True
		return False
	def check4(self):
		# Check 4th Reg Expression
		if self.seek < self.litLen and reg4(self.lit[self.seek]):
			#print("4th Expression Passed.")
			self.seek += 1
			return True
		return False
	def checkEnd(self):
		#print(str(self.seek) + ":" + str(self.litLen))
		return self.seek >= self.litLen
	def run(self):
		flag = self.check1() 
		if self.checkEnd():
			return flag

		flag = self.check2()
		if self.checkEnd():
			return flag

		flag = self.check3()
		if self.checkEnd():
			return flag

		flag = self.check2()
		if self.checkEnd():
			return flag

		flag = self.check4()
		if self.checkEnd():
			return flag

		flag = self.check1()
		if self.checkEnd():
			return flag

		flag = self.check2()
		if self.checkEnd():
			return flag

		return False			 

for i in data:
	test = RegTester(i)
	print(i + " : " + str(test.run()))