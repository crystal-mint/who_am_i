from func import *
from text import *
from art import tprint

tprint("Who am I ?")
lang = input(LANG)

if lang == '1':
    data = input(RU_DATA)
    if data == '1':
        sex = input(R_SEX)
        if sex == '1':
            ru_data_male()
        elif sex == '2':
            ru_data_female()
    if data == '2':
        sex = input(R_SEX)
        if sex == '1':
            en_data_male()
        elif sex == '2':
            en_data_female()
    if data == '3':
        sex = input(R_SEX)
        if sex == '1':
            uk_data_male()
        elif sex == '2':
            uk_data_female()

elif lang == '2':
    data = input(EN_DATA)
    if data == '1':
        sex = input(E_SEX)
        if sex == '1':
            en_ru_data_male()
        elif sex == '2':
            en_ru_data_female()
    if data == '2':
        sex = input(E_SEX)
        if sex == '1':
            en_en_data_male()
        elif sex == '2':
            en_en_data_female()
    if data == '3':
        sex = input(E_SEX)
        if sex == '1':
            en_uk_data_male()
        elif sex == '2':
            en_uk_data_female()