import random

#PowerBall generator
pball_list = []
for x in range(0, 5):
    n = random.randint(1, 69)
    pball_list.append(n)
pball = []
x = random.randint(1, 26)
if x in pball_list:
    x = random.randint(1, 26)
else:
    pball.append(x)

#print("PB Numbers: " + str(pball_list) + " PowerBall:" + str(pball))

#print("\n")

#MegaMillions generator
megam = random.sample(range(1, 70), 5)
mb = []
x = random.randint(1, 25)
if x in megam:
    x = random.randint(1, 25)
else:
    mb.append(x)

#print("Mega Numbers: " + str(megam) + " MegaBall:" + str(mb))

#print("\n")
#CarolinaCash5 generator

car_cash_5 = random.sample(range(1, 43), 5)

choice1 = input("""
    Which Lottery game would you like numbers for?
    Enter 1 for Powerball
    Enter 2 for MegaMillions
    Enter 3 for CarolinaCash5
    """)

if choice1 == str("1"):
    print("PB Numbers: " + str(pball_list) + " PowerBall:" + str(pball))
elif choice1 == str("2"):
    print("Mega Numbers: " + str(megam) + " MegaBall:" + str(mb))
elif choice1 == str("3"):
    print("CarolinaCash5 Numbers: " + str(car_cash_5))

#print("CarolinaCash5 Numbers: " + str(car_cash_5))
#print("\n")
