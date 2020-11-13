from sqlalchemy import Column, Integer, String, Date
from com_blacktensor.ext.db import db

import datetime

# ============================================================
# ==================                     =====================
# ==================       Modeling      =====================
# ==================                     =====================
# ============================================================
class EconomyNewsDto(db.Model):
    __tablename__ = 'economy_news'
    
    no = Column(Integer, primary_key=True)
    time = Column(Date)
    contents = Column(String(5000))
    
    def __repr__(self):
        timestr = self.createTime.strftime('%Y-%m-%d')
        return f'no : {self.no}, time : {timestr}, contents : {self.contents}'
    
    @property
    def json(self):
        return {
            'no': self.no,
            'time': self.time.strftime('%Y-%m-%d'),
            'contents': self.contents
        }

class EconomyExtractionWordDto(db.Model):
    __tablename__ = 'economy_extraction_words'
    
    no = Column(Integer, primary_key=True)
    time = Column(Date, default=datetime.date.today().strftime('%Y%m%d'))
    word = Column(String(100))
    count = Column(Integer)
    
    def __repr__(self):
        timestr = self.time.strftime('%Y-%m-%d')
        return f'no : {self.no}, time : {timestr}, word : {self.word}, count: {self.count}'
    
    @property
    def json(self):
        return {
            'no': self.no,
            'time': self.time.strftime('%Y-%m-%d'),
            'word': self.word,
            'count': self.count,
        }