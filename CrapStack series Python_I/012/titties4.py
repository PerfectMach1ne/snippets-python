weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == 'K':
    print("Weight in kgs: " + str(float(weight) * 0.45))
elif unit.upper() == 'L':
    print("Weight in lbs: " + str(float(weight) / 0.45))