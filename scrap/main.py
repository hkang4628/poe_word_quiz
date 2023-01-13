from scraper import get_items
from scraper import get_classes
from scraper import get_objects
from scraper import get_pantheons
from scraper import get_passives
import word_to_first_consonant_letter

import pickle
import pandas as pd

# csv 파일의 내용 읽어오기


def read_csv(csv: str) -> pd.DataFrame:
    df = pd.read_csv(csv, encoding='UTF-8', header=0, index_col=0)
    return df

# 스크랩한 데이터 리스트를 pickle로 저장


def save_list(pickle_name: str, data_list: list) -> None:
    try:
        with open(f'scrap/scraped_list/{pickle_name}.p', 'wb') as f:
            pickle.dump(data_list, f)
        print(f'{pickle_name} 저장 성공!')

    except Exception as e:
        print(f'{pickle_name} 저장 실패!')
        print(e)


if __name__ == '__main__':
    csv = 'scrap/url.csv'
    df = read_csv(csv)

    # 판테온 데이터 스크랩
    pantheon_url = df.loc["pantheon", "url"]
    pantheons = get_pantheons.get_data(pantheon_url)
    print(pantheons)

    # 스크랩한 데이터 리스트를 pickle로 저장
    save_list("pantheons", pantheons)
