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
class CovidStatus(Resource):
     
     def __init__(self):
        self.dao = CovidStatusDao()
        
     def get(self):        
        result = self.dao.find_all()
        return jsonify([item.json for item in result])