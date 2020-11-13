import csv
import pandas as pd
import numpy as np
# # from sqlalchemy import create_engine
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func
from com_blacktensor.util.file_handler import FileHandler
from com_blacktensor.cop.emo.model.emotion_kdd import keyword
# from com_blacktensor.ext.routes import Resource

class StockDfo(object):
    def __init__(self):
        self.fileHandler = FileHandler()  
        # self.colums = colums

    # def get_df(self, data):
    #     return pd.DataFrame(data, columns=self.colums)


    def get_df(self, keyword):

        df = pd.read_csv('{}_data.csv'.format(keyword), index_col=[0], encoding='utf-8-sig')
        # df.drop(df.tail(5).index, inplace=True)
        # df.drop(df.head(9).index, inplace=True)
        df = df.reset_index(drop=True)

        # news_df.rename( columns={'Unnamed: 0':'name'}, inplace=True )
        df.to_csv(keyword + '_data.csv', encoding='utf-8-sig')
        print('-----------------get_df------------------')
        print(df)
        print(type(df))
        return df
        # return pd.DataFrame(data, columns=self.colums)
    get_df(0, keyword)

    def get_csv(self, keyword):
        df = pd.read_csv('./csv/{}_data.csv'.format(keyword), index_col=[0], encoding='utf-8-sig')
        # df = df.reset_index(drop=True)
        # df = df.values.tolist()
        # df = df.to_json('./csv/{}_data.csv'.format(keyword), orient='table')
        # df.drop(df.tail(6).index, inplace=True)
        # df.drop(df.head(8).index, inplace=True)
        # df = df.reset_index(drop=True)

        # news_df.rename( columns={'Unnamed: 0':'name'}, inplace=True )
        # df.to_csv('./csv/'+keyword + '_data.csv', encoding='utf-8-sig')
        # df.to_csv('./csv/{}_data.csv', encoding='utf-8-sig')
        print('-----------------get_csv------------------')
        print(df)
        print(type(df))
        return df
