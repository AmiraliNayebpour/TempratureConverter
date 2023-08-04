kind = input("Please enter if the temprature is fahrenheit , celsious or even kelvin : ")
kind.lower()
if kind == "fahrenheit" :
	convert = input("convert to : (celsious or kelvin) ")
	if convert == "celsious" :
		temprature = float(input("Please enter the temprature : "))
		newtemp = (temprature-32) * 5/9
		print("your converted temprature is : " , newtemp , "degrees celsious")
	else :
		temprature = float(input("Please enter the temprature : "))
		newtemp =((temprature-32) * 5/9) + 273 
		print("your converted temprature is : " , newtemp , "kelvin")
elif kind == "celsious" :
	convert = input("convert to : (fahrenheit or kelvin) ")
	if convert == "fahrenheit" :
		temprature = float(input("Please enter the temprature : "))
		newtemp = (temprature*(9/5) ) + 32
		print("your converted temprature is : " , newtemp , "degrees fahrenheit")
	else :
		temprature = float(input("Please enter the temprature : "))
		newtemp = temprature + 273
		print("your converted temprature is : " , newtemp , "kelvin")
elif kind == "kelvin" :
	convert = input("convert to : (fahrenheit or celsious) ")
	if convert == "fahrenheit" :
		temprature = float(input("Please enter the temprature : "))
		newtemp = ((temprature - 273) * (9/5 )) +32
		print("your converted temprature is : " , newtemp , "degrees fahrenheit")
	else :
		temprature = float(input("Please enter the temprature : "))
		newtemp =temprature - 273
		print("your converted temprature is : " , newtemp , "degrees celsious")
else :
	print("Please enter the right thing")
