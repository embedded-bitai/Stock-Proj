from flask import Flask
from flask_restful import Resource, Api
from hello import HelloWorld

import datetime
import time
import threading

from flask_cors import CORS
from com_blacktensor.ext.routes import initialize_routes
from com_blacktensor.util.checker import Checker 
from com_blacktensor.util.file_handler import FileHandler as handler
from com_blacktensor.ext.db import url, db

from com_blacktensor.cop.emo.model.emotion_kdd import keyword
#Emotion
from com_blacktensor.cop.emo.model.emotion_dao import EmotionDao, StockNewsDao
from com_blacktensor.cop.emo.model.emotion_dfo import EmotionDfo
from com_blacktensor.cop.emo.model.emotion_kdd import EmotionKdd
from com_blacktensor.cop.emo.model.emotion_dto import EmotionDto, StockNewsDto
# Finance
from com_blacktensor.cop.fin.model.finance_dao import FinanceDao
from com_blacktensor.cop.fin.model.finance_dfo import FinanceDfo
from com_blacktensor.cop.fin.model.finance_dto import FinanceDto
from com_blacktensor.cop.fin.model.finance_kdd import FinanceKdd
# Stock
from com_blacktensor.cop.sto.model.stock_dao import StockDao
from com_blacktensor.cop.sto.model.stock_dfo import StockDfo
from com_blacktensor.cop.sto.model.stock_dto import StockDto
from com_blacktensor.cop.sto.model.stock_kdd import StockKdd

# ================================== kain code =====================================
from com_blacktensor.cop.cov.status.model.status_kdd import CovidStatusKdd
from com_blacktensor.cop.cov.status.model.status_df import CovidStatusDf
from com_blacktensor.cop.cov.status.model.status_dao import CovidStatusDao
from com_blacktensor.cop.cov.status.model.status_dto import CovidStatusDto
from com_blacktensor.cop.news.covid.model.covid_news_dto import CovidNewsDto, CovidExtractionWordDto
from com_blacktensor.cop.news.economy.model.economy_dto import EconomyNewsDto, EconomyExtractionWordDto
# ==================================================================================

from com_blacktensor.cop.emo.model import emotion_dfo

from com_blacktensor.ext.db import db, openSession

Session = openSession()
session = Session()

print(f'========================= START 1 ==============================')
EmotionDao.test()

app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})

print(f'========================= START 2 ==============================')
EmotionDao.test()

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

if __name__ == '__main__':
    code_df = FinanceKdd()
    # EmotionDfo.data_pro(0, keyword)
    EmotionDfo.data_pro(0, keyword)
    FinanceKdd.get_finance(0, keyword, code_df)
    # FinanceDfo.fina_pro(keyword)
    

print(f'========================= START 3 ==============================')
EmotionDao.test()

with app.app_context():
    db.create_all()
    emotion = session.query(EmotionDto)
    emotion_find_key = EmotionDao.find_by_keyword(keyword)
    # ====================== kain code ==============================
    status_count = CovidStatusDao.count()
    # ===============================================================
    # emotion_find_x = EmotionDao.find_x(keyword)
    # emotion_find_y = EmotionDao.find_y(keyword)
    # emotion_like = EmotionDao.find_like(keyword)
    # emotion_match = EmotionDao.match(emotion, keyword)
    # emotion_fi_insert = EmotionDao.find_insert(emotion, keyword)
    emotion_count = EmotionDao.count()
    stock_new_count = StockNewsDao.count()
    stock_count = StockDao.count()
    finance_count = FinanceDao.count()
    print(type(keyword))
    print(f'***** Emotion Total Count is {emotion_count} *****')
    if emotion_count[0] == 0:
    # if emotion_find == 0:
        EmotionDao.bulk()
    # elif emotion_find_x == 0:
    # elif emotion_like != 2:
    # elif emotion_match != 3:
    elif emotion_find_key == 0:
        EmotionDao.bulk()
        print('ok!')
    elif emotion_find_key == 1:
        EmotionDao.find_update(keyword)
        # EmotionDao.update()
        print('ok!!')
    # ================================ kain code =======================================
    if status_count == 0:
        endDate = datetime.date.today().strftime('%Y%m%d')
        datas = CovidStatusKdd().get_covid19_status(endDate)

        if len(datas) > 0:
            if not Checker.check_folder_path('./csv'):
                handler.crete_folder('./csv')
            
            keys = list(datas[0].keys())
            handler.save_to_csv('./csv/result_covid19_status.csv', datas, keys, 'utf-8-sig')

            df = CovidStatusDf(keys).get_dataframe(datas)
            CovidStatusDao.save_data_bulk(df)
    # ===================================================================================
    # EmotionDao.emotion_fi_insert()
    # EmotionDao.find_insert(EmotionDto, keyword)


        # session.query(cls).filter(cls.keyword == emotion['keyword'])\
        # if emotion_find == 0:
            # EmotionDao.find_insert()
        # session.query(emotion).filter(emotion.keyword == keyword).last()\
        #     .insert({EmotionDao.no : emotion['no'],\
        #         EmotionDao.positive:emotion['positive'],\
        #         EmotionDao.pos_count:emotion['pos_count'],\
        #         EmotionDao.negative:emotion['negative'],\
        #         EmotionDao.neg_count:emotion['neg_count'],\
        #         EmotionDao.keyword:emotion['keyword']})

    print(f'***** StockNews Total Count is {stock_new_count} *****')
    if stock_new_count[0] == 0:
        StockNewsDao.bulk()

    print(f'***** Stock Total Count is {stock_count} *****')
    if stock_count[0] == 0:
        StockDao.bulk()

    print(f'***** Finance Total Count is {finance_count} *****')
    if finance_count[0] == 0:
        FinanceDao.bulk()

initialize_routes(api)