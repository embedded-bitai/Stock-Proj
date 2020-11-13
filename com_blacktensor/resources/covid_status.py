import logging
import requests
import xml.etree.ElementTree as ET
import pandas as pd

from com_blackTensor.ext.db import db
from com_blackTensor.util.checker import Checker 
from com_blackTensor.util.file_hander import FileHandler as fh

from flask_restful import Resource
from flask import request


# ============================================================
# ==================                     =====================
# ==================         KDD         =====================
# ==================                     =====================
# ============================================================
class CovidStatusKdd(object):

    @staticmethod
    def get_covid19_status(endDate):
        url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=wCrhzKq2s2w58tjFGxjsD13C0W6qCFXnaQqQlkiExDGf6Xsjz8Hq4AzCOkksAHmicF7e8OW9ZcndFn64EYjRuA%3D%3D&pageNo=1&numOfRows=500&startCreateDt=20200101&endCreateDt={endDate}'

        res = requests.get(url)
        xmlStr = res.text

        xml = ET.ElementTree(ET.fromstring(xmlStr))
        root = xml.getroot()
        body = root.find('body')
        items = body.find('items')

        itemList = items.findall('item')
        resultList = []

        for item in itemList:
            decideCnt = item.find('decideCnt').text
            stateDt = item.find('stateDt').text

            if len(resultList) >= 2:

                before = resultList[-1]
                beforeTime = before.get('time')

                if beforeTime != stateDt:
                    obj = { 'time': stateDt, 'accumulate': decideCnt }
                    resultList.append(obj)            

            else:
                obj = { 'time': stateDt, 'accumulate': decideCnt }
                resultList.append(obj)

        resultList.reverse()
        last = 0

        for i in range(1, len(resultList)):    

            value = int(resultList[i].get('accumulate'))

            if value > 0:

                before = int(resultList[i-1].get('accumulate'))

                if before == 0:
                    value = int(resultList[i].get('accumulate')) - last
                else:
                    value = int(resultList[i].get('accumulate')) - int(resultList[i-1].get('accumulate'))
            else:
                last = int(resultList[i-1].get('accumulate'))
                value = 0       

            resultList[i] = { 'time': resultList[i].get('time'), 'accumulate': resultList[i].get('accumulate'), 'peopleCnt':value}

        resultList[0] = { 'time': resultList[0].get('time'), 'accumulate': 0, 'peopleCnt': 0}
        
        return resultList
    

# ============================================================
# ==================                     =====================
# ==================    Preprocessing    =====================
# ==================                     =====================
# ============================================================
class CovidStatusDf(object):
    ...
# ============================================================
# ==================                     =====================
# ==================       Modeling      =====================
# ==================                     =====================
# ============================================================
# class CovidStatusDto(db.Model):
#     ...
# class CovidStatusDao(StockDto):
#     ...
class CovidStatusVo(object):
    ...
class CovidStatusTf(object):
    ...
class CovidStatusAi(object):
    ...
# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
class CovidStatus(Resource):
     def get(self):
        params = request.json
        endDate = params['endDate']
        isSave = params['isSave']

        if endDate is not None and Checker.check_covid_date_type(endDate):

            responseList = CovidStatusKdd.get_covid19_status(endDate)

            if bool(isSave) and len(responseList) > 0:
                if not Checker.check_folder_path('./csv'):
                    fh.crete_folder('./csv')
                    
                fh.save_to_csv('./csv/result_Covid19.csv', responseList, list(responseList[0].keys()), 'utf-8-sig')

            return {'response': responseList}
        else:
            return {'response': f'This Request is BadRequest!! Request data : {endDate}'}