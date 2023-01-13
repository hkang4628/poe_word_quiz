from scraper import get_items
from scraper import get_classes
from scraper import get_objects
from scraper import get_pantheons
from scraper import get_passives
import word_to_first_consonant_letter
import data_control
import os

if __name__ == '__main__':

    # 판테온 데이터 스크랩
    name = "pantheons"
    pantheons = get_pantheons.get_data(name)
    print(pantheons)
