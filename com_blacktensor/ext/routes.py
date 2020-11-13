import logging
from flask import Blueprint
from flask_restful import Api

from com_blacktensor.cop.emo.resource.emotion import Emotion, StockNews
from com_blacktensor.cop.fin.resource.finance import Finance
from com_blacktensor.cop.sto.resource.stock import Stock

# =============================================================================================
# ===================================== kain code =============================================
# =============================================================================================
from com_blacktensor.cop.cov.status.resources.status import CovidStatus
from com_blacktensor.cop.cov.board.resources.covid_board import CovidBoard
from com_blacktensor.cop.cov.board.resources.covid_board import CovidBoard
from com_blacktensor.cop.news.covid.resources.covid_news import CovideNews
from com_blacktensor.cop.news.economy.resources.economy_news import EconomyNews
from com_blacktensor.cop.cov.status.resources.status_arr import CovidStatusToArray

covid = Blueprint('covidStatus', __name__, url_prefix='/api/status/covid')
board = Blueprint('covidBoard', __name__, url_prefix='/api/board/covid')
covid_arr = Blueprint('CovidStatusToArray', __name__, url_prefix='/api/status/arr/covid')
covid_news = Blueprint('FrequencyNaverNews', __name__, url_prefix='/api/news/covid')
economy_news = Blueprint('FrequencyNaverNews', __name__, url_prefix='/api/news/economy')
# =============================================================================================
# =============================================================================================
# =============================================================================================

stock = Blueprint('stock', __name__, url_prefix='/api/stock')
finance = Blueprint('finance', __name__, url_prefix='/api/finance')
emotion = Blueprint('emotion', __name__, url_prefix='/api/emotion')
stock_news = Blueprint('stock_news', __name__, url_prefix='/api/stock_news')

# =============================================================================================
# ===================================== kain code =============================================
# =============================================================================================
api = Api(covid)
api = Api(covid_news)
api = Api(board)
api = Api(economy_news)
api = Api(covid_arr)
# =============================================================================================
# =============================================================================================
# =============================================================================================
api = Api(stock)
api = Api(finance)
api = Api(emotion)
api = Api(stock_news)

def initialize_routes(api):
    api.add_resource(Stock, '/api/stock')
    api.add_resource(Finance, '/api/finance')
    api.add_resource(Emotion, '/api/emotion')
    api.add_resource(StockNews, '/api/stock_news')

# =============================================================================================
# ===================================== kain code =============================================
# =============================================================================================
    api.add_resource(CovidStatus, '/api/status/covid')
    api.add_resource(CovideNews, '/api/news/covid')
    api.add_resource(CovidBoard, '/api/board/covid')
    api.add_resource(EconomyNews, '/api/news/economy')
    api.add_resource(CovidStatusToArray, '/api/status/arr/covid')
# =============================================================================================
# =============================================================================================
# =============================================================================================

@stock.errorhandler(500)
def stock_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@finance.errorhandler(500)
def finance_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@emotion.errorhandler(500)
def emotion_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

@stock_news.errorhandler(500)
def stock_news_api_error(e):
    logging.exception('An error occurred during emotion request. %s' % str(e))
    return 'An internal error occurred.', 500

# =============================================================================================
# ===================================== kain code =============================================
# =============================================================================================
@covid.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during covid request. %s' % str(e))
    return 'An internal error occurred.', 500

@covid_news.errorhandler(500)
def frequency_api_error(e):
    logging.exception('An error occurred during frequency request. %s' % str(e))
    return 'An internal error occurred.', 500

@board.errorhandler(500)
def board_api_error(e):
    logging.exception('An error occurred during board request. %s' % str(e))
    return 'An internal error occurred.', 500

@economy_news.errorhandler(500)
def economy_news_api_error(e):
    logging.exception('An error occurred during board request. %s' % str(e))
    return 'An internal error occurred.', 500

@covid_arr.errorhandler(500)
def covid_arr_api_error(e):
    logging.exception('An error occurred during board request. %s' % str(e))
    return 'An internal error occurred.', 500
# =============================================================================================
# =============================================================================================
# =============================================================================================