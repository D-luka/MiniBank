from datetime import date

from utils.helper import date_to_str, str_to_date


class Client:
    counter: int = 101

    def __init__(self: object, name: str, email: str, nif: str, birth_date: str) -> None:
        self.__code: int = Client.counter
        self.__name: str = name
        self.__email: str = email
        self.__nif: str = nif
        self.__birth_date: date = str_to_date(birth_date)
        self.__date_registration: date = date.today()
        Client.counter += 1  # get one more

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def nif(self: object) -> str:
        return self.__nif

    @property
    def birth_date(self: object) -> str:
        return date_to_str(self.__birth_date)

    @property
    def date_registration(self: object) -> str:
        return date_to_str(self.__date_registration)

    def __str__(self: object) -> str:
        return f'Code: {self.code} \nName: {self.name} \nBirth Date: {self.birth_date} \nRegistration: {self.date_registration}'
