class MobilePackage:
  def __init__(self, packageMinutes, packageSms, packagePrice, extraMinuteCost, extraSmsCost):
    self.packageMinutes = packageMinutes
    self.packageSms = packageSms
    self.packagePrice = packagePrice
    self.extraMinuteCost = extraMinuteCost
    self.extraSmsCost = extraSmsCost

def calculateTotalCostForUsingMobile(totalMinutes, totalSmsQuantity):
    mb = MobilePackage(100, 30, 30, 0.3, 0.25)
    fixedAmount = mb.packagePrice

    minutesExtraAmount = totalMinutes - mb.packageMinutes
    if(minutesExtraAmount > 0):
        minutesExtraCost = minutesExtraAmount * mb.extraMinuteCost
    else:
        minutesExtraCost = 0

    smsExtraAmount = totalSmsQuantity - mb.packageSms
    if(smsExtraAmount > 0):
        smsExtraCost = smsExtraAmount * mb.extraSmsCost
    else:
        smsExtraCost = 0

    return fixedAmount + minutesExtraCost + smsExtraCost


print('How many minutes did you use this month?')
try:
   totalMinutes = int(input()) 
except:
   print('You have to input an integer number!')
   exit()

print('How many SMSs did you use this month?')
try:
   totalSmsQuantity = int(input()) 
except:
   print('You have to input an integer number!')
   exit()

result = calculateTotalCostForUsingMobile(totalMinutes, totalSmsQuantity)
print("Your total mobile expenses for current month are: " + str(result))