import requester
import random
import argparse
import matplotlib.pyplot as plt
import numpy as np
debug = False

if debug:
    temp = [requester.Requester(random.randint(5000,10000))for i in range(6)]
    for i in temp:
        print(i.brutto,i.net_income)

incomes = []
parser = argparse.ArgumentParser(description='Calculate net income from gross values')
parser.add_argument('values', type=float, nargs='+', help='example: 5000.00 6000.00 7000.00 8000.00 9000.00 10000.00')
parser.add_argument('-p','--plot', default=False, action='store_true', help='Ploting gross over net')
args = parser.parse_args()
n = len(args.values)
for i in range(n):
    incomes.append(requester.GrossToNet(args.values[i]))
    # currency = "{: ,2f} PLN".format(float(incomes[i].gross))
    print(f"Gross: {float(incomes[i].gross):,}".replace(',',' ').replace('.',',') + f" PLN, Net: {incomes[i].net_income}")

if args.plot:
    net = []
    gross = []
    for i in incomes:
        # print(float(i.net_income.replace(' ','').replace('PLN','').replace(',','.')))
        net.append(float(i.net_income.replace(' ','').replace('PLN','').replace(',','.')))
        gross.append(i.gross)
    gross=np.sort(gross)
    net=np.sort(net)
    # points = np.arange(0,max(args.values))
    points = np.linspace(0,max(args.values),len(args.values))
    plt.plot(points,gross,label='Gross')
    plt.plot(points,net,label='Net')
    plt.legend(loc="upper left")
    plt.show()
