# import requests
# import pandas as pd
# from pandas import DataFrame, Series
# import codecs
# import numpy as np
# import re
# from bs4 import BeautifulSoup
# from konlpy.tag import Twitter
# from collections import Counter
# from flask_restful import Resource, reqparse
# from com_blacktensor.ext.db import db, openSession, engine
# from sqlalchemy import func
# import json
# import csv

# from sqlalchemy import Column, Integer, String, Date
# # import time
# # import multiprocessing

# # ============================================================
# # ==================                     =====================
# # ==================         KDD         =====================
# # ==================                     =====================
# # ============================================================
# info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+"시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
# maxpage = int(input("최대 크롤링할 페이지 수 입력하시오: "))
# keyword = input("검색어 입력: ")
# order = input("뉴스 검색 방식 입력(관련도순=0 최신순=1 오래된순=2): ") #관련도순=0 최신순=1 오래된순=2
# s_date = input("시작날짜 입력(예: 2020.07.20):")
# e_date = input("끝날짜 입력(예: 2020.10.30):")
# # date_text = []
# # my_folder = 'C:/Users/Admin/VscProject/BlackTensor_Test/com_blacktensor/resources'


# code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13',header=0)[0]

# # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해둠
# code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

# # 회사명과 종목코드 필요 -> 그 이외에 필요 없는 column 제외
# code_df = code_df[['회사명', '종목코드']]

# # 한글로된 컬럼명을 영어로 변환
# code_df = code_df.rename(columns={'회사명' : 'name', '종목코드' : 'code'})
# code_df.head() 
# print(code_df.head())

# code = code_df.query("name=='{}'".format(keyword))['code'].to_string(index=False)
# code = code.strip()

# # ### HeadLine
# class CrawKdd(object):
#     # ##keyword = '삼성전자'
#     # info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+"시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
#     # maxpage = int(input("최대 크롤링할 페이지 수 입력하시오: "))
#     # keyword = input("검색어 입력: ")
#     # order = input("뉴스 검색 방식 입력(관련도순=0 최신순=1 오래된순=2): ") #관련도순=0 최신순=1 오래된순=2
#     # s_date = input("시작날짜 입력(예: 2020.07.20):")
#     # e_date = input("끝날짜 입력(예: 2020.10.30):")
#     # date_text = []
#     def __init__(self):
#         # info_main = self.info_main
#         # maxpage = self.maxpage
#         # keyword = self.keyword
#         # order = self.order
#         # s_date = self.s_date
#         # e_date = self.e_date
#         # date_text = self.date_text
#         self.info_main = info_main
#         self.maxpage = maxpage
#         self.keyword = keyword
#         self.order = order
#         self.s_date = s_date
#         self.e_date = e_date
#         # self.date_text = date_text
#         # self.code_df = code_df
#         # self.code = code
#     #원하시는 종목명

#     # my_folder = 'C:/Users/Admin/VscProject/BlackTensor_Test/com_blacktensor/resources'

#     # https://finance.naver.com/item/sise.nhn?code=005930(삼성전자)
#     def get_finance(self, keyword, code_df):
#         # item_name = self.item_name
        
#         # this = self.sk
#         # this.code_name = code_name
#         # code = code_df.query("name=='{}'".format(keyword))['code'].to_string(index=False)
#         # code = code.strip()

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
#         df.loc[:, 'stock'] = keyword
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

#     def get_url(self, keyword, code_df):
#         # item_name = self.item_name
        
#         # this = self.sk
#         # this.code_name = code_name
#         # code = code_df.query("name=='{}'".format(keyword))['code'].to_string(index=False)
#         # code = code.strip()

#         url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
        
#         print("요청 URL = {}".format(url))
#         # return url

#         # url = get_url(0, keyword, code_df)

#         df = pd.DataFrame()

#         for page in range(1, 16): 
#             pg_url = '{url}&page={page}'.format(url=url, page=page) 
#             df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)
#             # df = df.append({'stock' : keyword}, ignore_index=True)

#         df = df.dropna()

#         df = df.drop(columns= {'전일비', '시가', '고가', '저가'})

#         # print(df.head())
#         print(df)

#         df = df.rename(columns= {
#             '날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open',
#             '고가': 'high', '저가': 'low', '거래량': 'volume'
#             })

#         # df.drop(['diff', 'open', 'high', 'low'], axis=1, inplace=True)

#         # 데이터 타입 int 변환
#         df[['close', 'volume']] \
#             = df[['close', 'volume']].astype(int)

#         # df.drop(['diff', 'open', 'high', 'low'], axis=0, inplace=True)

#         # date를 date type 변환
#         df['date'] = pd.to_datetime(df['date'])

#         # date 기준으로 내림차순 sort
#         df = df.sort_values(by=['date'], ascending=False)

#         df.loc[:, 'stock'] = keyword

#         # df.head()
#         print('-------------------- head -------------------')
#         print(df.head())
#         print('\n-------------------- 전체 -------------------')
#         print(df)

#         # csv file 저장
#         # df.to_csv(keyword, '.csv', mode = 'a', header = False)
#         df.to_csv(keyword + '_data.csv', encoding='utf8')

#     url = get_url(0, keyword, code_df)

#     def naver_news(self, maxpage, keyword, order, s_date, e_date):
#         results = []
#         data_results = []
#         # date_text = []
#         test_date = []
        
#         for i in range(maxpage)[1:]:
#             url = r'https://search.naver.com/search.naver?&where=news&query={}&sm=tab_pge&sort={}&photo=0&field=0&reporter_article=&pd=3&ds={}&de={}&docid=&nso=so:da,p:from20201028to20201030,a:all&mynews=0&start={}&refresh_start=0'.format(keyword, order, s_date, e_date, 10*(i-1)+1)
#             resp = requests.get(url)
#             soup = BeautifulSoup(resp.text, 'lxml')
#             if i % 100 == 0:
#                 print(i,"번째 크롤링")

#             title_list = soup.find_all('a', class_ = 'news_tit')

#             for tag in title_list:
#                 results.append(tag.text)

# ### ------------------------------------------------------
#             date_lists = soup.select('span.info')

#             for date_list in date_lists:
#                 test = date_list.text

#             # print("날짜 데이터!!!!: ", test)
#             try:
#                 pattern = '\d+.(\d+).(\d+).'
#                 r = re.compile(pattern)
#                 match = r.search(test)#.group(0) # 2018.11.05.
#                 # date_text.append(match)
#                 test_date.append(test)
#             except AttributeError:

#                 pattern = '\w* (\d\w*)'

#                 r = re.compile(pattern)
#                 match = r.search(test)#.group(1)
#                 #print(match)
#                 # date_text.append(match)
#                 test_date.append(test)
            
#         # print("크롤링 날짜!! :", date_text)
#         # print("날짜 데이터!!!!: ", test_date)

# ### ------------------------------------------------------
#         return results
            

#             # #날짜 추출
#             # date_lists = soup.select('.info_group')
#             # for date_list in date_lists:
#             #     test=date_list.text
#             #     DateCleansing(0, test)

#         #     for tag in title_list:
#         #         # results += tag.get_text()
#         #         data_results.append(tag.text)
#         #     new_date = {"date" : date_text}
#         # return data_results

#     # def DateCleansing(self, test):
#     #     try:
#     #         pattern = '\d+.(\d+).(\d+).'
#     #         r = re.compile(pattern)
#     #         match = r.search(test).group(0) # 2018.11.05.
#     #         date_text.append(match)
#     #     except AttributeError:

#     #         pattern = '\w* (\d\w*)'

#     #         r = re.compile(pattern)
#     #         match = r.search(test).group(1)
#     #         #print(match)
#     #         date_text.append(match)
    
#     # print("크롤링 날짜!! :",date_text)

#     # result = naver_news(object, keyword, 1)
#     result = naver_news(object, maxpage, keyword, order, s_date, e_date)
#     # print(result)
#     df = pd.DataFrame(result)
#     # print(df)
#     df.columns = ['title']
#     print(df.head())
#     df.to_csv(keyword + '.csv', encoding='utf8')
# '''
# 0   논어, 새로운 가르침에 겁내지 않으려면 그간의 가르침을 실행해야 한다!       
# 1  "전 세계 AI 전문가 모여라"…'삼성 AI 포럼 2020' 온라인 개최
# 2              비트코인 지갑서비스 사업자도 자금세탁방지 의무 부과
# 3                  [연합뉴스 이 시각 헤드라인] - 12:00
# 4   “이건희 회장의 ‘도전 DNA’ 계승… 판도 바꾸는 기업으로 진화하자”
# '''
#     # https://finance.naver.com/item/sise.nhn?code=005930(삼성전자)


# # # # ============================================================
# # # # ==================                     =====================
# # # # ==================    Preprocessing    =====================
# # # # ==================                     =====================
# # # # ============================================================
# class CrawDf(object):
#     def __init__(self):
#         # self.ck = CrawKdd()
#         # this = self.ck
#         # self.keyword = this.keyword
#         self.keyword = keyword
#         # print("검색어1: ", self.keyword)

#         # this.maxpage = self.maxpage
#         # this.keyword = self.ck.keyword
#         # this.order = self.order
#         # this.s_date = self.s_date
#         # this.e_date = self.e_date

#         self.word = []
#         self.noun_list =[]
#         self.positive_word = []
#         self.negative_word = []

#         self.poflag = []
#         self.neflag = []

#         self.po_key = []
#         self.ne_key = []
#         self.po_val = []
#         self.ne_val = []

#         self.stock_name = []

#     # def DataPro(self, keyword, word, positive_word, negative_word, poflag, neflag):
#     def data_pro(self):
#         # 
#         keyword = str(self.keyword)
#         word = self.word
#         noun_list = self.noun_list
#         positive_word = self.positive_word
#         negative_word = self.negative_word
#         poflag = self.poflag
#         neflag = self.neflag
#         po_key = self.po_key
#         ne_key = self.ne_key
#         po_val = self.po_val
#         ne_val = self.ne_val
#         stock_name = self.stock_name

#         file = open('{}.csv'.format(keyword), 'r', encoding='utf-8')

#         lists = file.readlines()
#         file.close()
        
#         twitter = Twitter()
#         morphs = []

#         for sentence in lists:
#             morphs.append(twitter.pos(sentence))

#         # print(morphs)

#         pos = codecs.open('positive_words_self.txt', 'rb', encoding='UTF-8')

#         while True:
#             line = pos.readline()
#             line = line.replace('\n', '')
#             positive_word.append(line)
#             # keyword_text.append(line)

#             if not line: break
#         pos.close()

#         neg = codecs.open('negative_words_self.txt', 'rb', encoding='UTF-8')

#         while True:
#             line = neg.readline()
#             line = line.replace('\n', '')
#             negative_word.append(line)
#             # keyword_text.append(line)

#             if not line: break
#         neg.close()

#         for sentence in morphs : 
#             for word, text_tag in sentence :
#                 if text_tag in ['Noun']:
#                     noun_list.append(word)
#                     for x in positive_word:
#                         if x == word: 
#                             poflag.append(x)
                        
#                     for y in negative_word:
#                         if y == word:
#                             neflag.append(y)

#                 #         print("부정적 :", y)
#                 # if text_tag in ['Noun'] and ("것" not in word) and ("내" not in word) and ("첫" not in word) and \
#                 #     ("나" not in word) and ("와" not in word) and ("식" not in word) and ("수" not in word) and \
#                 #     ("게" not in word) and ("말" not in word):
#                 #      noun_list.append(word)
                    
#                 # if text_tag in ['Noun'] and ("갑질" not in word) and ("논란" not in word) and ("폭리" not in word) and \
#                 #     ("허위" not in word) and ("과징금" not in word) and ("눈물" not in word) and ("피해" not in word) and \
#                 #     ("포화" not in word) and ("우롱" not in word) and ("위반" not in word) and ("리스크" not in word) and \
#                 #     ("사퇴" not in word) and ("급락" not in word) and ("하락" not in word) and ("폐업" not in word) and \
#                 #     ("불만" not in word) and ("산재" not in word) and ("닫아" not in word) and ("손해배상" not in word) and \
#                 #     ("구설수" not in word) and ("적발" not in word) and ("침해" not in word) and ("빨간불" not in word) and \
#                 #     ("취약" not in word) and ("불명예" not in word) and ("구형" not in word) and ("기소" not in word) and \
#                 #     ("반토막" not in word) and ("호소" not in word) and ("불매" not in word) and ("냉담" not in word) and \
#                 #     ("문제" not in word) and ("직격탄" not in word) and ("한숨" not in word) and ("불똥" not in word) and \
#                 #     ("항의" not in word) and ("싸늘" not in word) and ("일탈" not in word) and ("파문" not in word) and \
#                 #     ("횡령" not in word) and ("사과문" not in word) and ("여파" not in word) and ("울상" not in word) and \
#                 #     ("초토화" not in word) and ("급감" not in word) and ("우려" not in word) and ("중단" not in word) and \
#                 #     ("퇴출" not in word) and ("해지" not in word) and ("일베" not in word) and ("이물질" not in word) and \
#                 #     ("엉망" not in word) and ("소송" not in word) and ("하락" not in word) and ("매출하락" not in word) and \
#                 #     ("혐의" not in word) and ("부채" not in word) and ("과징금" not in word) and ("포기" not in word) and \
#                 #     ("약세" not in word) and ("최악" not in word) and ("손실" not in word) and ("의혹" not in word):
#                 #     positive_word.append(word)

#                 # elif text_tag in ['Noun'] and ("MOU" not in word) and ("제휴" not in word) and ("주목" not in word) and \
#                 #     ("호응" not in word) and ("돌파" not in word) and ("이목" not in word) and ("수상" not in word) and \
#                 #     ("입점" not in word) and ("인기" not in word) and ("열풍" not in word) and ("진화" not in word) and \
#                 #     ("대박" not in word) and ("순항" not in word) and ("유치" not in word) and ("1위" not in word) and \
#                 #     ("출시" not in word) and ("오픈" not in word) and ("돌풍" not in word) and ("인싸" not in word) and \
#                 #     ("줄서서" not in word) and ("대세" not in word) and ("트렌드" not in word) and ("불티" not in word) and \
#                 #     ("진출" not in word) and ("체결" not in word) and ("증가" not in word) and ("기부" not in word) and \
#                 #     ("신제품" not in word) and ("신상" not in word) and ("최고" not in word) and ("새로운" not in word) and \
#                 #     ("착한" not in word) and ("신기록" not in word) and ("전망" not in word) and ("협력" not in word) and \
#                 #     ("역대" not in word) and ("상승" not in word) and ("늘어" not in word) and ("승인" not in word):
#                 #     negative_word.append(word)

#         count_po = Counter(poflag)
#         count_ne = Counter(neflag)
#         po_words = dict(count_po.most_common())
#         ne_words = dict(count_ne.most_common())

#         # 워드클라우드로 명사만 추출
#         '''
#         ['창립', '주년', '삼성', '전자', '이건희', '회장', '도전', '혁신', '삼성', '전자', '삼성', '포럼', '개최', '김기남', '대표', 
#         '핵심', '기술', '발전', '현', '코스피', '코스닥', '장', '동반', '상승', '덕성', '시스', '웍', '한국', '컴퓨터', '삼성', '전자
#         ', '창립', '주년', '기념', '개최', '이재용', '부회장', '불참', '롯데', '하이마트', '온라인', '오늘', '역대', '빅', '하트', ' 
#         일', '시작', '손연기', '칼럼', '차', '산업혁명', '시대', '문제', '일자리', '삼성', '전자', '모바일', '신제품', '엑시노스', ' 
#         ...
#         '멘토', '체험', '활동', '김기남', '삼성', '부회장', '로', '코로나', '해결', '위해', '전세계', '연구자', '협력', '순위', '주식
#         ', '부자', '위', '눈앞', '이재용', '뉴', '파워', '프라', '마', '규모', '유상증자', '결정', '삼성', '전자', '창립', '주념', ' 
#         기념', '회장', '도전', '혁신', '계승', '삼성', '전자', '창립', '주년', '기념', '개최']
#         '''

#         po_key = po_words.keys()
#         po_val = po_words.values()

#         ne_key = ne_words.keys()
#         ne_val = ne_words.values()

#         print("\n긍정적인 단어 :", po_key, po_val)
#         print("부정적인 단어 :", ne_key, ne_val)
        
#         po_df = pd.DataFrame(list(po_words.items()), columns=['positive', 'pos_count'])
#         ne_df = pd.DataFrame(list(ne_words.items()), columns=['negative', 'neg_count'])

#         df = pd.concat([po_df, ne_df], axis=1)

#         df.loc[:, 'stock'] = keyword

#         print(df.head())
#         df.to_csv(keyword + '_word.csv', encoding='utf8')

#         #

#         # df_file = []
#         # print('----------------------------')
#         # with open('{}_word.csv'.format(keyword), 'r', encoding='utf-8') as file_df:
#         #     reader = csv.reader(file_df)
#         #     for row in reader:
#         #         df_file.append(row)
#         #         print(row)
#         #     print('------------df_file----------------')
#         #     print(df_file)
#         # df_file = pd.DataFrame(df_file)
#         # print('------------df_file2----------------')
#         # print(df_file)
#         #
#         news_file = pd.read_csv('{}.csv'.format(keyword), index_col=[0], encoding='utf-8')
#         df_file = pd.read_csv('{}_data.csv'.format(keyword), index_col=[0], encoding='utf-8')
#         fin_file = pd.read_csv('{}_finance.csv'.format(keyword), index_col=[0], encoding='utf-8')
#         print('-----------------df_file------------------')
#         print(df)
#         print('-----------------df_file------------------')
#         print(df_file)
#         # df_file.to_csv(keyword + '_set.csv', index=False, encoding='utf8')
#         df_file.to_csv(keyword + '_set.csv', encoding='utf8')
#         print('-----------------news_file------------------')
#         print(news_file)
#         df_file.to_csv(keyword + '_set.csv', encoding='utf8')
#         print('-----------------fin_file------------------')
#         print(fin_file)

#         #     print(type(file_df))
#         #     print('------------DataFrame----------------')
#         #     file_df = pd.DataFrame(file_df)
#         #     print(file_df)

#         #     print('------------df_file----------------')
#         #     df_file = []
#         #     for txt in file_df:
#         #         df_file.append(txt)
#         #         print(txt)
#         #     print(df_file)
        
#         # print('----------------------------')
#         # df_file = open('{}_word.csv'.format(keyword), 'r', encoding='utf-8')
#         # # df = pd.read_csv('{}_word.csv'.format(keyword), encoding='utf-8')
#         # # df = df.drop([df.columns[0]], axis=1)
#         # rdr = csv.reader(df_file)
#         # print("확인: ", rdr)
#         df = pd.concat([df, df_file, news_file, fin_file], axis=1)
#         print('--------------final_df----------------')
#         df.to_csv(keyword + '_set.csv', encoding='utf8')
#         print(df)

# #       

#         '''
#         긍정적인 단어 : {'상승': 141, '인기': 66, '출시': 60, '전망': 36, '오픈': 30, 
#         '돌파': 19, '트렌드': 12, '체결': 12, '증가': 12, '역대': 11, '협력': 11, 
#         '주목': 11, '미소': 8, '기부': 8, '승인': 6, '최고': 6, '대세': 5, '유치': 4, 
#         '수상': 4, '불티': 2, '부상': 2, '순항': 2, '호응': 1, '진출': 1}
#         부정적인 단어 : {'급감': 233, '여파': 163, '하락': 162, '피해': 115, 
#         '직격탄': 83, '논란': 61, '중단': 41, '손실': 39, '반토 막': 34, '최악': 33, 
#         '포기': 32, '폐업': 25, '급락': 25, '우려': 24, '불매': 14, '눈물': 13, '
#         매각': 10, '호소': 9, '울상': 7, '문제': 6, '불만': 6, '약세': 5, '한숨': 5, 
#         '일베': 4, '해지': 4, '초토화': 3, '참혹': 3, '폐점': 2, '파문': 2, 
#         '과징금': 2, '항의': 1, '소송': 1, '불명예': 1, '리스크': 1, '갑질': 1, 
#         '침해': 1, '발끈': 1}
#         '''
#         return df
# # ============================================================
# # ==================                     =====================
# # ==================       Modeling      =====================
# # ==================                     =====================
# # ============================================================
# # class CrawDto(db.Model):
# #     __tablename__ = 'new_emotion'
# #     __table_args__={'mysql_collate' : 'utf8_general_ci'}

# #     # date : str = db.Column(db.String(10), primary_key = True, index = True)
# #     # stock_name : str = db.Column(db.String(10))
# #     # positive : str = db.Column(db.String(10))
# #     # negative : str = db.Column(db.String(10))
# #     no = Column(Integer, primary_key=True)
# #     date = Column(Date)
# #     stock_name = Column(String)
# #     positive = Column(String)
# #     negative = Column(String)

# #     def __init__(self, no, date, stock_name, positive, negative):
# #         self.no = no
# #         self.date = date
# #         self.stock_name = stock_name
# #         self.positive = positive
# #         self.negative = negative
    
# #     def __repr__(self):
# #         timer = self.time.strftime('%Y-%m-%d')
# #         return f'new_emotion(no={self.no}, date={self.timer}, stock_name={self.stock_name}, \
# #          positive={self.positive}, negative={self.negative})'

# #     @property
# #     def json(self):
# #         return {
# #             'no': self.no,
# #             'date': self.time.strftime('%Y-%m-%d'),
# #             'stock_name': self.stock_name,
# #             'positive': self.positive,
# #             'negative': self.negative
# #         }

# # # class CrawVo:
# # #     no = int = 0
# # #     date : str = ''
# # #     stock_name : str = ''
# # #     positive : str = ''
# # #     negative : str = ''


# # Session = openSession()
# # session = Session()
# # craw_df = CrawDf()


# # class CrawDao(CrawDto):
    
# #     @staticmethod
# #     def bulk():
# #         Session = openSession()
# #         session = Session()
# #         craw_df = CrawDf()
# #         df = craw_df.hook()
# #         # print(df.head())
# #         session.bulk_insert_mappings(CrawDto, df.to_dict(orient='records'))
# #         session.commit()
# #         session.close()

# #     @staticmethod
# #     def count():
# #         return session.query(func.count(CrawDto.date)).one()

# #     @staticmethod
# #     def save(craw):
# #         new_craw = CrawDto(date = craw['date'],
# #                            stock_name = craw['stock_name'],
# #                            positive = craw['positive'],
# #                            negative = craw['negative'])
# #         session.add(new_craw)
# #         session.commit()

# # # class CrawTf(object):
# # #     ...
# # # class CrawAi(object):
# # #     ...


# # if __name__ == "__main__":
# #     ck = CrawKdd()
# #     cd = CrawDf()
# #     cd.DataPro()

# # # ============================================================
# # # ==================                     =====================
# # # ==================      Resourcing     =====================
# # # ==================                     =====================
# # # ============================================================

# # # parser = reqparse.RequestParser()

# # # parser.add_argument('stock_name', type = str, required = True,
# # #                             help='This field should be a userId')
# # # parser.add_argument('positive', type = str, required = True,
# # #                             help='This field should be a password')
# # # parser.add_argument('negative', type = str, required = True,
# # #                             help='This field should be a password')

# # # class Craw(Resource):
    
# # #     @staticmethod
# # #     def post():
# # #         args = parser.parse_args()
# # #         craw = CrawVo()
# # #         craw.stock_name = args.stock_name
# # #         craw.positive = args.positive
# # #         craw.negative = args.negative
# # #         # service.assign(craw)
# # #         # print("Predicted Craw")

# # class Craw(Resource):
     
# #      def __init__(self):
# #         self.dao = CrawDao()
        
# #      def get(self):        
# #         result = self.dao.find_all()
# #         return jsonify(json_list=[item.json for item in result])
# # =========================================================================================================================
# # class CrawDto(db.Model):
# #     __tablename__ = 'stock'
# #     __table_args__={'mysql_collate' : 'utf8_general_ci'}
# #     no : int = db.Column(db.Integer, primary_key = True, index = True)
# #     positive : str = db.Column(db.String(10), primary_key = True, index = True)
# #     pos_count : int = db.Column(db.Integer)
# #     negative : str = db.Column(db.String(10))
# #     neg_count : int = db.Column(db.Integer)
# #     stock : str = db.Column(db.String(10))

# #     def __init__(self, no, positive, pos_count, negative, neg_count, stock):
# #         self.no = no
# #         self.positive = positive
# #         self.pos_count = pos_count
# #         self.negative = negative
# #         self.neg_count = neg_count
# #         self.stock = stock
    
# #     def __repr__(self):
# #         return f'Stock(no={self.no}, positive={self.positive}, pos_count{self.pos_count}, \
# #                negative={self.negative}, neg_count={self.neg_count}, stock={self.stock})'

# #     def json(self):
# #             return {
# #                 'no' : self.no,
# #                 'positive' : self.positive,
# #                 'pos_count' : self.pos_count,
# #                 'negative' : self.negative,
# #                 'neg_count' : self.neg_count,
# #                 'stock' : self.stock
# #             }

# # class CrawVo:
# #     no : int = 0
# #     positive : str = ''
# #     pos_count : int = 0
# #     negative : str = ''
# #     neg_count : int = 0
# #     stock : str = ''



# # Session = openSession()
# # session = Session()
# # craw_df = CrawDf()


# # class CrawDao(CrawDto):
# #     ck = CrawKdd()
# #     this = ck
# #     keyword = this.keyword
# #     print("DAO: ", keyword)
# #     # cd = CrawDf()
# #     # this = cd.DataPro()
# #     # data = this.df
# #     # print("DAO DATA: ", data)
# #     # keyword = str(keyword)
# #     # df = pd.read_csv(keyword, '_data.csv')
# #     # df = pd.read_csv(keyword, '.csv')
# #     df = pd.read_csv('{}_word.csv'.format(keyword), encoding='utf-8')
# #     df = df.drop([df.columns[0]], axis=1)
# #     # df = open('{}.csv'.format(keyword), 'r', encoding='utf-8')
# #     print('-----------------------------------')
# #     print(df)
# #     @staticmethod
# #     def bulk():
# #         # df = self.df
# #         # print('확인!!: ', df)
# #         # keyword = str(keyword)
# #         # print('확인', keyword)
# #         # df = pd.read_csv('_data.csv')
# #         # df = self.df
# #         print(df.head())
# #         Session = openSession()
# #         session = Session()
# #         craw_df = CrawDf()
# #         df = craw_df.hook()
# #         # print(df.head())
# #         session.bulk_insert_mappings(CrawDto, df.to_dict(orient='records'))
# #         session.commit()
# #         session.close()

# #     @staticmethod
# #     def count():
# #         return session.query(func.count(CrawDto.date)).one()

# #     @staticmethod
# #     def save(craw):
# #         new_craw = CrawDto(no = craw['no'],
# #                            positive = craw['positive'],
# #                            pos_count = craw['pos_count'],
# #                            negative = craw['negative'],
# #                            neg_count = craw['neg_count'],
# #                            stock = craw['stock'])
# #         session.add(new_craw)
# #         session.commit()
# #     print('Ok!')


# # # class CrawTf(object):
# # #     ...
# # # class CrawAi(object):
# # #     ...

# if __name__ == "__main__":
#     ck = CrawKdd()
#     cd = CrawDf()
#     # ck = get_url()
#     cd.data_pro()
#     # c_dto = CrawDto()
    
#     # CrawDao.bulk() # class

# # ============================================================
# # ==================                     =====================
# # ==================      Resourcing     =====================
# # ==================                     =====================
# # ============================================================

# # parser = reqparse.RequestParser()
# # parser.add_argument('no', type = int, required = True,
# #                             help='This field should be a userId')
# # parser.add_argument('positive', type = str, required = True,
# #                             help='This field should be a password')
# # parser.add_argument('pos_count', type = int, required = True,
# #                             help='This field should be a password')
# # parser.add_argument('negative', type = str, required = True,
# #                             help='This field should be a password')
# # parser.add_argument('neg_count', type = int, required = True,
# #                             help='This field should be a password')
# # parser.add_argument('stock', type = str, required = True,
# #                             help='This field should be a password')

# # class Craw(Resource):
# #     @staticmethod
# #     def post():
# #         args = parser.parse_args()
# #         craw = CrawVo()
# #         craw.stock_name = args.stock_name
# #         craw.positive = args.positive
# #         craw.negative = args.negative
#         # service.assign(craw)
#         # print("Predicted Craw")
