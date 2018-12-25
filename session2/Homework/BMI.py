h = int(input("enter your height(cm): "))
m = int(input("enter your weight(kg): "))
n = h/100
BMI = m/(n*n)
print("your BMI: ",BMI)
if BMI < 16:
    print("serverly underweight")
elif BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("normal")
elif BMI < 30:
    print("overweight")
else:
    print("obese")