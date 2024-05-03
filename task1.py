height = float(input("Enter height (in metres): "))
weight = float(input("Enter weight (in kilograms): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"[UnderWeight] BMI = {round(bmi, 2)}")
elif bmi >= 25:
    print(f"[OverWeight] BMI = {round(bmi, 2)}")
else:
    print(f"[Normal] BMI = {round(bmi, 2)}")