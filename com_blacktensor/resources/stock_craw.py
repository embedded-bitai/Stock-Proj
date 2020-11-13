# import csv
# import pandas as pd
# # # from sqlalchemy import create_engine
# from com_blacktensor.ext.db import db, openSession, engine
# from sqlalchemy import func
# # from com_blacktensor.ext.routes import Resource

# # # # ============================================================
# # # # ==================                     =====================
# # # # ==================         KDD         =====================
# # # # ==================                     =====================
# # # # ============================================================
# class StockKdd(object):
#     keyword = input("검색어 입력: ")

#     # def __init__(self):
#     #     self.sk = StockKdd()
#     #     self.keyword = keyword
#     #     self.code_df = code_df
#     #     self.code_name = code_name

#     # def get_code(self, keyword, code_df):
#         # print("get_code: ", keyword)
#     code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13',header=0)[0]
#     #
#     # self.code = self.code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False).strip()
#     # self.url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
#     #
#     # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해둠
#     code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

#     # 회사명과 종목코드 필요 -> 그 이외에 필요 없는 column 제외
#     code_df = code_df[['회사명', '종목코드']]

#     # 한글로된 컬럼명을 영어로 변환
#     code_df = code_df.rename(columns={'회사명' : 'name', '종목코드' : 'code'})
#     code_df.head() 
#     print(code_df.head())

#     # https://finance.naver.com/item/sise.nhn?code=005930(삼성전자)
#     def get_url(self, keyword, code_df):
#         # item_name = self.item_name
        
#         # this = self.sk
#         # this.code_name = code_name
#         code = code_df.query("name=='{}'".format(keyword))['code'].to_string(index=False)
#         code = code.strip()

#         url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
        
#         print("요청 URL = {}".format(url))
#         return url

#     url = get_url(0, keyword, code_df)

#     df = pd.DataFrame()

#     for page in range(1, 16): 
#         pg_url = '{url}&page={page}'.format(url=url, page=page) 
#         df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)
#         # df = df.append({'stock' : keyword}, ignore_index=True)

#     df = df.dropna()

#     df = df.drop(columns= {'전일비', '시가', '고가', '저가'})

#     # print(df.head())
#     print(df)

#     df = df.rename(columns= {
#         '날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open',
#         '고가': 'high', '저가': 'low', '거래량': 'volume'
#         })

#     # df.drop(['diff', 'open', 'high', 'low'], axis=1, inplace=True)

#     # 데이터 타입 int 변환
#     df[['close', 'volume']] \
#         = df[['close', 'volume']].astype(int)

#     # df.drop(['diff', 'open', 'high', 'low'], axis=0, inplace=True)

#     # date를 date type 변환
#     df['date'] = pd.to_datetime(df['date'])

#     # date 기준으로 내림차순 sort
#     df = df.sort_values(by=['date'], ascending=False)

#     df.loc[:, 'stock'] = keyword

#     # df.head()
#     print('-------------------- head -------------------')
#     print(df.head())
#     print('\n-------------------- 전체 -------------------')
#     print(df)

#     # csv file 저장
#     # df.to_csv(keyword, '.csv', mode = 'a', header = False)
#     df.to_csv(keyword + '_data.csv', encoding='utf8')

# # # # ============================================================
# # # # ==================                     =====================
# # # # ==================    Preprocessing    =====================
# # # # ==================                     =====================
# # # # ============================================================
# class StockDf(object):
    
#     def __init__(self, colums):
#         self.colums = colums

#     def get_df(self, data):
#         return pd.DataFrame(data, columns=self.colums)

# # ============================================================
# # ==================                     =====================
# # ==================       Modeling      =====================
# # ==================                     =====================
# # ============================================================
# class StockDto(db.Model):
#     __tablename__ = 'stock'
#     __table_args__={'mysql_collate' : 'utf8_general_ci'}

#     date : str = db.Column(db.String(10), primary_key = True, index = True)
#     keyword : str = db.Column(db.String(10))
#     close : int = db.Column(db.Integer)
#     volume : int = db.Column(db.Integer)

#     def __init__(self, date, keyword, close, volume):
#         self.date = date
#         self.keyword = keyword
#         self.close = close
#         self.volume = volume
    
#     def __repr__(self):
#         return f'Stock(date={self.date}, keyword={self.keyword}, close={self.close}, volume={self.volume})'

# class StockVo:
#     date : str = ''
#     keyword : str = ''
#     close : int = 0
#     volume : int = 0


# Session = openSession()
# session = Session()
# # stock_df = StockDf()


# class StockDao(StockDto):
    
#     @staticmethod
#     def bulk():
#         Session = openSession()
#         session = Session()
#         stock_df = StockDf()
#         df = stock_df.hook()
#         # print(df.head())
#         session.bulk_insert_mappings(StockDto, df.to_dict(orient='records'))
#         session.commit()
#         session.close()

#     @staticmethod
#     def count():
#         return session.query(func.count(StockDto.date)).one()

#     @staticmethod
#     def save(stock):
#         new_stock = StockDto(date = stock['date'],
#                            keyword = stock['keyword'],
#                            close = stock['close'],
#                            volume = stock['volume'])
#         session.add(new_stock)
#         session.commit()


# # class StockTf(object):
# #     ...
# # class StockAi(object):
# #     ...
# # ============================================================
# # ==================                     =====================
# # ==================      Resourcing     =====================
# # ==================                     =====================
# # ============================================================
# # # # class Stock(Resource):
# # # #     ...

