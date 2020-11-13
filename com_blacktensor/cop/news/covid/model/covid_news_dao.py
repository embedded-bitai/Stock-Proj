from com_blacktensor.ext.db import db, openSession

from com_blacktensor.cop.news.covid.model.covid_news_dto import CovidExtractionWordDto, CovidNewsDto
from sqlalchemy import func

class CovidExtractionWordDao(CovidExtractionWordDto):
    
    @staticmethod
    def save_data_bulk(datas):
        Session = openSession()
        session = Session()

        session.bulk_insert_mappings(CovidExtractionWordDto, datas.to_dict(orient='records'))

        session.commit()
        session.close()
    
    @staticmethod
    def count():
        Session = openSession()
        session = Session()
        
        result = session.query(func.count(CovidExtractionWordDto.no)).one()[0]
        session.close()
        return result
    
    @classmethod
    def find_all(self):
        
        Session = openSession()
        session = Session()

        result = session.query(CovidExtractionWordDto).all()
        session.close()

        return result

class CovidNewsDao(CovidNewsDto):
    
    @staticmethod
    def save_data_bulk(datas):
        Session = openSession()
        session = Session()

        session.bulk_insert_mappings(CovidNewsDto, datas.to_dict(orient='records'))

        session.commit()
        session.close()
    
    @staticmethod
    def count():
        Session = openSession()
        session = Session()
        
        result = session.query(func.count(CovidNewsDto.no)).one()[0]
        session.close()
        return result
    
    @classmethod
    def find_all(self):
        
        Session = openSession()
        session = Session()

        result = session.query(CovidNewsDto).all()
        session.close()

        return result
