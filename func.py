# https://habr.com/ru/articles/771950/
# https://habr.com/ru/articles/709282/
from mimesis import Person, Gender
from mimesis.locales import Locale
from mimesis.builtins import RussiaSpecProvider



def ru_data_male():
    person = Person(Locale.RU)
    ru = RussiaSpecProvider()

    person = Person(Locale.RU)
    ru = RussiaSpecProvider()

    name = (f"Имя: {person.full_name(gender=Gender.MALE)} {ru.patronymic(gender=Gender.MALE)}")
    number = (f"Номер: {person.phone_number()}")
    email = (f"Почта: {person.email()}")
    nickname = (f"Никнейм: {person.username()}")
    polit = (f"Пол. взгляды: {person.political_views()}")
    password = (f"Пароль: {person.password()}")
    study = (f"Образование: {person.university()}")
    pasport = (f"Серия\номер паспорта: {ru.series_and_number()}")
    nation = (f"Национальность: {person.nationality(gender=Gender.MALE)}")
    
    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print(pasport)
    print("\n")

def ru_data_female():
    person = Person(Locale.RU)
    ru = RussiaSpecProvider()

    name = (f"Имя: {person.full_name(gender=Gender.FEMALE)} {ru.patronymic(gender=Gender.FEMALE)}")
    number = (f"Номер: {person.phone_number()}")
    email = (f"Почта: {person.email()}")
    nickname = (f"Никнейм: {person.username()}")
    polit = (f"Пол. взгляды: {person.political_views()}")
    password = (f"Пароль: {person.password()}")
    study = (f"Образование: {person.university()}")
    pasport = (f"Серия\номер паспорта: {ru.series_and_number()}")
    nation = (f"Национальность: {person.nationality(gender=Gender.FEMALE)}")
    
    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print(pasport)
    print("\n")

def en_data_male():
    person = Person(Locale.EN)

    name = (f"Имя: {person.full_name(gender=Gender.MALE)} {person.surname(gender=Gender.MALE)}")
    number = (f"Номер: {person.phone_number()}")
    email = (f"Почта: {person.email()}")
    nickname = (f"Никнейм: {person.username()}")
    polit = (f"Пол. взгляды: {person.political_views()}")
    password = (f"Пароль: {person.password()}")
    study = (f"Образование: {person.university()}")
    nation = (f"Национальность: {person.nationality(gender=Gender.MALE)}")

    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print("\n")

def en_data_female():
    person = Person(Locale.EN)

    name = (f"Имя: {person.full_name(gender=Gender.FEMALE)} {person.surname(gender=Gender.FEMALE)}")
    number = (f"Номер: {person.phone_number()}")
    email = (f"Почта: {person.email()}")
    nickname = (f"Никнейм: {person.username()}")
    polit = (f"Пол. взгляды: {person.political_views()}")
    password = (f"Пароль: {person.password()}")
    study = (f"Образование: {person.university()}")
    nation = (f"Национальность: {person.nationality(gender=Gender.FEMALE)}")
  
    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print("\n")

def uk_data_male():
    person = Person(Locale.UK)

    name = (f"Имя: {person.full_name(gender=Gender.MALE)} {person.surname(gender=Gender.MALE)}")
    number = (f"Номер: {person.phone_number()}")
    email = (f"Почта: {person.email()}")
    nickname = (f"Никнейм: {person.username()}")
    polit = (f"Пол. взгляды: {person.political_views()}")
    password = (f"Пароль: {person.password()}")
    study = (f"Образование: {person.university()}")
    nation = (f"Национальность: {person.nationality()}")


    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print("\n")

def uk_data_female():
    person = Person(Locale.UK)

    name = (f"Имя: {person.full_name(gender=Gender.FEMALE)} {person.surname(gender=Gender.FEMALE)}")
    number = (f"Номер: {person.phone_number()}")
    email = (f"Почта: {person.email()}")
    nickname = (f"Никнейм: {person.username()}")
    polit = (f"Пол. взгляды: {person.political_views()}")
    password = (f"Пароль: {person.password()}")
    study = (f"Образование: {person.university()}")
    nation = (f"Национальность: {person.nationality()}")
  
    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print("\n")



def en_ru_data_male():
    person = Person(Locale.RU)
    ru = RussiaSpecProvider()

    person = Person(Locale.RU)
    ru = RussiaSpecProvider()

    name = (f"Name: {person.full_name(gender=Gender.MALE)} {ru.patronymic(gender=Gender.MALE)}")
    number = (f"Number: {person.phone_number()}")
    email = (f"Mail: {person.email()}")
    nickname = (f"Nickname: {person.username()}")
    polit = (f"Political Views: {person.political_views()}")
    password = (f"Password: {person.password()}")
    study = (f"Education: {person.university()}")
    pasport = (f"Series/passport number: {ru.series_and_number()}")
    nation = (f"Nationality: {person.nationality(gender=Gender.MALE)}")
    
    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print(pasport)
    print("\n")

def en_ru_data_female():
    person = Person(Locale.RU)
    ru = RussiaSpecProvider()

    name = (f"Name: {person.full_name(gender=Gender.FEMALE)} {ru.patronymic(gender=Gender.FEMALE)}")
    number = (f"Number: {person.phone_number()}")
    email = (f"Mail: {person.email()}")
    nickname = (f"Nickname: {person.username()}")
    polit = (f"Political Views: {person.political_views()}")
    password = (f"Password: {person.password()}")
    study = (f"Education: {person.university()}")
    pasport = (f"Series/passport number: {ru.series_and_number()}")
    nation = (f"Nationality: {person.nationality(gender=Gender.FEMALE)}")
    
    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print(pasport)
    print("\n")

def en_en_data_male():
    person = Person(Locale.EN)

    name = (f"Name: {person.full_name(gender=Gender.MALE)} {person.surname(gender=Gender.MALE)}")
    number = (f"Number: {person.phone_number()}")
    email = (f"Mail: {person.email()}")
    nickname = (f"Nickname: {person.username()}")
    polit = (f"Political Views: {person.political_views()}")
    password = (f"Password: {person.password()}")
    study = (f"Education: {person.university()}")
    nation = (f"Nationality: {person.nationality(gender=Gender.MALE)}")

    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print("\n")

def en_en_data_female():
    person = Person(Locale.EN)

    name = (f"Name: {person.full_name(gender=Gender.FEMALE)} {person.surname(gender=Gender.FEMALE)}")
    number = (f"Number: {person.phone_number()}")
    email = (f"Mail: {person.email()}")
    nickname = (f"Nickname: {person.username()}")
    polit = (f"Political Views: {person.political_views()}")
    password = (f"Password: {person.password()}")
    study = (f"Education: {person.university()}")
    nation = (f"Nationality: {person.nationality(gender=Gender.FEMALE)}")
  
    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print("\n")

def en_uk_data_male():
    person = Person(Locale.UK)

    name = (f"Name: {person.full_name(gender=Gender.MALE)} {person.surname(gender=Gender.MALE)}")
    number = (f"Number: {person.phone_number()}")
    email = (f"Mail: {person.email()}")
    nickname = (f"Nickname: {person.username()}")
    polit = (f"Political Views: {person.political_views()}")
    password = (f"Password: {person.password()}")
    study = (f"Education: {person.university()}")
    nation = (f"Nationality: {person.nationality(gender=Gender.MALE)}")


    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print("\n")

def en_uk_data_female():
    person = Person(Locale.UK)

    name = (f"Name: {person.full_name(gender=Gender.FEMALE)} {person.surname(gender=Gender.FEMALE)}")
    number = (f"Number: {person.phone_number()}")
    email = (f"Mail: {person.email()}")
    nickname = (f"Nickname: {person.username()}")
    polit = (f"Political Views: {person.political_views()}")
    password = (f"Password: {person.password()}")
    study = (f"Education: {person.university()}")
    nation = (f"Nationality: {person.nationality(gender=Gender.FEMALE)}")
  
    print("\n")
    print(name)
    print(number)
    print(nickname)
    print(password)
    print(email)
    print(study)
    print(polit)
    print("\n")