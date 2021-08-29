from bs4 import BeautifulSoup
import requests
import pandas as pd

#url input was made to 'https://fundamentus.com.br/detalhes.php'
class Fundamentus:
    def __init__(self, url):
        self.url = url
        self.ativos = []
        self.headers = {'User-Agent': 'Chrome/81.0.4044.138'
           }
    
    #the next method will return all possible tickers from Fundamentu's database
    def get_tickers(self):
        ticker_request = requests.get(self.url, headers=self.headers)
        tickers = pd.read_html(ticker_request.text)[0]
        
        for papeis in tickers['Papel']:
            self.ativos.append(papeis)
    
    #right here we make an instance of a DataFrame object for filling it afterwards
    #some developers would say it's not the bet option for handling DataFrames but+
    #considering it's an old script and it's functional, I didn't want to change it
    def init_dataframe(self):
        indx = ["Ticker",
                "Tipo de Ação",
                "Cotação",
                "Valor de Mercado",
                "Valor da Firma",
                "Ativo",
                "Nro. de Ações",
                "Oscilação 2021",
                "Oscilação 2020",
                "Oscilação 2019",
                "P/L",
                "LPA",
                "VPA",
                "P/EBIT",
                "Marg. Bruta",
                "PSR",
                "Marg. EBIT",
                "P/Ativos",
                "Margem Líquida",
                "P/Cap. Giro",
                "EBIT/Ativo",
                "P/Ativo Cic. Liq.",
                "ROIC",
                "DY",
                "ROE",
                "EV/EBIT",
                "Div Br/Patrim.",
                "Cres Rec. 5a",
                "Giro Ativos",
                "Disponibilidade",
                "Div. Bruta",
                "Div. Líquida",
                "Patrim. Liq.",
                "Receita Liq. 1a",
                "EBIT 1a",
                "Lucro Liq. 1a"]
        df = pd.DataFrame(index=indx)
        
        self.retrieve_data(df=df)
       
    #this method will retrieve all data from all possible tickers, create an object+
    #with the returned values and append it to the dataframe
    def retrieve_data(self, df):
        for element in self.ativos:
            url = f'https://fundamentus.com.br/detalhes.php?papel={element}'
            ticker_request = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(ticker_request.content, 'html.parser')

            try:
                ticker = element
            except:
                ticker = 'N/A'
            try:
                mbruta = soup.findAll('td', 'data')[22].span.text.replace('\n', '')
            except:
                mbruta = 0
            try:
                pebit = soup.findAll('td', 'data w2')[5].span.text.replace('\n', '')
            except:
                pebit = 0
            try:
                psr = soup.findAll('td', 'data')[24].span.text.replace('\n', '')
            except:
                psr = 0
            try:
                mebit = soup.findAll('td', 'data')[25].span.text.replace('\n', '')
            except:
                mebit = 0
            try:
                pativo = soup.findAll('td', 'data')[27].span.text.replace('\n', '')
            except:
                pativo = 0
            try:
                margliq = soup.findAll('td', 'data')[28].span.text.replace('\n', '')
            except:
                margliq = 0
            try:
                pcapg = soup.findAll('td', 'data')[30].span.text.replace('\n', '')
            except:
                pcapg = 0
            try:
                ebitativo = soup.findAll('td', 'data')[31].span.text.replace('\n', '')
            except:
                ebitativo = 0
            try:
                patcili = soup.findAll('td', 'data')[33].span.text.replace('\n', '')
            except:
                patcili = 0
            try:
                roic = soup.findAll('td', 'data')[34].span.text.replace('\n', '')
            except:
                roic = 0
            try:
                dy = soup.findAll('td', 'data')[36].span.text.replace('\n', '')
            except:
                dy = 0
            try:
                roe = soup.findAll('td', 'data')[37].span.text.replace('\n', '')
            except:
                roe = 0
            try:
                evebitda = soup.findAll('td', 'data')[39].span.text.replace('\n', '')
            except:
                evebitda = 0
            try:
                liqcor = soup.findAll('td', 'data')[40].span.text.replace('\n', '')
            except:
                liqcor = 0
            try:
                evebit = soup.findAll('td', 'data')[42].span.text.replace('\n', '')
            except:
                evebit = 0
            try:
                divbr = soup.findAll('td', 'data')[43].span.text.replace('\n', '')
            except:
                divbr = 0
            try:
                cres5a = soup.findAll('td', 'data')[45].span.text.replace('\n', '')
            except:
                cres5a = 0
            try:
                giroa = soup.findAll('td', 'data')[46].span.text.replace('\n', '')
            except:
                giroa = 0
            try:
                dispo = soup.findAll('td', 'data')[49].span.text.replace('\n', '')
            except:
                dispo = 0
            try:
                ativoc = soup.findAll('td', 'data')[51].span.text.replace('\n', '')
            except:
                ativoc = 0
            try:
                divb = soup.findAll('td', 'data')[48].span.text.replace('\n', '')
            except:
                divb = 0
            try:
                divl = soup.findAll('td', 'data')[50].span.text.replace('\n', '')
            except:
                divl = 0
            try:
                patliq = soup.findAll('td', 'data')[52].span.text.replace('\n', '')
            except:
                patliq = 0
            try:
                recliq = soup.findAll('td', 'data')[53].span.text.replace('\n', '')
            except:
                recliq = 0
            try:
                ebit = soup.findAll('td', 'data')[55].span.text.replace('\n', '')
            except:
                ebit = 0
            try:
                lucliq = soup.findAll('td', 'data')[57].span.text.replace('\n', '')
            except:
                lucliq = 0
            try:
                tipo = soup.findAll('td', 'data')[2].span.text
            except:
                tipo = 0
            try:
                cota = soup.find('td', 'data destaque w3').span.text
            except:
                cota = 0
            try:
                valorm = soup.findAll('td', 'data w3')[0].span.text
            except:
                valorm = 0
            try:
                valorf = soup.findAll('td', 'data w3')[1].span.text
            except:
                valorf = 0
            try:
                ativo = soup.findAll('td', 'data w3')[2].span.text
            except:
                ativo = 0
            try:
                nroa = soup.findAll('td', 'data')[13].span.text
            except:
                nroa = 0
            try:
                osc2021 = soup.findAll('td', 'data w1')[4].span.text
            except:
                osc2021 = 0
            try:
                osc2020 = soup.findAll('td', 'data w1')[5].span.text
            except:
                osc2020 = 0
            try:
                osc2019 = soup.findAll('td', 'data w1')[6].span.text
            except:
                osc2019 = 0
            try:
                pl = soup.findAll('td', 'data w2')[1].span.text
            except:
                pl = 0
            try:
                lpa = soup.findAll('td', 'data w2')[2].span.text
            except:
                lpa = 0
            try:
                pvp = soup.findAll('td', 'data w2')[3].span.text
            except:
                pvp = 0
            try:
                vpa = soup.findAll('td', 'data w2')[4].span.text
            except:
                vpa = 0

            data = {"Ticker": ticker,
                    "Tipo de Ação": tipo,
                    "Cotação": cota,
                    "Valor de Mercado": valorm,
                    "Valor da Firma": valorf,
                    "Ativo": ativo,
                    "Nro. de Ações": nroa,
                    "Oscilação 2021": osc2021,
                    "Oscilação 2020": osc2020,
                    "Oscilação 2019": osc2019,
                    "P/L": pl,
                    "LPA": lpa,
                    "VPA": vpa,
                    "P/EBIT": pebit,
                    "Marg. Bruta": mbruta,
                    "PSR": psr,
                    "Marg. EBIT": mebit,
                    "P/Ativos": pativo,
                    "Margem Líquida": margliq,
                    "P/Cap. Giro": pcapg,
                    "EBIT/Ativo": ebitativo,
                    "P/Ativo Cic. Liq.": patcili,
                    "ROIC": roic,
                    "DY": dy,
                    "ROE": roe,
                    "EV/EBIT": evebit,
                    "Div Br/Patrim.": divbr,
                    "Cres Rec. 5a": cres5a,
                    "Giro Ativos": giroa,
                    "Disponibilidade": ativoc,
                    "Div. Bruta": divb,
                    "Div. Líquida": divl,
                    "Patrim. Liq.": patliq,
                    "Receita Liq. 1a": recliq,
                    "EBIT 1a": ebit,
                    "Lucro Liq. 1a": lucliq}

            df = pd.DataFrame.append(self=df, other=data, ignore_index=True)
        self.export_to_csv(df)

    #now we get the DataFrame completed, clean it and export to a csv file
    def export_to_csv(self, df):
        df = df.dropna(how='all')
        df = df.drop_duplicates(subset=['Ticker'])
        df.reset_index(inplace = True, drop = True)
        df.index = df.index + 1
        df.to_csv('compile.csv')

    #then, all you need to do is run the 'run_script' function for it to call+
    #all the other methods for getting it done
    def run_script(self):
        self.get_tickers()
        self.init_dataframe()


#run the python script whenever you'd like and it'll do all the things automatically. Hope you enjoy :)
if __name__ == '__main__':
    run = Fundamentus('https://fundamentus.com.br/detalhes.php')
    run.run_script()
