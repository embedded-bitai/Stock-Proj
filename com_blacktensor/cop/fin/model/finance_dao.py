# import sys
# sys.path.insert(0, '/c/Users/Admin/VscProject/BlackTensor_Test/com_blacktensor/cop/fin/model/')
import csv
import pandas as pd
from com_blacktensor.ext.db import db, openSession, engine
from sqlalchemy import func

from com_blacktensor.cop.fin.model.finance_kdd import FinanceKdd
from com_blacktensor.cop.fin.model.finance_dfo import FinanceDfo
from com_blacktensor.cop.fin.model.finance_dto import FinanceDto
from com_blacktensor.cop.emo.model.emotion_kdd import keyword
Session = openSession()
session = Session()

class FinanceDao(FinanceDto):

    @staticmethod
    def bulk():
        finance_dfo = FinanceDfo()
        dfo = finance_dfo.fina_pro(keyword)
        session.bulk_insert_mappings(FinanceDto, dfo.to_dict(orient='records'))
        session.commit()
        session.close()
    
    @classmethod
    def count(cls):
        return session.query(func.count(cls.no)).one()

    @classmethod
    def find_all(cls):

        result = session.query(FinanceDto).all()
        session.close()

        return result

