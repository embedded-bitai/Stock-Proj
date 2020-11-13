import requests
import pandas as pd
import codecs
import numpy as np
import re
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from collections import Counter
from com_blacktensor.ext.db import db, openSession
from sqlalchemy import func
import json

from sqlalchemy import Column, Integer, String, Date
from com_blacktensor.cop.emo.model.emotion_kdd import EmotionKdd
from com_blacktensor.cop.emo.model.emotion_dto import EmotionDto, StockNewsDto
from com_blacktensor.cop.emo.model.emotion_dfo import EmotionDfo
from com_blacktensor.cop.emo.model.emotion_kdd import keyword

# import time
# import multiprocessing


Session = openSession()
session = Session()

class EmotionDao(EmotionDto):
    # @classmethod
    # def bulk(cls, emotion_dfo):
    #     dfo = emotion_dfo.data_pro(0, keyword)
    #     print('--------Emotion----------')
    #     print(dfo.head())
    #     session.bulk_insert_mappings(cls, dfo.to_dict(orient="records"))
    #     session.commit()
    #     session.close()

    @staticmethod
    def bulk():
        emotion_dfo = EmotionDfo()
        dfo = emotion_dfo.data_pro(keyword)
        session.bulk_insert_mappings(EmotionDto, dfo.to_dict(orient='records'))
        session.commit()
        session.close()

    @staticmethod
    def save(emotion):
        session.add(emotion)
        session.commit()

    @classmethod
    def update(cls, emotion):
        # session.query(cls).filter(cls.keyword == emotion['keyword'])\
        emotion = session.query(cls).filter(cls.keyword == keyword).first()\
                .update({cls.no : emotion['no'],\
                cls.positive:emotion['positive'],\
                cls.pos_count:emotion['pos_count'],\
                cls.negative:emotion['negative'],\
                cls.neg_count:emotion['neg_count']})                                                        
        session.commit()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.no)).one()

    # @classmethod
    # def find_insert(cls, emotion, keyword):
    #     session.query(cls).filter_by(cls.keyword == emotion['keyword']).last()\
    #         .insert({cls.no : emotion['no'],\
    #             cls.positive:emotion['positive'],\
    #             cls.pos_count:emotion['pos_count'],\
    #             cls.negative:emotion['negative'],\
    #             cls.neg_count:emotion['neg_count'],\
    #             cls.keyword:emotion['keyword']})
            # if session.query(cls).filter(cls.keyword != keyword):
            # emotion_dfo = EmotionDfo()
            # dfo = emotion_dfo.data_pro(keyword)
            # session.bulk_insert_mappings(EmotionDto, dfo.to_dict(orient='records'))
            # session.commit()
            # session.close()

        # return session.query(cls).all()

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    # @classmethod
    # def find_x(cls, keyword):
    #     # session.query(cls).filter(cls.keyword != keyword).last()
    #     # session.query(cls).filter(cls.keyword.like('keyword'))
    #     session.query(cls).filter(cls.keyword != keyword)
    #     session.close()
    #     return 0

    # @classmethod
    # def find_y(cls, keyword):
    #     # session.query(cls).filter(cls.keyword != keyword).last()
    #     # session.query(cls).filter(cls.keyword.like('keyword'))
    #     session.query(cls).filter(cls.keyword == keyword)
    #     session.close()
    #     return 0

    # @classmethod
    # def find_like(cls, keyword):
    #     # session.query(cls).filter(cls.keyword.like('%'+keyword+'%'))
    #     session.query(cls).filter(cls.keyword.like('%'+keyword+'%'))
    #     print(cls.keyword)
    #     session.close()
    #     return 0

    # # @classmethod
    # # def match(cls, keyword):
    # @staticmethod
    # def match(emotion, keyword):
    #     a = session.query(EmotionDto).filter(EmotionDto.keyword == keyword).all()
    #     print('===========확인1==========')
    #     print(a)
    #     print('===========확인2==========')
    #     print(EmotionDto.keyword)
    #     print('===========확인3==========')
    #     print(keyword)
    #     session.commit()
    #     session.close()
    #     return 0

    @classmethod
    def find_update(cls, keyword):
        emotion = session.query(cls).filter(cls.keyword == keyword).first()
        # emotion.positive += 1
        # emotion.pos_count += 1
        # emotion.negative += 1
        # emotion.neg_count += 1
        # emotion.keyword += 1
        # session.commit()
    @classmethod
    def find_by_keyword(cls, keyword):
        print('==============find_by_keyword================')
        a = cls.query.filter(cls.keyword != keyword).all()
        b = cls.query.filter(cls.keyword == keyword).all()
        if a: 
            # emotion = session.query(cls).filter(cls.keyword == keyword).first()
            # emotion.positive += 1
            # emotion.pos_count += 1
            # emotion.negative += 1
            # emotion.neg_count += 1
            # session.commit()
            return 0
        elif b:
            print('------------중복--------------')
            # emotion = session.query(cls).filter(cls.keyword == keyword).first()
            # emotion.positive += 1
            # emotion.pos_count += 1
            # emotion.negative += 1
            # emotion.neg_count += 1
            # session.commit()
            return 1
            # print(a)
            # print(type(a))
            # print(keyword)
            # print(type(keyword))
            # print(df)
            # print(type(df))
        # for word in a:
        #     if keyword in word:
        #         print('ok')
        #         s.append(keyword)
        #         break;        
        # print(s)
        # if any(keyword in word for word in a):
        #     print('ok')
        # print('===========s확인1==========')
        # print(s)
        
        # return cls.query.filter(EmotionDto.keyword == keyword).all()


    @staticmethod
    def test():
        print(' TEST SUCCESS !!')

class StockNewsDao(StockNewsDto):
    @staticmethod
    def bulk():
        emotion_dfo = EmotionDfo()
        df = emotion_dfo.get_df(keyword)
        session.bulk_insert_mappings(StockNewsDto, df.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def save(emotion):
        session.add(emotion)
        session.commit()
    
    @staticmethod
    def count():
        return session.query(func.count(StockNewsDto.no)).one()

    @classmethod
    def find_all(cls):

        result = session.query(StockNewsDto).all()
        session.close()

        return result

# if __name__ == '__main__':
#     EmotionDao.bulk()