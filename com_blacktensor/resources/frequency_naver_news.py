from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from com_blackTensor.util.file_hander import FileHandler as handler

class FrequencyNaverNews:

    def get(self):
        return self.frequency_naver_news('./result_naverCrawContent.csv', 'utf-8-sig')
    
    def frequency_naver_news(self, filePath, encoding):
        df = handler.load_to_csv(filePath, encoding)
        contents = df['content'].tolist()

        print('list load end')

        total = []

        okt = Okt()
        for content in contents:
            content = str(content)
            content = content.replace("\n","")
        #     print(f'content : {content}')
            noun = okt.nouns(content)
            
            for i,v in enumerate(noun):
                if len(v)<2:
                    noun.pop(i)
            
            total.extend(noun)
            
        count = Counter(total)
        noun_list = count.most_common(100)

        print('noun_list load end')

        for value in noun_list:
            print(value)

        colnames = ['word', 'count']

        return pd.DataFrame(noun_list, columns=colnames)