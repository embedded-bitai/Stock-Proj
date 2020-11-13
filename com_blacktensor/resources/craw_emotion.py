# import requests
# import pandas as pd
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
# date_text = []
# # ### HeadLine
# class EmotionKdd(object):
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
#     df.loc[:, 'keyword'] = keyword
#     print(df.head())
#     df.to_csv(keyword + '.csv', encoding='utf8')
# '''
# 0   논어, 새로운 가르침에 겁내지 않으려면 그간의 가르침을 실행해야 한다!       
# 1  "전 세계 AI 전문가 모여라"…'삼성 AI 포럼 2020' 온라인 개최
# 2              비트코인 지갑서비스 사업자도 자금세탁방지 의무 부과
# 3                  [연합뉴스 이 시각 헤드라인] - 12:00
# 4   “이건희 회장의 ‘도전 DNA’ 계승… 판도 바꾸는 기업으로 진화하자”
# '''


# # # =======================================================================================================================================

# # # # title_text = []
# # # # link_text = []
# # # # source_text = []
# # # # date_text = []
# # # # contents_text = []

# # # def main():
# # #     info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+" 시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
# # #     maxpage = input("최대 크롤링할 페이지 수 입력하시오: ")
# # #     query = input("검색어 입력: ")
# # #     sort = input("뉴스 검색 방식 입력(관련도순=0 최신순=1 오래된순=2): ") #관련도순=0 최신순=1 오래된순=2
# # #     s_date = input("시작날짜 입력(2019.01.04):") #2019.01.04
# # #     e_date = input("끝날짜 입력(2019.01.05):") #2019.01.05
# # #     crawler(maxpage, query, sort, s_date, e_date)
# # # main()

# # # def crawler(maxpage, query, sort, s_date, e_date):
# # #     s_from = s_date.replace(".","")
# # #     e_to = e_date.replace(".","")
# # #     page = 1
# # #     maxpage_t =(int(maxpage)-1)*10+1 # 11= 2페이지 21=3페이지 31=4페이지 ...81=9페이지 , 91=10페이지, 101=11페이지

# # #     while page <= maxpage_t:
# # #         url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
# # #         response = requests.get(url)
# # #         html = response.text

# # #         #뷰티풀소프의 인자값 지정
# # #         soup = BeautifulSoup(html, 'html.parser')

# # #         #태그에서 제목과 링크주소 추출
# # #         atags = soup.select('.news_tit')
# # #         for atag in atags:
# # #             title_text.append(atag.text)
# # #             link_text.append(atag['href'])

# # #         #신문사 추출
# # #         source_lists = soup.select('.thumb_box')
# # #         for source_list in source_lists:
# # #             source_text.append(source_list.text)

# # #         #날짜 추출
# # #         date_lists = soup.select('.info')
# # #         for date_list in date_lists:
# # #             test=date_list.text
# # #             date_cleansing(test)

# # #         #본문요약본
# # #         contents_lists = soup.select('a.api_txt_lines.dsc_txt_wrap')
# # #         for contents_list in contents_lists:
# # #             #print('==='*40)
# # #             #print(contents_list)
# # #             contents_cleansing(contents_list)

# # #         #모든 리스트 딕셔너리형태로 저장
# # #         result= {"date" : date_text , "title":title_text , "source" : source_text ,"contents": contents_text ,"link":link_text }
# # #         print(page)

# # #         df = pd.DataFrame(result) #df로 변환
# # #         page += 10

# # # #날짜 정제화 함수
# # # def date_cleansing(test):
# # #     try:
# # #         pattern = '\d+.(\d+).(\d+).'
# # #         r = re.compile(pattern)
# # #         match = r.search(test).group(0) # 2018.11.05.
# # #         date_text.append(match)
# # #     except AttributeError:

# # #         pattern = '\w* (\d\w*)'

# # #         r = re.compile(pattern)
# # #         match = r.search(test).group(1)
# # #         #print(match)
# # #         date_text.append(match)

# # # #내용 정제화 함수
# # # def contents_cleansing(contents):
# # #     first_cleansing_contents = re.sub('<dl>.*?</a> </div> </dd> <dd>', '',
# # #     str(contents)).strip()
# # #     second_cleansing_contents = re.sub('<ul class="relation_lst">.*?</dd>', '',
# # #     first_cleansing_contents).strip()
# # #     third_cleansing_contents = re.sub('<.+?>', '', second_cleansing_contents).strip()
# # #     contents_text.append(third_cleansing_contents)
# # #     #print(contents_text)


# # # #엑셀로 저장하기 위한 변수
# # # RESULT_PATH ='C:/Users/User/Desktop/python study/beautifulSoup_ws/crawling_result/'
# # # now = datetime.now()

# # # # 새로 만들 파일이름 지정
# # # outputFileName = '%s-%s-%s %s시 %s분 %s초 merging.xlsx' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
# # # df.to_excel(RESULT_PATH+outputFileName,sheet_name='sheet1')

# # # ============================================================
# # # ==================                     =====================
# # # ==================    Preprocessing    =====================
# # # ==================                     =====================
# # # ============================================================
# class EmotionDf(object):
#     def __init__(self):
#         self.ek = EmotionKdd()
#         this = self.ek
#         self.keyword = this.keyword
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

#         df = pd.concat([po_df,ne_df], axis=1)

#         df.loc[:, 'keyword'] = keyword

#         print(df.head())
#         df.to_csv(keyword + '_word.csv', encoding='utf8')



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
# # class EmotionDto(db.Model):
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

# # # class EmotionVo:
# # #     no = int = 0
# # #     date : str = ''
# # #     stock_name : str = ''
# # #     positive : str = ''
# # #     negative : str = ''


# # Session = openSession()
# # session = Session()
# # emotion_df = EmotionDf()


# # class EmotionDao(EmotionDto):
    
# #     @staticmethod
# #     def bulk():
# #         Session = openSession()
# #         session = Session()
# #         emotion_df = EmotionDf()
# #         df = emotion_df.hook()
# #         # print(df.head())
# #         session.bulk_insert_mappings(EmotionDto, df.to_dict(orient='records'))
# #         session.commit()
# #         session.close()

# #     @staticmethod
# #     def count():
# #         return session.query(func.count(EmotionDto.date)).one()

# #     @staticmethod
# #     def save(emotion):
# #         new_craw = CrawDto(date = emotion['date'],
# #                            stock_name = emotion['stock_name'],
# #                            positive = emotion['positive'],
# #                            negative = emotion['negative'])
# #         session.add(emotion)
# #         session.commit()

# # # class EmotionTf(object):
# # #     ...
# # # class EmotionAi(object):
# # #     ...


# # if __name__ == "__main__":
# #     ck = EmotionKdd()
# #     cd = EmotionDf()
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

# # # class Emotion(Resource):
    
# # #     @staticmethod
# # #     def post():
# # #         args = parser.parse_args()
# # #         emotion = EmotionVo()
# # #         emotion.stock_name = args.stock_name
# # #         emotion.positive = args.positive
# # #         emotion.negative = args.negative
# # #         # service.assign(emotion)
# # #         # print("Predicted Craw")

# # class Emotion(Resource):
     
# #      def __init__(self):
# #         self.dao = EmotionDao()
        
# #      def get(self):        
# #         result = self.dao.find_all()
# #         return jsonify(json_list=[item.json for item in result])
# # =========================================================================================================================
# class EmotionDto(db.Model):
#     __tablename__ = 'stock'
#     __table_args__={'mysql_collate' : 'utf8_general_ci'}
#     no : int = db.Column(db.Integer, primary_key = True, index = True)
#     positive : str = db.Column(db.String(10), primary_key = True, index = True)
#     pos_count : int = db.Column(db.Integer)
#     negative : str = db.Column(db.String(10))
#     neg_count : int = db.Column(db.Integer)
#     stock : str = db.Column(db.String(10))

#     def __init__(self, no, positive, pos_count, negative, neg_count, stock):
#         self.no = no
#         self.positive = positive
#         self.pos_count = pos_count
#         self.negative = negative
#         self.neg_count = neg_count
#         self.stock = stock
    
#     def __repr__(self):
#         return f'Stock(no={self.no}, positive={self.positive}, pos_count{self.pos_count}, \
#                negative={self.negative}, neg_count={self.neg_count}, stock={self.stock})'

#     def json(self):
#             return {
#                 'no' : self.no,
#                 'positive' : self.positive,
#                 'pos_count' : self.pos_count,
#                 'negative' : self.negative,
#                 'neg_count' : self.neg_count,
#                 'stock' : self.stock
#             }

# class EmotionVo:
#     no : int = 0
#     positive : str = ''
#     pos_count : int = 0
#     negative : str = ''
#     neg_count : int = 0
#     stock : str = ''



# Session = openSession()
# session = Session()
# emotion_df = EmotionDf()


# class EmotionDao(EmotionDto):
#     ck = EmotionKdd()
#     this = ck
#     keyword = this.keyword
#     print("DAO: ", keyword)
#     # cd = EmotionDf()
#     # this = cd.DataPro()
#     # data = this.df
#     # print("DAO DATA: ", data)
#     # keyword = str(keyword)
#     # df = pd.read_csv(keyword, '_data.csv')
#     # df = pd.read_csv(keyword, '.csv')
#     df = pd.read_csv('{}_word.csv'.format(keyword), encoding='utf-8')
#     df = df.drop([df.columns[0]], axis=1)
#     # df = open('{}.csv'.format(keyword), 'r', encoding='utf-8')
#     print('-----------------------------------')
#     print(df)
#     @staticmethod
#     def bulk():
#         # df = self.df
#         # print('확인!!: ', df)
#         # keyword = str(keyword)
#         # print('확인', keyword)
#         # df = pd.read_csv('_data.csv')
#         # df = self.df
#         print(df.head())
#         Session = openSession()
#         session = Session()
#         emotion_df = EmotionDf()
#         df = emotion_df.hook()
#         # print(df.head())
#         session.bulk_insert_mappings(EmotionDto, df.to_dict(orient='records'))
#         session.commit()
#         session.close()

#     @staticmethod
#     def count():
#         return session.query(func.count(EmotionDto.date)).one()

#     @staticmethod
#     def save(emotion):
#         new_emotion = EmotionDto(no = emotion['no'],
#                            positive = emotion['positive'],
#                            pos_count = emotion['pos_count'],
#                            negative = emotion['negative'],
#                            neg_count = emotion['neg_count'],
#                            stock = emotion['stock'])
#         session.add(new_emotion)
#         session.commit()
#     print('Ok!')


# # class EmotionTf(object):
# #     ...
# # class EmotionAi(object):
# #     ...

# if __name__ == "__main__":
#     ck = EmotionKdd()
#     cd = EmotionDf()
#     cd.data_pro()
#     # c_dto = EmotionDto()
    
#     EmotionDao.bulk() # class

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

# # class Emotion(Resource):
# #     @staticmethod
# #     def post():
# #         args = parser.parse_args()
# #         emotion = EmotionVo()
# #         emotion.stock_name = args.stock_name
# #         emotion.positive = args.positive
# #         emotion.negative = args.negative
# #         service.assign(emotion)
# #         print("Predicted emotion")
