import pandas as pd
from pandas import DataFrame, Series
import requests as re
from bs4 import BeautifulSoup
import datetime as date
import time

my_folder = '/c/Users/Admin/VscProject/BlackTensor_Test'

class ExchangeKdd(object):
    def market_index_kdd(self):
        Data = DataFrame()

        url_dict = {'미국 USD':'http://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW',
                    '일본 JPY':'http://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_JPYKRW',
                    '유럽연합 EUR':'http://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_EURKRW',
                    '중국 CNY':'http://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_CNYKRW',
                    'WTI':'http://finance.naver.com/marketindex/worldDailyQuote.nhn?marketindexCd=OIL_CL&fdtc=2',
                    '국제 금':'http://finance.naver.com/marketindex/worldDailyQuote.nhn?marketindexCd=CMDT_GC&fdtc=2'}

        for key in url_dict.keys():
            
            date = []
            value = []

            for i in range(1,1000):
                url = re.get(url_dict[key] + '&page=%s'%i)
                url = url.content

                html = BeautifulSoup(url,'html.parser')

                tbody = html.find('tbody')
                tr = tbody.find_all('tr')
                
                
                '''마지막 페이지 까지 받기'''
                if len(tbody.text.strip()) > 3:
                    
                    for r in tr:
                        temp_date = r.find('td',{'class':'date'}).text.replace('.','-').strip()
                        temp_value = r.find('td',{'class':'num'}).text.strip()
                
                        date.append(temp_date)
                        value.append(temp_value)
                else:

                    temp = DataFrame(value, index = date, columns = [key])
                    
                    Data = pd.merge(Data, temp, how='outer', left_index=True, right_index=True)        
                    
                    print(key + '자료 수집 완료')
                    time.sleep(10)
                    break

        Data.to_csv('%s/market_index.csv'%(my_folder))
        print(Data)
        return Data

    K = market_index_kdd()