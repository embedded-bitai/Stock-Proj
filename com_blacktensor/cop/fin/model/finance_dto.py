import csv
import json
import pandas as pd
from com_blacktensor.ext.db import db, openSession, engine
# from com_blacktensor.ext.routes import Resource

class FinanceDto(db.Model):
    __tablename__ = 'finance'
    __table_args__={'mysql_collate' : 'utf8_general_ci'}
    no : int = db.Column(db.Integer, primary_key = True, index = True)
    name : str = db.Column(db.String(10))
    f_2015_12 : float = db.Column(db.Float)
    f_2016_12 : float = db.Column(db.Float)
    f_2017_12 : float = db.Column(db.Float)
    f_2018_12 : float = db.Column(db.Float)
    f_2019_12 : float = db.Column(db.Float)
    f_2020_12 : float = db.Column(db.Float)
    f_2021_12 : float = db.Column(db.Float)
    f_2022_12 : float = db.Column(db.Float)
    keyword : str = db.Column(db.String(10))

    # def __init__(self, no, name, f_2015_12, f_2016_12, f_2017_12, f_2018_12, f_2019_12, f_2020_12, f_2021_12, f_2022_12, keyword):
    #     self.no = no
    #     self.name = name
    #     self.f_2015_12 = f_2015_12
    #     self.f_2016_12 = f_2016_12
    #     self.f_2017_12 = f_2017_12
    #     self.f_2018_12 = f_2018_12
    #     self.f_2019_12 = f_2019_12
    #     self.f_2020_12 = f_2020_12
    #     self.f_2021_12 = f_2021_12
    #     self.f_2022_12 = f_2022_12
    #     self.keyword = keyword
    
    def __repr__(self):
        return f'Finance(no={self.no}, name={self.name}, f_2015_12={self.f_2015_12}, \
        f_2016_12={self.f_2016_12}, f_2017_12={self.f_2017_12}, f_2018_12={self.f_2018_12}, \
        f_2019_12={self.f_2019_12}, f_2020_12={self.f_2020_12}, f_2021_12={self.f_2021_12}, \
        f_2022_12={self.f_2022_12}, keyword={self.keyword})'

    def __str__(self):
        return f'Finance(no={self.no}, name={self.name}, f_2015_12={self.f_2015_12}, \
        f_2016_12={self.f_2016_12}, f_2017_12={self.f_2017_12}, f_2018_12={self.f_2018_12}, \
        f_2019_12={self.f_2019_12}, f_2020_12={self.f_2020_12}, f_2021_12={self.f_2021_12}, \
        f_2022_12={self.f_2022_12}, keyword={self.keyword})'

    @property
    def json(self):
        return {
        'no' : self.no,
        'name' : self.name,
        'f_2015_12' : self.f_2015_12,
        'f_2016_12' : self.f_2016_12,
        'f_2017_12' : self.f_2017_12,
        'f_2018_12' : self.f_2018_12,
        'f_2019_12' : self.f_2019_12,
        'f_2020_12' : self.f_2020_12,
        'f_2021_12' : self.f_2021_12,
        'f_2022_12' : self.f_2022_12,
        'keyword' : self.keyword
    }

class FinanceVo:
    no : int = 0
    name : str = ''
    f_2015_12 : float = 0.0
    f_2016_12 : float = 0.0
    f_2017_12 : float = 0.0
    f_2018_12 : float = 0.0
    f_2019_12 : float = 0.0
    f_2020_12 : float = 0.0
    f_2021_12 : float = 0.0
    f_2022_12 : float = 0.0
    keyword : str = ''