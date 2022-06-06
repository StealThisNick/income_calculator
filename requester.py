import requests
from pyquery import PyQuery as pq
from datetime import date

class GrossToNet:
    def __init__(self, earnings):
        self.gross = earnings
        self.__data = {
            'sedlak_calculator[contractType]': 'work',
            'sedlak_calculator[calculateWay]': 'gross',
            'sedlak_calculator[earnings]': earnings,
            'sedlak_calculator[year]': date.today().year,
            'sedlak_calculator[mandateModels]': 'otherCompany',
            'sedlak_calculator[theSameCity]': '1',
            'sedlak_calculator[freeCost]': '1',
            'sedlak_calculator[constantEarnings]': '1',
            'work_end26Year': 'on',
            'sedlak_calculator[monthlyMiddleClassTax]': '1',
            'sedlak_calculator[monthlyEarnings][0]': earnings,
            'sedlak_calculator[monthlyEarnings][1]': earnings,
            'sedlak_calculator[monthlyEarnings][2]': earnings,
            'sedlak_calculator[monthlyEarnings][3]': earnings,
            'sedlak_calculator[monthlyEarnings][4]': earnings,
            'sedlak_calculator[monthlyEarnings][5]': earnings,
            'sedlak_calculator[monthlyEarnings][6]': earnings,
            'sedlak_calculator[monthlyEarnings][7]': earnings,
            'sedlak_calculator[monthlyEarnings][8]': earnings,
            'sedlak_calculator[monthlyEarnings][9]': earnings,
            'sedlak_calculator[monthlyEarnings][10]': earnings,
            'sedlak_calculator[monthlyEarnings][11]': earnings,
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
            'sedlak_calculator[save]' : ''
        }
        self.get_net_income()
    def get_net_income(self):
        s = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        try:
            r = s.get('https://wynagrodzenia.pl/kalkulator-wynagrodzen', headers=headers)
        except Exception as e:
            print(e)
        if r.status_code:
            html = r.text
            d = pq(html)
            token = d('#sedlak_calculator__token').attr('value')
            self.__data['sedlak_calculator[_token]'] = token
            p = s.post('https://wynagrodzenia.pl/kalkulator-wynagrodzen/wyniki', headers= headers, data = self.__data)
            html = p.text
            d = pq(html)
            try:
                self.net_income = d('#main-container div.fullbox div.col-md-3:first span')[0].text
            except Exception as e:
                self.net_income = ""
                print(f"{25*'='}ERROR: {e}{25*'='}")
                print(html)
        else:
            print(f"Can't reach destamatopn, http error code: {r.status_code}")