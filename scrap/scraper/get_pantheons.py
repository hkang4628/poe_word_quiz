import data_control
import os
import time

from selenium import webdriver  # 웹 브라우저 컨트롤을 위한 프레임 워크
from selenium.webdriver.common.by import By  # selenium 4.0 이상에서 사용


def get_data(name: str) -> list:
    pantheon = []

    if os.path.isfile(f'scrap/scraped_list/{name}.p'):
        # {name} pickle 파일이 있을 시 pickle load
        pantheon = data_control.load_list(name)
        
    else:
        # {name} pickle 파일이 없으면 크롤링

        # url 가져오기
        url = data_control.get_url(name)

        # 크롤링
        # Chrome Driver 위치
        cd = 'C:/Users/Administrator/AppData/Local/Google/Chrome/chromedriver.exe'

        # web 페이지 로딩을 기다리는 시간
        wait_loading = 3

        # 웹 드라이버 생성
        with webdriver.Chrome(cd) as driver:
            driver.get(url)
            time.sleep(wait_loading)

            # 판테온 NAME 테이블 선택
            tr_list = driver.find_elements(
                By.XPATH, '//*[@id="Pantheonlists"]/div/table/tbody/tr')
            for tr in tr_list:
                td_list = tr.find_elements(By.TAG_NAME, 'td')
                pantheon.append(td_list[1].text)
            
    return pantheon



    