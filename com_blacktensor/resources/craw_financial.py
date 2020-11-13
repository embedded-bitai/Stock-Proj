# import requests
# from bs4 import BeautifulSoup
# from pandas import DataFrame, Series
# import numpy as np
# import pandas as pd
# import codecs
# # import re

# # from flask_restful import Resource, reqparse
# # from com_blacktensor.ext.db import db, openSession, engine
# # from sqlalchemy import func
# # import time
# # import multiprocessing
# keyword = input("종목명 입력: ")
# # ============================================================
# # ==================                     =====================
# # ==================         KDD         =====================
# # ==================                     =====================
# # ============================================================
# class FinanceKdd(object):
#     #원하시는 종목명
#     # keyword = input("종목명 입력: ")

#     code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13',header=0)[0]
#     code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

#     # 회사명과 종목코드 필요 -> 그 이외에 필요 없는 column 제외
#     code_df = code_df[['회사명', '종목코드']]

#     # 한글로된 컬럼명을 영어로 변환
#     code_df = code_df.rename(columns={'회사명' : 'name', '종목코드' : 'code'})
#     code_df.head() 
#     print(code_df.head())
#     '''
#             name    code
#     0        DSR  155660
#     1      GS글로벌  001250
#     2  HDC현대산업개발  294870
#     3      KG케미칼  001390
#     4      LG이노텍  011070
#     '''    

#     my_folder = 'C:/Users/Admin/VscProject/BlackTensor_Test/com_blacktensor/resources'

#     def __init__(self):
#         self.keyword = keyword
#         self.code_df = code_df

#     # https://finance.naver.com/item/sise.nhn?code=005930(삼성전자)
#     def get_finance(self, keyword, code_df):
#         # item_name = self.item_name
        
#         # this = self.sk
#         # this.code_name = code_name
#         code = code_df.query("name=='{}'".format(keyword))['code'].to_string(index=False)
#         code = code.strip()

#         # 경로 탐색(http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701)
#         url = requests.get('http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A%s'%(code))
#         url = url.content
        
#         # print("요청 URL = {}".format(url))
    
#         html = BeautifulSoup(url,'html.parser')
#         body = html.find('body')

#         fn_body = body.find('div',{'class':'fng_body asp_body'})
#         ur_table = fn_body.find('div',{'id':'div15'})
#         # D_A 전체 / D_Y 연간 / D_Q 분기
#         table = ur_table.find('div',{'id':'highlight_D_Y'})

#         tbody = table.find('tbody')
    
#         tr = tbody.find_all('tr')

#         Table = DataFrame()

#         for i in tr:
        
#             # 항목 가져오기
#             category = i.find('span',{'class':'txt_acd'})
            
#             if category == None:
#                 category = i.find('th')   
        
#             category = category.text.strip()

        
#             # 값 가져오기
#             value_list =[]

#             j = i.find_all('td',{'class':'r'})
            
#             for value in j:
#                 temp = value.text.replace(',','').strip()
                    
#                 try:
#                     temp = float(temp)
#                     value_list.append(temp)
#                 except:
#                     value_list.append(0)
            
#             Table['%s'%(category)] = value_list
            
#             # 기간 가져오기
            
#             thead = table.find('thead')
#             tr_2 = thead.find('tr',{'class':'td_gapcolor2'}).find_all('th')
                    
#             year_list = []
            
#             for i in tr_2:
#                 try:
#                     temp_year = i.find('span',{'class':'txt_acd'}).text
#                 except:
#                     temp_year = i.text
                
#                 year_list.append(temp_year)
                    
#             Table.index = year_list
     
#         Table = Table.T
    
#         # print(Table)
#         df = pd.DataFrame(Table)
#         # df[loc['매출액', '영업이익', '영업이익(발표기준)', '당기순이익 ', '지배주주순이익', '비지배주주순이익', \
#         #     '자산총계', '부채총계', '자본총계', '지배주주지분', '비지배주주지분', \
#         #     '자본금', '발행주식수']] \
#         # = df[loc['매출액', '영업이익', '영업이익(발표기준)', '당기순이익 ', '지배주주순이익', '비지배주주순이익', \
#         #       '자산총계', '부채총계', '자본총계', '지배주주지분', '비지배주주지분', \
#         #     '자본금', '발행주식수']].astype(int)

#         # df = df.drop(['매출액'])
#         df.loc[:, 'keyword'] = keyword
#         print(df)

#         '''
#                             2015/12     2016/12     2017/12     2018/12     2019/12  2020/12(E)  2021/12(E)  2022/12(E)
#         매출액              2006535.00  2018667.00  2395754.00  2437714.00  2304009.00  2388064.00  2615902.00  2800634.00
#         영업이익            264134.00   292407.00   536450.00   588867.00   277685.00   372393.00   465164.00   548498.00
#         영업이익(발표기준)   264134.00   292407.00   536450.00   588867.00   277685.00        0.00        0.00        0.00     
#         당기순이익          190601.00   227261.00   421867.00   443449.00   217389.00   279829.00   353435.00   418121.00        
#         지배주주순이익      186946.00   224157.00   413446.00   438909.00   215051.00   277341.00   350214.00   414319.00      
#         비지배주주순이익       3655.00     3104.00     8422.00     4540.00     2338.00        0.00        0.00        0.00     
#         자산총계            2421795.00  2621743.00  3017521.00  3393572.00  3525645.00  3757402.00  4056352.00  4418639.00
#         부채총계            631197.00   692113.00   872607.00   916041.00   896841.00   928824.00   986411.00  1036838.00
#         자본총계            1790598.00  1929630.00  2144914.00  2477532.00  2628804.00  2828578.00  3069942.00  3381802.00
#         지배주주지분        1728768.00  1864243.00  2072134.00  2400690.00  2549155.00  2745300.00  2986764.00  3297408.00       
#         비지배주주지분       61830.00    65387.00    72780.00    76842.00    79649.00    83278.00    83178.00    84394.00      
#         자본금              8975.00     8975.00     8975.00     8975.00     8975.00     8979.00     8979.00     8979.00
#         부채비율             35.25       35.87       40.68       36.97       34.12       32.84       32.13       30.66
#         유보율              20659.47    21757.56    23681.42    26648.22    28302.40        0.00        0.00        0.00
#         영업이익률            13.16       14.49       22.39       24.16       12.05       15.59       17.78       19.58        
#         지배주주순이익률       9.32       11.10       17.26       18.00        9.33       11.61       13.39       14.79     
#         ROA                  8.07        9.01       14.96       13.83        6.28        7.68        9.05        9.87
#         ROE                 11.16       12.48       21.01       19.63        8.69       10.48       12.22       13.19
#         EPS                2198.00     2735.00     5421.00     6024.00     3166.00     4083.00     5156.00     6100.00
#         BPS                21903.00    24340.00    28971.00    35342.00    37528.00    40416.00    43970.00    48544.00
#         DPS                420.00      570.00      850.00     1416.00     1416.00     1576.00     1560.00     1543.00
#         PER                 11.47       13.18        9.40        6.42       17.63       14.40       11.40        9.64
#         PBR                 1.15        1.48        1.76        1.10        1.49        1.45        1.34        1.21
#         발행주식수         7364967.00  7033967.00  6454925.00  5969783.00  5969783.00        0.00        0.00        0.00        
#         배당수익률             1.67        1.58        1.67        3.66        2.54        0.00        0.00        0.00 
#         '''

#         # csv 파일 저장
#         df.to_csv(keyword + '_finance.csv', encoding='utf8')

#     get_finance(0, keyword, code_df)
#     # Table.to_csv('%s/%s재무.csv'%(my_folder,keyword[code]))

# # # ============================================================
# # # ==================                     =====================
# # # ==================    Preprocessing    =====================
# # # ==================                     =====================
# # # ============================================================
# class FinancelDf(object):
#     # def __init__(self):
#         # self.ck = CrawKdd()
#         # this = self.ck
#         # self.keyword = this.keyword
#         # fk = FinanceKdd()
#         # self.fk = FinanceKdd()
#         # this = self.fk
#         # self.keyword = this.keyword

#     def fina_pro(self, keyword):
#         print('----------Finance Testing----------')
# #     def DataPro(self):
#         # keyword = str(self.keyword)
#         df = pd.read_csv('{}_finance.csv'.format(keyword), encoding='utf-8')

#         df.rename( columns={'Unnamed: 0':'name', '2015/12':'f_2015_12', '2016/12':'f_2016_12',\
#             '2017/12':'f_2017_12', '2018/12':'f_2018_12', '2019/12':'f_2019_12','2020/12(E)':'f_2020_12',\
#             '2021/12(E)':'f_2021_12', '2022/12':'f_2022_12'}, inplace=True)
#         df.to_csv(keyword + '_finance.csv', encoding='utf8')
#         print('-----------------fin_file------------------')
#         print(df)
#     fina_pro(0, keyword)


# # ============================================================
# # ==================                     =====================
# # ==================       Modeling      =====================
# # ==================                     =====================
# # ============================================================
# # class FinanceDto(db.Model):
# #     __tablename__ = 'stock'
# #     __table_args__={'mysql_collate' : 'utf8_general_ci'}

# #     date : str = db.Column(db.String(10), primary_key = True, index = True)
# #     stock_name : str = db.Column(db.String(10))
# #     positive : str = db.Column(db.String(10))
# #     negative : str = db.Column(db.String(10))

# #     def __init__(self, date, stock_name, positive, negative):
# #         self.date = date
# #         self.stock_name = stock_name
# #         self.positive = positive
# #         self.negative = negative
    
# #     def __repr__(self):
# #         return f'Stock(date={self.date}, positive={self.positive},\
# #                negative={self.negative})'

# # class FinanceVo:
# #     date : str = ''
# #     stock_name : str = ''
# #     positive : str = ''
# #     negative : str = ''


# # Session = openSession()
# # session = Session()
# # finance_df = FinanceDf()


# # class FinanceDao(FinanceDto):
    
# #     @staticmethod
# #     def bulk():
# #         Session = openSession()
# #         session = Session()
# #         finance_df = FinanceDf()
# #         df = finance_df.hook()
# #         # print(df.head())
# #         session.bulk_insert_mappings(FinanceDto, df.to_dict(orient='records'))
# #         session.commit()
# #         session.close()

# #     @staticmethod
# #     def count():
# #         return session.query(func.count(FinanceDto.date)).one()

# #     @staticmethod
# #     def save(finance):
# #         new_finance = FinanceDto(date = finance['date'],
# #                            stock_name = finance['stock_name'],
# #                            positive = finance['positive'],
# #                            negative = finance['negative'])
# #         session.add(new_finance)
# #         session.commit()
# #     print('Ok!')


# # # class FinanceTf(object):
# # #     ...
# # # class FinanceAi(object):
# # #     ...


# # if __name__ == "__main__":
# #     fk = FinanceKdd()
# #     fd = FinanceDf()
# #     fd.DataPro()

# # ============================================================
# # ==================                     =====================
# # ==================      Resourcing     =====================
# # ==================                     =====================
# # ============================================================
