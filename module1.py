#def Pindala(külg1:float,külg2:float)->float:
#	"""Riistküliku pindala ledmine
#	:param float külg1: Riistküliku esimene külg
#	:param float külg2: Riistküliku teine külg
#	:rtype:float
#	"""

#	S=külg1*külg2
#	return S


#def arithmetic(a:float,b:float,c:str):
#	"""Saab teha +,-,*,/ ja tagastab arv kui
#	vastus on arv ja "Tundmatu tehe" kui ei saa vastus leida
#	:param float a: Esimene arv
#	:param float b: Teine arv
#	:param str c: arithmetic'
#	rtype:var
#	"""
	
#	if c =="+":
#		vastus=a+b
#	elif c =="-":
#		vastus=a-b
#	elif c =="*":
#		vastus=a*b
#	elif c =="/":
#		if b==0:
#			vastus="Нельзя делить на ноль"
#		else:
#			vastus=a/b
#	return vastus


#def  is_year_leap(year:int):

#	if year %4==0:
#		vastus=True
#	elif year%4!=0:
#		vastus=False
#	return vastus

import math
def square(side:float):
	S=side*side
	P=4*side
	D=round(side*math.sqrt(2))
	return S,P,D