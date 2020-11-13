import logging

from com_blacktensor.cop.cov.board.model.board_kdd import CovidBoardKdd

from flask_restful import Resource
from flask import jsonify

class CovidBoard(Resource):

    def get(self):
        result = CovidBoardKdd().get_covid_board_datas()      
        # print(pd.DataFrame(result, columns=list(result.keys()) ,index=[0]))
        return jsonify(result)