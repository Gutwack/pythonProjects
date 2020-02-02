breed = input("Is this a dog or a cat?")

weight = float(input("What is the weight?"))

if breed == "dog":
    dose = weight * 0.04
    print(dose)
elif breed == "cat":
    dose = weight * 0.05
    print(dose)
else:
    print("error")
