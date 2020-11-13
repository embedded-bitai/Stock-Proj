from com_blacktensor.util.file_handler import FileHandler as handler
from com_blacktensor.util.checker import Checker

import datetime
import pandas as pd
from pandas import DataFrame

from konlpy.tag import Okt
from collections import Counter
# from wordcloud import WordCloud

# ============================================================
# ==================                     =====================
# ==================    Preprocessing    =====================
# ==================                     =====================
# ============================================================
class CovidNewsDf(object):

    def get_df_news(self, news):
        return DataFrame(news, columns=['time', 'contents'])

    def get_df_news_word(self, filePath, encoding):
        df = handler.load_to_csv(filePath, encoding)
        contents = df['contents'].tolist()
        # times = df['time'].tolist()

        print('list load end')

        total = []
        stopWords = ['지난', '진자', '판정', '대통령', '위해', '지역', '사람', '관련', '이후', '대해', '개발', '올해', '당국', 
                     '경우', '국내', '때문', '조사', '최근', '이번', '확인', '증가', '진행', '통해', '신종', '지난달', '대상'
                     '단계', '우리', '상황', '현재', '조치']

        okt = Okt()

        for content in contents:
            content = str(content)
        #     print(f'content : {content}')
            # noun = okt.nouns(content)
            morph = okt.pos(content)
                                   
            for word, tag in morph:
                if tag in ['Noun'] and len(word) > 1 and word not in stopWords:
                    total.append(word)
            
        count = Counter(total)
        noun_list = count.most_common(30)

        print('noun_list load end')

        if not Checker.check_folder_path('./csv'):
                handler.crete_folder('./csv')
            
        handler.save_to_csv('./csv/result_covid_news_word.csv', noun_list, ['word','count'], 'utf-8-sig')

        # for value in noun_list:
        #     print(value)

        # print('create wordclude')
        # wc = WordCloud(font_path='./font/NanumBarunGothic.ttf', background_color="white", width=1000, height=1000, max_words=50, max_font_size=300)
        # wc.generate_from_frequencies(dict(noun_list))

        # wc.to_file('wordCloud.png')

        colnames = ['word', 'count']
        
        return pd.DataFrame(noun_list, columns=colnames)