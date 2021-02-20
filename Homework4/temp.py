def tem_conv(Tf):
	Tc = (5/9)*(Tf-32)

	return Tc

x = int(input("enter temperature in Fahrenheit: "))
result = tem_conv(x)
print(result)