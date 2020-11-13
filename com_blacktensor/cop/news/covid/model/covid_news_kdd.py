from selenium import webdriver

import threading
import requests
import datetime

from bs4 import BeautifulSoup as bs

from com_blacktensor.util.summary_news import SummaryUtil as summary

# ============================================================
# ==================                     =====================
# ==================         KDD         =====================
# ==================                     =====================
# ============================================================
class CovidNewsKDD(object):

    def __init__(self):
        self.lock = threading.Lock()

    def get_naver_news_urls(self, keyword):

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--log-level=3")

        driver = webdriver.Chrome('./com_blackTensor/resources/driver/chromedriver.exe', options=options)

        endDate = datetime.date.today().strftime('%Y.%m.%d')
        totalNewsCount = 0
        endNewsCount = 3000
        startNum = 1

        crawNewsList = []

        driver.get(f'https://search.naver.com/search.naver?&where=news&query={keyword}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2020.01.01&de={endDate}&cluster_rank=49&start={startNum}&refresh_start=1')
        driver.implicitly_wait(2)
        
        midiaBtn = driver.find_elements_by_css_selector('ul.option_menu>li')[4]
        midiaBtn = midiaBtn.find_element_by_css_selector('a')
        driver.execute_script("arguments[0].setAttribute('aria-selected','true')", midiaBtn)
        driver.implicitly_wait(2)

        selectDiv = driver.find_elements_by_css_selector('div.select_item>div')[3]
        checkBox1 = selectDiv.find_element_by_css_selector('div.rule_check>input')
        driver.execute_script("arguments[0].click();", checkBox1)
        # checkBox1.click()
        driver.implicitly_wait(2)
            
        selectDiv = driver.find_elements_by_css_selector('div.select_item>div')[9]
        checkBox2 = selectDiv.find_element_by_css_selector('div.rule_check>input')
        driver.execute_script("arguments[0].click();", checkBox2)
        # checkBox2.click()
        driver.implicitly_wait(2)
        
        selectDiv = driver.find_elements_by_css_selector('div.select_item>div')[10]
        checkBox3 = selectDiv.find_element_by_css_selector('div.rule_check>input')
        driver.execute_script("arguments[0].click();", checkBox3)
        # checkBox3.click()
        driver.implicitly_wait(2)

        okBtn = driver.find_element_by_css_selector('span.btn_inp>span.btn_inp_inner>button')
        okBtn.click()
        driver.implicitly_wait(2)

        baseurl = driver.current_url

        for _ in range(0, int((endNewsCount / 10) + 1)):
                                
            newslist = driver.find_elements_by_css_selector('div.group_news>ul.list_news>li.bx')

            for news in newslist:
                tag = news.find_element_by_css_selector('div.api_ani_send>div.news_area>a')
                href = tag.get_attribute('href')

                if len(crawNewsList) < endNewsCount:        
                    crawNewsList.append(href)
                else:
                    break

            if totalNewsCount < endNewsCount:
                startNum += 10
                # print(f'startNum : {startNum}')
                # print(f'len(crawNewsList) : {len(crawNewsList)}')
                
                driver.get(f'{baseurl}&start={startNum}')
                driver.implicitly_wait(4)
            else:
                break

        return crawNewsList

    def get_contents_from_naver_urls(self, urls, result_list):
        
        # print(f'thread Name : {threading.currentThread().getName()}, urls len : {len(urls)}')

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--log-level=3")

        driver = webdriver.Chrome('./com_blackTensor/resources/driver/chromedriver.exe', options=options)
           
        for url in urls:
            
            response = requests.get(url)

            if response.status_code == 200:
                if "donga.com" in url:
                    
                    # response = requests.get(url)
                    html = response.text
                    soup = bs(html, 'html.parser')

                    body = soup.select_one(
                        'div.article_body'
                    )

                    create_time = soup.select_one(
                        'div.title_foot > span.date01'
                    )

                    if body == None:
                        body = soup.select_one(
                            'div.article_txt'
                        )

                    if body == None:
                        body = soup.select_one(
                            'div.txt_ban'
                        )
                    
                    for br in body.select('br'):
                        br.extract()
                        
                    for div in body.select('div'):
                        div.extract()

                    for script in body.select('script'):
                        script.extract()

                    total_text = body.text
                    create_time_text = create_time.text
                    create_time_text = create_time_text.split(' ')[1]
                    
                    try:
                        
                        img_text = soup.select_one(
                            'p.caption'
                        ).text

                        total_text = total_text.replace(img_text, "")
                        
                        more_text = soup.select_one(
                            '.btn_more'
                        ).text
                        
                        total_text = total_text.replace(more_text, "")
                            
                    except Exception:
                            ...

                    remove_idx = total_text.rfind('기자')
                    total_text = total_text[:remove_idx]

                    remove_idx = total_text.rfind('.')
                    total_text = total_text[:remove_idx]

                    total_text = total_text.replace(' ', '')

                    if len(total_text) > 0:
                    
                        with self.lock:
                            result_list.append({"time":create_time_text, "contents": summary.Summry_News(total_text.replace('\n', ''))})
                    else:
                        print(f'total_text is empty. url : {url}')

                elif "joins.com" in url:
                    
                    # response = requests.get(url)
                    html = response.text
                    soup = bs(html, 'html.parser')

                    total_text = soup.select_one(
                        'div.article_body'
                    ).text

                    create_time_text = soup.select(
                        'div.byline > em'
                    )[1].text

                    create_time_text = create_time_text.split(' ')[1]
                    
                    try:
                        
                        img_text = soup.select_one(
                        'p.caption'
                        ).text

                        total_text = total_text.replace(img_text, "")
                        
                        more_text = soup.select_one(
                            '.btn_more'
                        ).text
                        
                        total_text = total_text.replace(more_text, "")
                            
                    except Exception:
                            ...

                    remove_idx = total_text.rfind('기자')
                    total_text = total_text[:remove_idx]

                    remove_idx = total_text.rfind('.')
                    total_text = total_text[:remove_idx]

                    total_text = total_text.replace(' ', '')
                                    
                    if len(total_text) > 0:
                    
                        with self.lock:
                            result_list.append({"time":create_time_text, "contents": summary.Summry_News(total_text.replace('\n', ''))})
                    else:
                        print(f'total_text is empty. url : {url}')

                else:
                    try:

                        driver.get(url)
                        driver.implicitly_wait(4)

                        data_list = driver.find_elements_by_css_selector('section.article-body>p')
                        total_text = ''
                        
                        create_time = driver.find_element_by_css_selector('div.article-dateline>span')
                        
                        create_time_text = create_time.text
                        create_time_text = create_time_text.split(' ')[1]
                        
                        for data in data_list:
                            total_text += data.text

                        if len(total_text) > 0:
                    
                            with self.lock:
                                result_list.append({"time":create_time_text, "contents": summary.Summry_News(total_text.replace('\n', ''))})
                        else:
                            print(f'total_text is empty. url : {url}')

                    except Exception:
                        print(f'Exception. thread Name : {threading.currentThread().getName()}, url : {url}')

                # with self.lock:
                #     print(f'thread Name : {threading.currentThread().getName()}, processing counter : {len(result_list)}')
            else:
                print(f'status not ok. thread Name : {threading.currentThread().getName()}, url : {url}, status_code : {response.status_code}')

        driver.quit()