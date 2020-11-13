import requests
import pandas as pd
import codecs
import numpy as np
import re
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from collections import Counter

# from sqlalchemy import Column, Integer, String, Date
# # from sqlalchemy import create_engine

from com_blacktensor.util.file_handler import FileHandler
from com_blacktensor.cop.emo.model.emotion_kdd import keyword
# # ============================================================
# # ==================                     =====================
# # ==================    Preprocessing    =====================
# # ==================                     =====================
# # ============================================================
class EmotionDfo(object):
    def __init__(self):
        print('-----------emotionDfo--------------')
        print(keyword)
        self.fileReader = FileHandler()  

    def data_pro(self, keyword):
    # def data_pro(self, keyword):
        print('-----------emotionDfo--------------')

        word = []
        positive_word = []
        negative_word = []
        noun_list =[]
        poflag = []
        neflag = []

        po_key = []
        ne_key = []
        po_val = []
        ne_val = []


        file = open('{}.csv'.format(keyword), 'r', encoding='utf-8-sig')

        lists = file.readlines()
        file.close()
        
        twitter = Twitter()
        morphs = []

        for sentence in lists:
            morphs.append(twitter.pos(sentence))

        # print(morphs)

        pos = codecs.open('positive_words_self.txt', 'rb', encoding='utf-8-sig')

        while True:
            line = pos.readline()
            line = line.replace('\n', '')
            positive_word.append(line)
            # keyword_text.append(line)

            if not line: break
        pos.close()

        neg = codecs.open('negative_words_self.txt', 'rb', encoding='utf-8-sig')

        while True:
            line = neg.readline()
            line = line.replace('\n', '')
            negative_word.append(line)
            # keyword_text.append(line)

            if not line: break
        neg.close()

        for sentence in morphs : 
            for word, text_tag in sentence :
                if text_tag in ['Noun']:
                    noun_list.append(word)
                    for x in positive_word:
                        if x == word: 
                            poflag.append(x)
                        
                    for y in negative_word:
                        if y == word:
                            neflag.append(y)

                #         print("부정적 :", y)
                # if text_tag in ['Noun'] and ("것" not in word) and ("내" not in word) and ("첫" not in word) and \
                #     ("나" not in word) and ("와" not in word) and ("식" not in word) and ("수" not in word) and \
                #     ("게" not in word) and ("말" not in word):
                #      noun_list.append(word)
                    
                # if text_tag in ['Noun'] and ("갑질" not in word) and ("논란" not in word) and ("폭리" not in word) and \
                #     ("허위" not in word) and ("과징금" not in word) and ("눈물" not in word) and ("피해" not in word) and \
                #     ("포화" not in word) and ("우롱" not in word) and ("위반" not in word) and ("리스크" not in word) and \
                #     ("사퇴" not in word) and ("급락" not in word) and ("하락" not in word) and ("폐업" not in word) and \
                #     ("불만" not in word) and ("산재" not in word) and ("닫아" not in word) and ("손해배상" not in word) and \
                #     ("구설수" not in word) and ("적발" not in word) and ("침해" not in word) and ("빨간불" not in word) and \
                #     ("취약" not in word) and ("불명예" not in word) and ("구형" not in word) and ("기소" not in word) and \
                #     ("반토막" not in word) and ("호소" not in word) and ("불매" not in word) and ("냉담" not in word) and \
                #     ("문제" not in word) and ("직격탄" not in word) and ("한숨" not in word) and ("불똥" not in word) and \
                #     ("항의" not in word) and ("싸늘" not in word) and ("일탈" not in word) and ("파문" not in word) and \
                #     ("횡령" not in word) and ("사과문" not in word) and ("여파" not in word) and ("울상" not in word) and \
                #     ("초토화" not in word) and ("급감" not in word) and ("우려" not in word) and ("중단" not in word) and \
                #     ("퇴출" not in word) and ("해지" not in word) and ("일베" not in word) and ("이물질" not in word) and \
                #     ("엉망" not in word) and ("소송" not in word) and ("하락" not in word) and ("매출하락" not in word) and \
                #     ("혐의" not in word) and ("부채" not in word) and ("과징금" not in word) and ("포기" not in word) and \
                #     ("약세" not in word) and ("최악" not in word) and ("손실" not in word) and ("의혹" not in word):
                #     positive_word.append(word)

                # elif text_tag in ['Noun'] and ("MOU" not in word) and ("제휴" not in word) and ("주목" not in word) and \
                #     ("호응" not in word) and ("돌파" not in word) and ("이목" not in word) and ("수상" not in word) and \
                #     ("입점" not in word) and ("인기" not in word) and ("열풍" not in word) and ("진화" not in word) and \
                #     ("대박" not in word) and ("순항" not in word) and ("유치" not in word) and ("1위" not in word) and \
                #     ("출시" not in word) and ("오픈" not in word) and ("돌풍" not in word) and ("인싸" not in word) and \
                #     ("줄서서" not in word) and ("대세" not in word) and ("트렌드" not in word) and ("불티" not in word) and \
                #     ("진출" not in word) and ("체결" not in word) and ("증가" not in word) and ("기부" not in word) and \
                #     ("신제품" not in word) and ("신상" not in word) and ("최고" not in word) and ("새로운" not in word) and \
                #     ("착한" not in word) and ("신기록" not in word) and ("전망" not in word) and ("협력" not in word) and \
                #     ("역대" not in word) and ("상승" not in word) and ("늘어" not in word) and ("승인" not in word):
                #     negative_word.append(word)

        count_po = Counter(poflag)
        count_ne = Counter(neflag)
        po_words = dict(count_po.most_common())
        ne_words = dict(count_ne.most_common())

        # 워드클라우드로 명사만 추출
        '''
        ['창립', '주년', '삼성', '전자', '이건희', '회장', '도전', '혁신', '삼성', '전자', '삼성', '포럼', '개최', '김기남', '대표', 
        '핵심', '기술', '발전', '현', '코스피', '코스닥', '장', '동반', '상승', '덕성', '시스', '웍', '한국', '컴퓨터', '삼성', '전자
        ', '창립', '주년', '기념', '개최', '이재용', '부회장', '불참', '롯데', '하이마트', '온라인', '오늘', '역대', '빅', '하트', ' 
        일', '시작', '손연기', '칼럼', '차', '산업혁명', '시대', '문제', '일자리', '삼성', '전자', '모바일', '신제품', '엑시노스', ' 
        ...
        '멘토', '체험', '활동', '김기남', '삼성', '부회장', '로', '코로나', '해결', '위해', '전세계', '연구자', '협력', '순위', '주식
        ', '부자', '위', '눈앞', '이재용', '뉴', '파워', '프라', '마', '규모', '유상증자', '결정', '삼성', '전자', '창립', '주념', ' 
        기념', '회장', '도전', '혁신', '계승', '삼성', '전자', '창립', '주년', '기념', '개최']
        '''

        po_key = po_words.keys()
        po_val = po_words.values()

        ne_key = ne_words.keys()
        ne_val = ne_words.values()

        print("\n긍정적인 단어 :", po_key, po_val)
        print("부정적인 단어 :", ne_key, ne_val)
        
        po_df = pd.DataFrame(list(po_words.items()), columns=['positive', 'pos_count'])
        ne_df = pd.DataFrame(list(ne_words.items()), columns=['negative', 'neg_count'])

        df = pd.concat([po_df,ne_df], axis=1)

        df.loc[:, 'keyword'] = keyword

#
        df.fillna(0, inplace=True)
#

        print(df.head())
        df.to_csv(keyword + '_word.csv', encoding='utf-8-sig')



        '''
        긍정적인 단어 : {'상승': 141, '인기': 66, '출시': 60, '전망': 36, '오픈': 30, 
        '돌파': 19, '트렌드': 12, '체결': 12, '증가': 12, '역대': 11, '협력': 11, 
        '주목': 11, '미소': 8, '기부': 8, '승인': 6, '최고': 6, '대세': 5, '유치': 4, 
        '수상': 4, '불티': 2, '부상': 2, '순항': 2, '호응': 1, '진출': 1}
        부정적인 단어 : {'급감': 233, '여파': 163, '하락': 162, '피해': 115, 
        '직격탄': 83, '논란': 61, '중단': 41, '손실': 39, '반토 막': 34, '최악': 33, 
        '포기': 32, '폐업': 25, '급락': 25, '우려': 24, '불매': 14, '눈물': 13, '
        매각': 10, '호소': 9, '울상': 7, '문제': 6, '불만': 6, '약세': 5, '한숨': 5, 
        '일베': 4, '해지': 4, '초토화': 3, '참혹': 3, '폐점': 2, '파문': 2, 
        '과징금': 2, '항의': 1, '소송': 1, '불명예': 1, '리스크': 1, '갑질': 1, 
        '침해': 1, '발끈': 1}
        '''
        print('---------------EmotionDfo Success----------------')
        return df



    def get_df(self, keyword):
        # file = open('{}.csv'.format(keyword), 'r', encoding='utf-8-sig')

        news_df = pd.read_csv('{}.csv'.format(keyword), index_col=[0], encoding='utf-8-sig')
        # C:/Users/Admin/VscProject/BlackTensor_Test/

        news_df.rename( columns={'Unnamed: 0':'name'}, inplace=True )
        news_df.to_csv(keyword + '.csv', encoding='utf-8-sig')
        print('-----------------get_df------------------')
        print(news_df)
        return news_df
        # return pd.DataFrame(data, columns=self.colums)
    data_pro(0, keyword)
    # get_df(0, keyword)