import logging

from flask_restful import Resource
from flask import request
from flask import jsonify
from com_blacktensor.cop.cov.status.model.status_dao import CovidStatusDao

# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
class CovidStatusToArray(Resource):
     
     def __init__(self):
        self.dao = CovidStatusDao()
        
     def get(self):        
         result = self.dao.find_all()

         result_list = []
         result_list.append("확진자")

         for item in result:
            result_list.append(item.diff)

         return result_list
         
