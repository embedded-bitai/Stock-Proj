import requests
import xml.etree.ElementTree as ET

# ============================================================
# ==================                     =====================
# ==================         KDD         =====================
# ==================                     =====================
# ============================================================
class CovidStatusKdd(object):

    def get_covid19_status(self, endDate):
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
                    obj = { 'time': stateDt, 'totalCnt': decideCnt }
                    resultList.append(obj)            

            else:
                obj = { 'time': stateDt, 'totalCnt': decideCnt }
                resultList.append(obj)

        resultList.reverse()
        last = 0

        for i in range(1, len(resultList)):    

            value = int(resultList[i].get('totalCnt'))

            if value > 0:

                before = int(resultList[i-1].get('totalCnt'))

                if before == 0:
                    value = int(resultList[i].get('totalCnt')) - last
                else:
                    value = int(resultList[i].get('totalCnt')) - int(resultList[i-1].get('totalCnt'))
            else:
                last = int(resultList[i-1].get('totalCnt'))
                value = 0       

            resultList[i] = { 'time': resultList[i].get('time'), 'totalCnt': resultList[i].get('totalCnt'), 'diff':value}

        resultList[0] = { 'time': resultList[0].get('time'), 'totalCnt': 0, 'diff': 0}
        
        return resultList
    