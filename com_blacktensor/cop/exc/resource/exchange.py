# from flask import request
# from flask_restful import Resource, reqparse
# from flask import jsonify

# from com_blacktensor.cop.exc.model.exchange_kdd import ExchangeKdd
# from com_blacktensor.cop.exc.model.exchange_kdd import ExchangeDao

# # ============================================================
# # ==================                     =====================
# # ==================      Resourcing     =====================
# # ==================                     =====================
# # ============================================================
# class Exchange(Resource):
#     def __init__(self):
#         self.dao = FinanceDao()

#     def get(self):
#         result = self.dao.find_all()
#         return jsonify([item.json for item in result])
#         # return jsonify(str(result))