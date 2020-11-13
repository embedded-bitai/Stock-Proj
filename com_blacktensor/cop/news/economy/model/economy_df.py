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
class EconomyNewsDf(object):
    
    def get_df_news(self, news):
        return DataFrame(news, columns=['time', 'contents'])

    def get_df_news_word(self, filePath, encoding):
        df = handler.load_to_csv(filePath, encoding)
        contents = df['contents'].tolist()
        # times = df['time'].tolist()

        print('list load end')

        total = []
        stopWords = ['크게', '여기', '서울', '정부', '위원회', '사업', '한국', '옵티머스', '의원', '금융감독원', '국회', '지난']
        
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
        noun_list = count.most_common(10)

        print('noun_list load end')

        for value in noun_list:
            print(value)

        # print('create wordclude')
        # wc = WordCloud(font_path='./font/NanumBarunGothic.ttf', background_color="white", width=1000, height=1000, max_words=50, max_font_size=300)
        # wc.generate_from_frequencies(dict(noun_list))

        # wc.to_file('wordCloud.png')

        colnames = ['word', 'count']
        
        if not Checker.check_folder_path('./csv'):
                handler.crete_folder('./csv')
            
        handler.save_to_csv('./csv/result_economy_news_word.csv', noun_list, colnames, 'utf-8-sig')

        return pd.DataFrame(noun_list, columns=colnames)
