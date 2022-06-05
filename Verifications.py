
class Verifications:
	def IsNumber(value):
		if(value == '+' or value == '-' or value == '*' or value == '/' or value == '=' or value == "(" or value == ")"):
			return False
		else:
			return True
	def IsInList(values, caracter):
		try:
			return values.index(caracter)
		except:
			return -1
	def hasDivisionOrMult(expression):
		for i in expression:
			if i == '*' or i=='/':
				return True
		return False		
		