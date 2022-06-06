import requester
import random
# import sys
import argparse

debug = False

if debug:
    temp = [requester.Requester(random.randint(5000,10000))for i in range(6)]
    for i in temp:
        # print(i.brutto,i.net_income)
        pass
        

incomes = []
# n = len(sys.argv)
# for i in range(1,n):
#     incomes.append(requester.Requester(sys.argv[i]))
#     currency = "{:,.2f} PLN".format(float(incomes[i-1].gross))
#     print(f"Brutto: {currency}, Net: {incomes[i-1].net_income}")


parser = argparse.ArgumentParser(description='Calculate net income from gross values')
parser.add_argument('values', type=float, nargs='+', help='example: 5000.00 6000.00 7000.00 8000.00 9000.00 10000.00')
args = parser.parse_args()
n = len(args.values)
for i in range(n):
    incomes.append(requester.Requester(args.values[i]))
    currency = "{:,.2f} PLN".format(float(incomes[i].gross))
    print(f"Gross: {currency}, Net: {incomes[i].net_income}")