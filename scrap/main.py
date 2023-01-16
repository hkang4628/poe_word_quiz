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
    # NPC and Object 데이터 스크랩
    name = "objects"
    df = get_objects.get_data(name)
    print(df)

    # 초성 Column 추가
    df['first_letter'] = df.apply(data_control.add_first_letter, axis=1)

    # DB에 저장

    # ==================================
    # 직업 데이터 스크랩
    name = "classes"
    df = get_classes.get_data(name)
    print(df)

    # 초성 Column 추가
    df['first_letter'] = df.apply(data_control.add_first_letter, axis=1)
    print(df.head(15))
    print(df.tail(15))

    # DB에 저장
    # ==================================
    # 패시브 데이터 스크랩
    name = "passives"
    df = get_passives.get_data(name)
    print(df)

    # 초성 Column 추가
    df['first_letter'] = df.apply(data_control.add_first_letter, axis=1)
    print(df.head(15))
    print(df.tail(15))

    # DB에 저장
