from flask_restful import Resource
from flask import jsonify
from flask import request

from com_blacktensor.cop.news.covid.model.covid_news_dao import CovidNewsDao, CovidExtractionWordDao
from com_blacktensor.cop.news.covid.model.covid_news_df import CovidNewsDf
from com_blacktensor.cop.news.covid.model.covid_news_kdd import CovidNewsKDD

from com_blacktensor.util.checker import Checker
from com_blacktensor.util.file_handler import FileHandler as handler

import threading
import time
# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
class CovideNews(Resource):   
    
    def __init__(self):
        self.news_dao = CovidNewsDao()
        self.word_dao = CovidExtractionWordDao()
        self.df = CovidNewsDf()

    def get(self):

        params = request.get_json()
        keyword = params['keyword']

        if keyword is not None:
            
            count = self.news_dao.count()

            if count == 0:
                crawer = CovidNewsKDD()
                print('get urls start')
                start_time = time.time()
                urls = crawer.get_naver_news_urls(keyword)
                print(f'get urls end. processing time : {time.time() - start_time}s')

                if not Checker.check_folder_path('./csv'):
                    handler.crete_folder('./csv')
                
                handler.save_to_csv('./csv/result_Covid19_urls.csv', urls, ['urls'], 'utf-8-sig')

                # url_df = handler.load_to_csv('./csv/result_Covid19_urls.csv', 'utf-8-sig')
                # urls = url_df['urls'].tolist()

                print('get contents from urls start')
                
                start_time = time.time()
                
                result_list = []
                thread_count = 5
                thread_list = []
                div_count = int(len(urls) / thread_count)   # 600

                for idx in range(0, thread_count):
                    start_idx = idx * div_count
                    end_idx = (start_idx + div_count)

                    div_url = urls[int(start_idx):int(end_idx)]

                    thread = threading.Thread(target=crawer.get_contents_from_naver_urls, args=(div_url, result_list))
                    thread_list.append(thread)
                    thread.start()
                
                for thread in thread_list:
                    thread.join()

                print(f'get contents from urls end. processing time : {time.time() - start_time}s')
                
                if not Checker.check_folder_path('./csv'):
                    handler.crete_folder('./csv')
                
                handler.save_to_csv('./csv/result_covid19_news.csv', result_list, ['time','contents'], 'utf-8-sig')

                df = self.df.get_df_news(result_list)
                # df = handler.load_to_csv('./csv/result_Covid19_News.csv', 'utf-8-sig')
                # print(df)
                # print(df.isnull().values.any())
                # counter = df['contents'].isnull().sum()
                # print(f'contents is non : {counter}')
                # counter = df['time'].isnull().sum()
                # print(f'time is non : {counter}')
                self.news_dao.save_data_bulk(df)

            wordcount = self.word_dao.count()

            if wordcount == 0:
                df = self.df.get_df_news_word('./csv/result_covid19_news.csv', 'utf-8-sig')
                # print(df)
                
                self.word_dao.save_data_bulk(df)

            result = self.word_dao.find_all()
            return jsonify([item.json for item in result])
            # result = self.news_dao.find_all()
            # return jsonify(json_list=[item.json for item in result])