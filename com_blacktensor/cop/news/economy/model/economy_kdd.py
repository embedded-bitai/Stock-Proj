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
class EconomyNewsKdd(object):

    def __init__(self):
        self.lock = threading.Lock()

    def get_economy_news_urls(self):

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--log-level=3")

        driver = webdriver.Chrome('./com_blackTensor/resources/driver/chromedriver.exe', options=options)

        total_news_count = 0
        end_news_count = 240
        start_page = 1
        end_page = -1

        if end_news_count % 24 == 0:
            end_page = int(end_news_count / 24)
        else:
            end_page = int((end_news_count / 24) + 1)

        crawNewsList = []

        driver.get(f'https://www.mk.co.kr/news/economy/economic-policy/?page={start_page}')
        driver.implicitly_wait(2)
        
        for _ in range(0, end_page + 1):

            news_list = driver.find_elements_by_css_selector("div.list_area>dl")

            for news in news_list:
                a = news.find_element_by_css_selector('dt.tit>a')
                href = a.get_attribute('href')
                crawNewsList.append(href)
                total_news_count += 1
            
                if total_news_count == end_news_count:
                    break

            if total_news_count == end_news_count:
                    break
            else:
                start_page += 1
                driver.get(f'https://www.mk.co.kr/news/economy/economic-policy/?page={start_page}')
                driver.implicitly_wait(2)

        return crawNewsList

    def get_contents_from_economy_urls(self, urls, result_list):
        
        # print(f'thread Name : {threading.currentThread().getName()}, urls len : {len(urls)}')

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--log-level=3")

        driver = webdriver.Chrome('./com_blackTensor/resources/driver/chromedriver.exe', options=options)
           
        for url in urls:
            driver.get(url)
            body = driver.find_element_by_css_selector("div.art_txt")

            total_text = body.text
            remove_idx = total_text.rfind('기자')
            total_text = total_text[:remove_idx]

            remove_idx = total_text.rfind('.')
            total_text = total_text[:remove_idx]

            create_time_text = driver.find_elements_by_css_selector("div.news_title_author>ul>li")[-2].text
            create_time_text = create_time_text.replace('입력 : ', '')
            create_time_text = create_time_text[:create_time_text.find(' ')]

            with self.lock:
                result_list.append({"time":create_time_text, "contents": summary.Summry_News(total_text.replace('\n', ''))})

        driver.quit()