import csv
import pandas as pd
import os
from pathlib import Path
# # from sqlalchemy import create_engine
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
from com_blacktensor.util.file_handler import FileHandler
from com_blacktensor.cop.emo.model.emotion_kdd import keyword
# from com_blacktensor.ext.routes import Resource

class FinanceDfo(object):
    def __init__(self):
        print('-----------FinanceDfo--------------')
        self.fileHandler = FileHandler()



    def fina_pro(self, keyword):
        print('----------FinanceDfo----------')
        # df = pd.read_csv('{}_finance.csv'.format(keyword), index_col=[0], encoding='utf-8-sig')
        file = pd.read_csv('{}_finance.csv'.format(keyword), encoding='utf-8-sig')
        # C:/Users/Admin/VscProject/BlackTensor_Test/
        df = pd.DataFrame(file)
        # df.rename( columns={'Unnamed: 0':'name'}, inplace=True )
        df = df.rename(columns= {
        'Unnamed: 0':'name', '2015/12' : 'f_2015_12', '2016/12' : 'f_2016_12', '2017/12' : 'f_2017_12',
        '2018/12' : 'f_2018_12', '2019/12' : 'f_2019_12', '2020/12(E)' : 'f_2020_12', 
        '2021/12(E)' : 'f_2021_12', '2022/12(E)' : 'f_2022_12'})
        df.to_csv(keyword + '_finance.csv', encoding='utf-8-sig')
        print('-----------------fin_file------------------')
        print(df)
        return df
    fina_pro(0, keyword)