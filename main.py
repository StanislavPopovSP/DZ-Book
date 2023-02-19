from people import *

if __name__ == '__main__':
    reader = Reader()
    while True:
        command = input("\nБиблиотека>: \n"
                        "1 - Доступные жанры: \n"
                        "2 - Жанры и ее книги: \n"
                        "3 - Выбрать книгу из жанра: \n"
                        "4 - Добавить книгу в интересующий жанр: \n"
                        "5 - Количество книг в интересующем жанре: \n"
                        "6 - Удалить книгу из выбранного жанра: \n"
                        "7 - exit\n -> ")

        if command != '7':
            if command == '1':
                reader.show_genre()
            elif command == '2':
                reader.show_books()
            elif command == '3':
                print(reader.select__book())
            elif command == '4':
                reader.append_book()
            elif command == '5':
                print(reader.count_books())
            elif command == '6':
                reader.del_book()
        else:
            break