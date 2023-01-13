from selenium import webdriver  # 웹 브라우저 컨트롤을 위한 프레임 워크
from selenium.webdriver.common.by import By  # selenium 4.0 이상에서 사용


def start_web_browser():
    # Chrome Driver 위치
    cd = 'C:/Users/Administrator/AppData/Local/Google/Chrome/chromedriver.exe'

    # web 페이지 로딩을 기다리는 시간
    wait_loading = 3

    # 웹 드라이버 생성
