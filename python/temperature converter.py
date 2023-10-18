'''
    Temperature Converter from
    "Fahrenheit to Celsius", "Celsius to Fahrenheit",
    "Kelvin to Celcius", "Celsius to Kelvin",
    "Farenheit to kelvin", "Kelvin to Farenheit"
'''
print("Welcome to Temperature Converter")
print("For Coversion from Fahrenheit to Celsius, type= F2C()")
print("For Coversion from Celsius to Fahrenheit, type= C2F()")
print("For Coversion from Kelvin to Celcius, type= K2C()")
print("For Coversion from Celsius to Kelvin, type= C2K()")
print("For Coversion from Farenheit to Kelvin, type= F2K()")
print("For Coversion from Kelvin to Farenheit, type= K2F()")

def F2C():
    F=float(input("Enter the temperature value \nFahrenheit: "))
    C =(F-32)*(5/9)
    print("Celsius=%0.3f"%C)

def C2F():
    C=float(input("Enter the temperature value in \nCelsius: "))
    F =(9/5)*C + 32
    print("Celsius=",C)
    print("Fahrenheit=%0.3f"%F)

def K2C():
    K=float(input("Enter the temperature value in \nKelvin: "))
    C = K-273.15
    print("Kelvin=",K)
    print("Celsius=%0.3f"%C)

def C2K():
    C=float(input("Enter the temperature value in \nCelsius: "))
    K = C+273.15
    print("Celsius=",C)
    print("Kelvin=%0.3f"%K)

def F2K():
    F=float(input("Enter the temperature value in \nFahrenheit: "))
    K=(F-32)*5/9+273.15
    print("Fahrenheit=",F)
    print("Kelvin=%0.3f"%K)

def F2K():
    F=float(input("Enter the temperature value in \nFahrenheit: "))
    K=(F-32)*5/9+273.15
    print("Fahrenheit=",F)
    print("Kelvin=%0.3f"%K)

def K2F():
    K=float(input("Enter the temperature value in \nKelvin: "))
    F=(K-273.15)*9/5+32;
    print("Kelvin=",K)
    print("Fahrenheit=%0.3f"%F)



