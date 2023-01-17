import data_control
import os
import time
import pandas as pd

from selenium import webdriver  # 웹 브라우저 컨트롤을 위한 프레임 워크
from selenium.webdriver.common.by import By  # selenium 4.0 이상에서 사용


def get_data(name: str) -> list:
    df = pd.DataFrame(columns=['name'])

    if os.path.isfile(f'scrap/scraped_data/{name}.p'):
        # {name} pickle 파일이 있을 시 pickle load
        df = data_control.load_df(name)

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

            # Object NAME 테이블 선택
            li_list = driver.find_elements(
                By.XPATH, '/html/body/div[2]/div/ul/li')
            for li in li_list:
                a_tag_title = li.find_element(By.TAG_NAME, 'a')
                if a_tag_title.text.find("⍟") != -1:
                    a_tag_title.click()
                    time.sleep(1)
                    tr_list = driver.find_elements(
                        By.XPATH, '//*[@class="table-responsive"]/table/tbody/tr')
                    for tr in tr_list:
                        # 테이블내 tr은 다 있으나 태그에 맞춰 내용이 있다 없다 함
                        # 그래서 모든 tr을 체크함..
                        if tr.text == '':
                            continue
                        else:
                            td = tr.find_elements(By.TAG_NAME, 'td')[1]
                            a_tag = td.find_element(By.TAG_NAME, 'a')
                            print(a_tag.text)
                            df.loc[len(df)] = [a_tag.text]
        # df 저장
        data_control.save_df(name, df)

    return df
