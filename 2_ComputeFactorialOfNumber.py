"""
Question: Write a program which can compute the factorial of a given numbers. 
Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
result = factorial computation
	print(numb)
input = give user input of #
	x=int(input(x))
factorial algorithm
	def fact(x):
		print(x)
		if x==0:
			return 1
		return x * fact (x-1)
"""
def fact(x):
	print(x)
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))

#4
#24