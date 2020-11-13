from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import time

# ============================================================
# ==================                     =====================
# ==================         KDD         =====================
# ==================                     =====================
# ============================================================
class CovidBoardKdd(object):   

    def get_covid_board_datas(self):

        options = webdriver.ChromeOptions()

        options.add_argument("headless")
        options.add_argument("--log-level=3")

        driver = webdriver.Chrome('./com_blackTensor/resources/driver/chromedriver.exe', options=options)
        driver.get('https://coronaboard.kr/')
        driver.implicitly_wait(2)

        result = {}        
        time.sleep(1)
        datas = driver.find_elements_by_css_selector('div.domestic>div')      
        
        for data in datas:
            
            ps = data.find_elements_by_css_selector('p')

            key = ps[-1].text
                        
            if key == '확진자':

                result['DECIDE_CNT'] = ps[0].text

                diff = ps[1].text
                result['DECIDE_DIFF'] = self.replace_diff(diff)

            elif key == '사망자':

                result['DEATH_CNT'] = ps[0].text

                diff = ps[1].text
                result['DEATH_DIFF'] = self.replace_diff(diff)

            elif key == '격리해제':

                result['CLEAR_CNT'] = ps[0].text

                diff = ps[1].text
                result['CLEAR_DIFF'] = self.replace_diff(diff)

            elif key == '치명률':

                result['CRITICAL_CNT'] = ps[0].text

            elif key == '총검사자':

                result['ACC_EXAM_CNT'] = ps[0].text
                
                diff = ps[1].text
                result['ACC_EXAM_DIFF'] = self.replace_diff(diff)

            elif key == '검사중':

                result['EXAM_CNT'] = ps[0].text

                diff = ps[1].text
                result['EXAM_DIFF'] = self.replace_diff(diff)

            elif key == '결과음성':

                result['RESUTL_NEG_CNT'] = ps[0].text

                diff = ps[1].text
                result['RESUTL_NEG_DIFF'] = self.replace_diff(diff)

        driver.quit()
        return result

    def replace_diff(self, data):
        data = data.replace('(', '')
        data = data.replace(')', '')
        data = data.replace('+', '')
        data = data.replace('-', '')

        return data

    def check_text_value(self, element):
        return element.find_elements_by_css_selector('p')[0].text == None