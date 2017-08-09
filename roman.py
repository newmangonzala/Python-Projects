class transform: 
	
	def __init__(self, number):
		self.number = number

	def roman_numeral(self):

		roman = ""
		symbol = ["I", "V", "X", "L", "C", "D", "M", u'V\u0305', u'X\u0305',u'L\u0305',u'C\u0305',u'D\u0305']
		divisor = 1
		count = 0
		for i in range(int(len(symbol)/2)):
			digit = (self.number % (divisor * 10)) // divisor
			if digit <= 3:
				roman = symbol[count] * digit + roman
			elif digit == 4: 
				roman =  symbol[count] + symbol[count+1] + roman
			elif  digit <= 8:
				roman = symbol[count+1] + symbol[count] * (digit % 5) + roman
			else:
				roman = symbol[count] + symbol[count+2] + roman
			count += 2
			divisor *= 10
		return roman

integer = transform(int(input('Enter an integer: ')))
print(integer.roman_numeral())
