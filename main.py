import requester
import argparse
import matplotlib.pyplot as plt
import numpy as np

incomes = []
parser = argparse.ArgumentParser(description='Calculate net income from gross values')
parser.add_argument('values', type=float, nargs='+', help='example: 5000.00 6000.00 7000.00 8000.00 9000.00 10000.00')
parser.add_argument('-p','--plot', default=False, action='store_true', help='Ploting gross over net')
args = parser.parse_args()
n = len(args.values)
for i in range(n):
    incomes.append(requester.GrossToNet(args.values[i]))
    currency = "{:,.2f}".format(float(incomes[i].gross)).replace(',',' ').replace('.',',')
    print(f"Gross: {currency} PLN, Net: {incomes[i].net_income}")
    # print(f"Gross: {float(incomes[i].gross):,}".replace(',',' ').replace('.',',') + f" PLN, Net: {incomes[i].net_income}")

if args.plot:
    net = []
    gross = []
    for i in incomes:
        net.append(float(i.net_income.replace(' ','').replace('PLN','').replace(',','.')))
        gross.append(i.gross)
    gross=np.sort(gross)
    net=np.sort(net)
    # points = np.linspace(0,max(args.values),len(args.values))
    plt.plot(gross,net,'rx')
    plt.plot(gross,net)
    # plt.plot(points,gross,label='Gross')
    # plt.plot(points,net,label='Net')
    # plt.legend(loc="upper left")
    plt.title('Gross over Net')
    plt.xlabel('Gross')
    plt.ylabel('Net')
    plt.ylim(0,max(args.values))
    plt.show()
