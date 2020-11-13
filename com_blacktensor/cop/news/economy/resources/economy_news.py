from flask_restful import Resource
from flask import jsonify

from com_blacktensor.cop.news.economy.model.economy_kdd import EconomyNewsKdd
from com_blacktensor.cop.news.economy.model.economy_df import EconomyNewsDf
from com_blacktensor.cop.news.economy.model.economy_dao import EconomyNewsDao, EconomyExtractionWordDao

from com_blacktensor.util.checker import Checker
from com_blacktensor.util.file_handler import FileHandler as handler

import threading

class EconomyNews(Resource):
    
    def __init__(self):
        self.news_dao = EconomyNewsDao()
        self.word_dao = EconomyExtractionWordDao()
        self.df = EconomyNewsDf()

    def get(self):

        econmoy_news_count = self.news_dao.count()

        if econmoy_news_count == 0:
            kdd = EconomyNewsKdd()
            urls = kdd.get_economy_news_urls()
            # print(datas)

            if not Checker.check_folder_path('./csv'):
                handler.crete_folder('./csv')
                    
            handler.save_to_csv('./csv/result_economy_urls.csv', urls, ['urls'], 'utf-8-sig')

            result_list = []
            thread_count = 6
            thread_list = []
            div_count = int(len(urls) / thread_count)   # 600

            for idx in range(0, thread_count):
                start_idx = idx * div_count
                end_idx = (start_idx + div_count)

                div_url = urls[int(start_idx):int(end_idx)]

                thread = threading.Thread(target=kdd.get_contents_from_economy_urls, args=(div_url, result_list))
                thread_list.append(thread)
                thread.start()
            
            for thread in thread_list:
                thread.join()

            if not Checker.check_folder_path('./csv'):
                handler.crete_folder('./csv')
            
            handler.save_to_csv('./csv/result_economy_news.csv', result_list, ['time','contents'], 'utf-8-sig')
            df = self.df.get_df_news(result_list)
            self.news_dao.save_data_bulk(df)
        
        econmoy_word_count = self.word_dao.count()
        if econmoy_word_count == 0:
            df = self.df.get_df_news_word('./csv/result_economy_news.csv', 'utf-8-sig')
            self.word_dao.save_data_bulk(df)
        
        result = self.word_dao.find_all()
        return jsonify([item.json for item in result])

        


