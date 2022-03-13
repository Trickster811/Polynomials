###############################################################
###		Ngaoundere, Feb, 9 2022 | Nedaouka Joachim			###
###		Project talking about Operations on Polynomials		###
###		Here are functions used to perform operations on 	###
###						Polynomials							###
###		...... Started on Feb, 9 2022 at 05:41 am ......	###
###		.... Last Modified on Feb, 9 2022 at 05:41 pm ....	###
###		...... Ended on Feb, 9 2022 at 05:41 pm ......		###
###############################################################

from math import sqrt


class Monomial:
	def __init__(self, coefficient=0, degree=0):
		self.coefficient = coefficient
		self.degree = degree
	
	def print_monomial(self):
		if self.degree == 0:
			return f"{self.coefficient}"
		elif self.degree == 1:
			return f"{self.coefficient}x"
		else:
			if self.coefficient == 0:
				return ""
			else:
				return f"{self.coefficient}x^{self.degree}"
	
	def sum_monomials(self, mono):
		mono.coefficient += self.coefficient
		
		return mono
	
	def substract_monomials(self, mono):
		mono.coefficient -= self.coefficient
		
		return mono
	
	def multiply_monomials(self, mono):
		mono.coefficient *= self.coefficient
		mono.degree *= self.degree
		
		return mono


class Polynomial:
	def __init__(self, mono1, mono2, mono3, *mono):
		self.monomial1 = mono1
		self.monomial2 = mono2
		self.monomial3 = mono3

		for mon in mono:
			self.monimial = mon
		
	def print_polynomial(self):
		a = b = '+'
		if self.monomial2.coefficient < 0:
			a = ''
		if self.monomial3.coefficient < 0:
			b = ''
		return self.monomial1.print_monomial() + a + self.monomial2.print_monomial() + b + self.monomial3.print_monomial() + '\n'
		
	def sum_polynomials(self, poly):
		poly.monomial1 = poly.monomial1.sum_monomials(self.monomial1)
		poly.monomial2 = poly.monomial2.sum_monomials(self.monomial2)
		poly.monomial3 = poly.monomial3.sum_monomials(self.monomial3)
		
		return poly
	
	def substract_polynomials(self, poly):
		poly.monomial1 = poly.monomial1.substract_monomials(self.monomial1)
		poly.monomial2 = poly.monomial2.substract_monomials(self.monomial2)
		poly.monomial3 = poly.monomial3.substract_monomials(self.monomial3)
		
		return poly
		
	def multiply_monomials(self, poly):
		poly.monomial1 = poly.monomial1.sum_monomials(self.monomial1)
		poly.monomial2 = poly.monomial2.sum_monomials(self.monomial3)
		poly.monomial3 = poly.monomial3.sum_monomials(self.monomial3)
		
		return poly
		
	def factorize_polynomial(self):
		delta = self.monomial2.coefficient**2 - (4 * self.monomial1.coefficient * self.monomial3.coefficient)
		
		if delta == 0:
			x = -self.monomial2.coefficient / 2 * self.monomial1.coefficient

			if x < 0:
				x2 = str(x * -1)
				x1 = str(x)
				return 'The factorization form \nof your polynomial is \n(x ' + x1 + ')(x ' + x2 + ')' + '\n And the solution of ' + self.print_polynomial + '=0 is x = ' + x
			else:
				x2 = str(x * -1)
				x1 = str(x)
				return 'The factorization form \nof your polynomial is \n(x + ' + x2 + ')(x + ' + x1 + ')' + '\n And the solution of ' + self.print_polynomial + '=0 is x = ' + x 

		elif delta > 0:
			x1 = -self.monomial2.coefficient - sqrt(delta) / 2 * self.monomial1.coefficient
			x2 = -self.monomial2.coefficient + sqrt(delta) / 2 * self.monomial1.coefficient
			
			if x1 < 0 and x2 < 0:
				x_2 = str(x2)
				x_1 = str(x1)
				return 'The factorization form \nof your polynomial is \n(x' + x_1 + ')(x' + x_2 + ')\n' 
			elif x1 < 0 and x2 > 0:
				x_2 = str(x2)
				x_2 = x_2[:-15]
				x_1 = str(x1)
				x_1 = x_1[:-15]
				return f'The factorization form \nof your polynomial is \n(x {x_1})(x + {x_2})\n'
			elif x1 > 0 and x2 < 0:
				x_2 = str(x2)
				x_2 = x_2[:-15]
				x_1 = str(x1)
				x_1 = x_1[:-15]				
				return 'The factorization form \nof your polynomial is \n(x + ' + x_1 + ')(x + ' + x_2 + ')\n' 
			else:
				x_2 = str(x2)
				x_2 = x_2[:-15]				
				x_1 = str(x1)
				x_1 = x_1[:-15]
				return 'The factorization form \nof your polynomial is \n(x + ' + x_1 + ')(x + ' + x_2 + ')\n' 
		else:
			return 'Sorry!!! Your polynomial \nis not factorizable...'
		
	
	
		
		
def multiplication(monomial, polynomial):
	polynomial.monomial1 = polynomial.monomial1.multiply_monomials(monomial)
	polynomial.monomial2 = polynomial.monomial1.multiply_monomials(monomial)
	polynomial.monomial3 = polynomial.monomial1.multiply_monomials(monomial)

	return polynomial
	
