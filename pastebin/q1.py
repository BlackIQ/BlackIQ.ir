from fractions import Fraction

sorat1 = int(input("Enter Sorat 1 : "))
makhraj1 = int(input("Enter makhraj 1 : "))

sorat2 = int(input("Enter Sorat 2 : "))
makhraj2 = int(input("Enter makhraj 2 : "))

sorat3 = int(input("Enter Sorat 3 : "))
makhraj3 = int(input("Enter makhraj 3 : "))

sorats = sorat1 * sorat2 * sorat3
makhrajs = makhraj3 * makhraj2 * makhraj3

first = Fraction(sorat1, makhraj1)
second = Fraction(sorat2, makhraj2)
third = Fraction(sorat3, makhraj3)

mul = first * second * third

print("multiplication of them : ", mul)

print("Float is : ", sorats/makhrajs)

