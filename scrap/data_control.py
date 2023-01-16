import pickle
import pandas as pd
from jamo import h2j, j2hcj

# csv 파일의 내용 읽어오기


def get_url(name: str) -> str:
    csv = 'scrap/url.csv'
    df = pd.read_csv(csv, encoding='UTF-8', header=0, index_col=0)
    return df.loc[name, "url"]

# 스크랩한 데이터 리스트를 pickle로 저장


def save_df(name: str, data_list: pd.DataFrame) -> None:
    try:
        with open(f'scrap/scraped_data/{name}.p', 'wb') as f:
            pickle.dump(data_list, f)
        print(f'{name} 저장 성공!')

    except Exception as e:
        print(f'{name} 저장 실패!')
        print(e)

# pcikle로 저장된 리스트를 불러옴


def load_df(name: str):
    with open(f'scrap/scraped_data/{name}.p', 'rb') as f:
        return pickle.load(f)


# 초성 Column 추가
def add_first_letter(df):
    first_letters = ""
    name = df['name'].replace(" ", "")

    for n in name:
        first_letters += j2hcj(h2j(n)[0])

    return first_letters
