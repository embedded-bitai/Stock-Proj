from com_blacktensor.cop.cov.status.model.status_dto import CovidStatusDto
from com_blacktensor.ext.db import db, openSession

from sqlalchemy import func
# ============================================================
# ==================                     =====================
# ==================       Modeling      =====================
# ==================                     =====================
# ============================================================


# JPA Repository
class CovidStatusDao(CovidStatusDto):
    @staticmethod
    def save_data_bulk(datas):
        Session = openSession()
        session = Session()

        session.bulk_insert_mappings(CovidStatusDto, datas.to_dict(orient='records'))

        session.commit()
        session.close()
    
    @staticmethod
    def count():
        Session = openSession()
        session = Session()
        
        result = session.query(func.count(CovidStatusDto.no)).one()[0]
        session.close()
        return result
    
    @classmethod
    def find_all(self):
        
        Session = openSession()
        session = Session()

        result = session.query(CovidStatusDto).all()
        session.close()

        return result
