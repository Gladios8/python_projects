height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
x = round(weight / (height)**2, 2)
if x <= 18.5:
  print(f"Your BMI is {x}, You are under weight.")
elif x <= 25:
  print(f"Your BMI is {x}, You are normal weight!.")
elif x <= 30:
  print(f"Your BMI is {x}, You are overweight.")
elif x <= 35:
  print(f"Your BMI is {x}, You are obese.")
elif x >= 35:
  print(f"Your BMI is {x}, You are clinically obese.")
