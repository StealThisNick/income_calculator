import requests
from pyquery import PyQuery as pq

s = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
r = s.get('https://wynagrodzenia.pl/kalkulator-wynagrodzen', headers=headers)
print(r.status_code)
html = r.text
d = pq(html)
print(d('#sedlak_calculator__token').attr('value'))
token = d('#sedlak_calculator__token').attr('value')
# print(r.headers)
# print(r.url)
# print(r.json())

data_2 = {
    'sedlak_calculator[contractType]': 'work',
    'sedlak_calculator[calculateWay]': 'gross',
    'sedlak_calculator[earnings]': 5400,
    'sedlak_calculator[year]':2022,
    'sedlak_calculator[mandateModels]': 'otherCompany',
    'sedlak_calculator[theSameCity]': '1',
    'sedlak_calculator[freeCost]': '1',
    'sedlak_calculator[constantEarnings]': '1',
    'work_end26Year': 'on',
    'sedlak_calculator[monthlyEarnings][0]': 5400,
    'sedlak_calculator[monthlyEarnings][1]': 5400,
    'sedlak_calculator[monthlyEarnings][2]': 5400,
    'sedlak_calculator[monthlyEarnings][3]': 5400,
    'sedlak_calculator[monthlyEarnings][4]': 5400,
    'sedlak_calculator[monthlyEarnings][5]': 5400,
    'sedlak_calculator[monthlyEarnings][6]': 5400,
    'sedlak_calculator[monthlyEarnings][7]': 5400,
    'sedlak_calculator[monthlyEarnings][8]': 5400,
    'sedlak_calculator[monthlyEarnings][9]': 5400,
    'sedlak_calculator[monthlyEarnings][10]': 5400,
    'sedlak_calculator[monthlyEarnings][11]': 5400,
    'sedlak_calculator[selfEmployer]': '1',
    'sedlak_calculator[rentAndAnnuityCost]': '1',
    'sedlak_calculator[sicknesCost]': '1',
    'sedlak_calculator[healthCost]': '1',
    'sedlak_calculator[FPCost]': '1',
    'sedlak_calculator[FGSPCost]': '1',
    'mandate_end26Year': 'on',
    'sedlak_calculator[accidentPercent]': '1.67',
    'sedlak_calculator[end26Year]': '1',
    'sedlak_calculator[employeePercent]': '2',
    'sedlak_calculator[employerPercent]': '1.5',
    'sedlak_calculator[octoberIncome]': '1',
    'sedlak_calculator[businessExpenses]': '0',
    'work_accidentPercent': '1.67',
    'nonwork_accidentPercent:': '1.67',
    'sedlak_calculator[save]' : '',
    'sedlak_calculator[_token]': token
}

p = s.post('https://wynagrodzenia.pl/kalkulator-wynagrodzen/wyniki', headers= headers, data = data_2)
# print(x.text)
html = p.text
d = pq(html)
temp = d('#main-container div.fullbox div.col-md-3:first span')
for i in temp:
    print(i.text)
# print(d('#main-container div.fullbox div.col-md-3:first span'))

# print(x.headers)

# r = s.get('https://wynagrodzenia.pl/kalkulator-wynagrodzen/wyniki', headers=headers)

# print(r.headers)

