mealCost = float(raw_input())
tipPercent = float(raw_input())
taxPercent = float(raw_input())
tip = mealCost*(tipPercent/100)
tax= mealCost*(taxPercent/100)
totalCost = int(round(mealCost + tip + tax))

print "The total meal cost is %s dollars." % (totalCost)