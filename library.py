from librarian import *


class Library:
    __instance = None

    def __new__(cls, *args, **kwargs):
        # Проверяем атрибут класс __instance если есть создается 1 экземпляр, второго е будет. Если не было ни одного объекта. is None
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            raise Exception('Вы не можете создать еще один экземпляр класса')

    def __init__(self, lib_name='Библиотека им. Маяковского'):
        self.lib_name = lib_name
        self.books = 459

    def __str__(self):
        return self.lib_name


if __name__ == '__main__':
    library = Library()
    print('Библиотека:')
    print(library)
    print()
    librarian1 = Librarian('МарьИванна')
    librarian2 = Librarian('ЕвгенияБарисовна')
    librarian3 = Librarian('ЕвдакиньяГеоргевна')

    print('Сотрудники:')
    for i in(librarian1, librarian2, librarian3):
        print(i)
