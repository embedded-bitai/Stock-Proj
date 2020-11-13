from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify

from com_blacktensor.cop.fin.model.finance_dao import FinanceDao
from com_blacktensor.cop.fin.model.finance_dfo import FinanceDfo
from com_blacktensor.cop.fin.model.finance_kdd import FinanceKdd
from com_blacktensor.cop.fin.model.finance_dto import FinanceVo

# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
class Finance(Resource):
    def __init__(self):
        self.dao = FinanceDao()

    def get(self):
        result = self.dao.find_all()
        return jsonify([item.json for item in result])
        # return jsonify(str(result))
