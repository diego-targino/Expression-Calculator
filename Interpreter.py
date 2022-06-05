from Operations import Operations
from Verifications import Verifications
class Interpreter:
	def __init__(self, expression):
		self.expression = expression + '='
		self.value = 0
		self.toExecuteOrder = [] 
		self.numbers = []
		self.order  = []
		
	def readExpression(self):
		aux = ''
		for i in self.expression:
			if Verifications.IsNumber(i):
				aux = aux + i
			else:
				self.numbers.append(aux)
				self.order.append(aux)
				if(i!= '='):
					self.order.append(i)
					aux = ''
		self.removeSpaces()
		listValues = self.order
		self.order = Operations(listValues).executeOperations(listValues)
		print(f"O resultado da expressão {self.expression} é: {self.order}")
		
	def removeSpaces(self):	
			while (Verifications.IsInList(self.order, '') > -1):
				divIndex = self.order.index('')
				self.order.pop(divIndex)