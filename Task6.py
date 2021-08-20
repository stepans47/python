def getPercentageAmount(creditAmount, creditPercentage):
    return (creditAmount * creditPercentage)/100


isAmountIncorrect = True
while(isAmountIncorrect):
    print("Enter credit amount:")
    try:
        creditAmount = int(input())
        isAmountIncorrect = False
    except:
        print("Credit amount has to be a figure!")

isPercentageIncorrect = True
while(isPercentageIncorrect):
    print("Enter credit percentage:")
    try:
        creditPercentage = int(input())
        isPercentageIncorrect = False
    except:
        print("Credit percentage has to be a figure!")

overpayment = getPercentageAmount(creditAmount, creditPercentage)       
payment = creditAmount + overpayment

print("Total payment amount: " + str(payment))
print("Overpayment amount: " + str(overpayment))