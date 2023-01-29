 import os
def add(a, b):
	print("Gong to add two number")
	print("Addition", a+b)
input1 = os.getenv("Input1")
input2 = os.getenv("input2")
add(input1,input2)