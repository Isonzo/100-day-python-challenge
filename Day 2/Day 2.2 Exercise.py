height = input("Please enter your height in m: ")
weight = input("Please enter your weight in kg: ")

#Code above can't be changed

calculating_bmi = float(weight) / float(height)**2

bmi = str(round(calculating_bmi, 2))

#Under weight is 18.5, normal is 18.5 to 25, Overweight is 25 to 30, Obese is more than 30

if calculating_bmi < 18.5:
    print("Your BMI is " + bmi + ", I'm guessing you're mostly skin and bones.")

elif 18.5 < calculating_bmi < 25:
    print("Your BMI is " + bmi + ", nothing noteworthy about you.")

elif 25 < calculating_bmi < 30:
    print("Your BMI is " + bmi + ", you're either a chubster or building muscle.")

else:
    print("Your BMI is " + bmi + ", if you're not a body builder, you're just a fat fuck.")
