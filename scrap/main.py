from scraper import get_items
from scraper import get_classes
from scraper import get_objects
from scraper import get_pantheons
from scraper import get_passives

import data_control


if __name__ == '__main__':

    # 판테온 데이터 스크랩
    name = "pantheons"
    df = get_pantheons.get_data(name)
    print(df)

    # 초성 Column 추가
    df['first_letter'] = df.apply(data_control.add_first_letter, axis=1)
    print(df)

    # DB에 저장
    # ==================================
    # 판테온 데이터 스크랩
    name = "objects"
    df = get_objects.get_data(name)
    print(df)

    # 초성 Column 추가
    df['first_letter'] = df.apply(data_control.add_first_letter, axis=1)
    print(df.tail(15))

    # DB에 저장
