from com_blacktensor.ext.db import db
from sqlalchemy import Column, Integer, String, Date

# ============================================================
# ==================                     =====================
# ==================       Modeling      =====================
# ==================                     =====================
# ============================================================
# JPA entity
class CovidStatusDto(db.Model):
    
    __tablename__ = 'covid_status'
    
    no = Column(Integer, primary_key=True)
    time = Column(Date)
    totalCnt = Column(Integer)
    diff = Column(Integer)

    def __repr__(self):
        timestr = self.time.strftime('%Y-%m-%d')
        return f'no : {self.no}, time : {timestr}, totalCnt : {self.totalCnt}, diff : {self.diff}'
    
    @property
    def json(self):
        return {
            'no': self.no,
            'time': self.time.strftime('%Y-%m-%d'),
            'totalCnt': self.totalCnt,
            'diff': self.diff
        }