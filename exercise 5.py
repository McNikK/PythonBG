ear = int(input("What is the conpany's earning: "))
ex = int(input("What is your company's expenses: "))

dlt = ear - ex

if dlt > 0:
    print('Your company generate profit margin, %.2f' % (dlt/ear))
else:
    print('your company generate losses', dlt)