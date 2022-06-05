from Verifications import Verifications
class Operations:	
	def __init__(self, listValues):
		self.listValues = listValues
		self.parenteseslist = []
		self.limit = True

	def sum(self,values):
		return values[0] + values[1]

	def sub(self,values):
		return values[0] - values[1]

	def mult(self,values):
		return values[0] * values[1]

	def div(self,values):
		try:
			return values[0] / values[1]
		except:
			return Exception("Can´t be divide per 0")
		
		
	
	def executeOperations(self, listValues):
		if(Verifications.IsInList(self.listValues, '(')> -1):
			self.executeParenteses()
		
		while(len(listValues) > 1):
				listValues = self.removeParenteses(listValues)
				if(Verifications.IsInList(listValues, "/") > -1):
					divIndex = listValues.index('/')
					value = []
					value.append(float(listValues[divIndex-1])) 
					value.append(float(listValues[divIndex+1]))
					listValues[divIndex-1] = self.div(value)
					listValues.pop(divIndex)
					listValues.pop(divIndex)
				
				elif(Verifications.IsInList(listValues, "*") > -1):
					divIndex = listValues.index('*')
					value = []
					value.append(float(listValues[divIndex-1])) 
					value.append(float(listValues[divIndex+1]))
					listValues[divIndex-1] = self.mult(value)
					listValues.pop(divIndex)
					listValues.pop(divIndex)

				elif(Verifications.IsInList(listValues, "+") > -1 and not Verifications.hasDivisionOrMult(listValues)):
					divIndex = listValues.index('+')
					value = []
					value.append(float(listValues[divIndex-1])) 
					value.append(float(listValues[divIndex+1]))
					listValues[divIndex-1] = self.sum(value)
					listValues.pop(divIndex)
					listValues.pop(divIndex)

				elif(Verifications.IsInList(listValues, "-") > -1 and not Verifications.hasDivisionOrMult(listValues)):
					divIndex = listValues.index('-')
					value = []
					value.append(float(listValues[divIndex-1])) 
					value.append(float(listValues[divIndex+1]))
					listValues[divIndex-1] = self.sub(value)
					listValues.pop(divIndex)
					listValues.pop(divIndex)
		
		return listValues[0]

	def executeParenteses(self):
		if(self.limit):
			self.limit = False
			if(Verifications.IsInList(self.listValues, '(')> -1):
				index = self.listValues.index('(')
				final = self.listValues.index(')')
				
				for i in range(index+1, final):
					self.parenteseslist.append(self.listValues[i])

				for j in range(index+1, final+1):
					self.listValues[index] = '1'
					self.listValues.pop(index+1)

				self.listValues[index] = self.executeOperations(self.parenteseslist)

	
	def removeParenteses(self, listValues):
		while (Verifications.IsInList(listValues, '(') > -1):
				divIndex = listValues.index('(')
				listValues.pop(divIndex)
		while (Verifications.IsInList(listValues, ')') > -1):
				divIndex = listValues.index(')')
				listValues.pop(divIndex)
		return listValues			