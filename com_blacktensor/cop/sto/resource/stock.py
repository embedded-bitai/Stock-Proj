from flask import request, make_response
from flask_restful import Resource, reqparse
from flask import jsonify
import json

from com_blacktensor.cop.sto.model.stock_dao import StockDao
from com_blacktensor.cop.sto.model.stock_dfo import StockDfo
from com_blacktensor.cop.sto.model.stock_kdd import StockKdd
from com_blacktensor.cop.sto.model.stock_dto import StockVo
from com_blacktensor.cop.sto.model.stock_dto import StockDto

from com_blacktensor.cop.emo.model.emotion_kdd import keyword

# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================

class Stock(Resource):
    def __init__(self):
        self.dao = StockDao()
        self.df = StockDfo()

    def get(self):
        result = self.dao.find_all()
        print(result)
        print(type(result))
        return jsonify([item.json for item in result])
    # def get(self):
    #     result = self.df.get_csv(keyword)
    #     # print(result)
    #     # print(type(result))
    #     json_data = json.dumps(result)
    #     # print('=================json_data========================')
    #     # print(json_data)
    #     # print(type(json_data))
    #     # json = json.loads(json_data)
    #     # return jsonify([item.json for item in result])
    #     return jsonify(item.json for item in json_data)