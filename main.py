import requester
import random
import sys

debug = False

if debug:
    temp = [requester.Requester(random.randint(5000,10000))for i in range(6)]
    for i in temp:
        print(i.brutto,i.net_income)
        

incomes = []
n = len(sys.argv)
for i in range(1,n):
    incomes.append(requester.Requester(sys.argv[i]))
    currency = "{:,.2f} PLN".format(float(incomes[i-1].brutto))
    print(f"Brutto: {currency}, Netto: {incomes[i-1].net_income}")