import csv
import json
import pandas as pd
from com_blacktensor.ext.db import db, openSession, engine
# from com_blacktensor.ext.routes import Resource

class EmotionDto(db.Model):
    __tablename__ = 'emotion'
    __table_args__={'mysql_collate' : 'utf8_general_ci'}
    no : int = db.Column(db.Integer, primary_key = True, index = True)
    positive : str = db.Column(db.String(10))
    pos_count : int = db.Column(db.Integer)
    negative : str = db.Column(db.String(10))
    neg_count : int = db.Column(db.Integer)
    keyword : str = db.Column(db.String(10))

    # def __init__(self, no, positive, pos_count, negative, neg_count, keyword):
    #     self.no = no
    #     self.positive = positive
    #     self.pos_count = pos_count
    #     self.negative = negative
    #     self.neg_count = neg_count
    #     self.keyword = keyword
      
    def __repr__(self):
        return f'Emotion(no={self.no}, positive={self.positive}, pos_count={self.pos_count}, negative={self.negative},\
            neg_count={self.neg_count}, keyword={self.keyword})'

    def __str__(self):
        return f'Emotion(no={self.no}, positive={self.positive}, pos_count={self.pos_count}, negative={self.negative},\
            neg_count={self.neg_count}, keyword={self.keyword})'
            
    @property
    def json(self):
        return {
        'no' : self.no,
        'positive' : self.positive,
        'pos_count' : self.pos_count,
        'negative' : self.negative,
        'neg_count' : self.neg_count,
        'keyword' : self.keyword
    }

class StockNewsDto(db.Model):
    __tablename__ = 'stock_news'
    __table_args__={'mysql_collate' : 'utf8_general_ci'}
    no : int = db.Column(db.Integer, primary_key = True, index = True)
    title : str = db.Column(db.String(100))
    keyword : str = db.Column(db.String(10))

    # def __init__(self, no, positive, pos_count, negative, neg_count, keyword):
    #     self.no = no
    #     self.title = title
    #     self.keyword = keyword
    
    def __repr__(self):
        return f'Emotion(no={self.no}, title={self.title}, keyword={self.keyword})'

    def __str__(self):
        return f'Emotion(no={self.no}, title={self.title}, keyword={self.keyword})'

    @property
    def json(self):
        return {
        'no' : self.no,
        'title' : self.title,
        'keyword' : self.keyword
    }

class EmotionVo:
    no : int = 0
    positive : str = ''
    pos_count : int = 0
    negative : str = ''
    neg_count : int = 0
    keyword : str = ''

class StockNewsVo:
    no : int = 0
    title : str = ''
    keyword : str = ''