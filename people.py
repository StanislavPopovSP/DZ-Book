from book import *

class Reader(Book):

    def show_books(self):
        books = self.all_books
        print()
        for key in books:
            print(f'{key}:')
            for value in books[key]:
                print('\t', f'{value} : {books[key][value]}шт')

    def show_genre(self):
        books = self.all_books
        print()
        for key in books:
            print(f'{key}')

    def select__book(self):
        print()
        books = self.all_books
        genre = input('Введите Жанр: ')
        book = input('Введите Книгу: ')
        if genre in books:
            if book in books[genre]:
                return f'Вы взяли данную книгу'
            else:
                return f'Данной книги нет в библиотеке'
        else:
            return f'Данного жанра нет в библиотеке'

    def append_book(self):
        print()
        books = self.all_books
        genre = input('Введите Жанр: ')
        book = input('Введите Книгу: ')
        book_amount = input('Сколько копий хотите добавить?\n -> ')
        assert book_amount.isdigit(), 'Нужно ввести число'
        book_amount = int(book_amount)
        if genre in books:
            books[genre][book] = book_amount
        else:
            return f'Данного жанра нет в библиотеке'

    def count_books(self):
        print()
        books = self.all_books
        genre = input('Введите Жанр: ')
        count = 0
        if genre in books:
            for _ in books[genre]:
                count += 1
        else:
            return f'Данного жанра нет в библиотеке'
        return f'Количество книг: {count}\nЖанр: {genre}'

    def del_book(self):
        print()
        books = self.all_books
        genre = input('Введите Жанр: ')
        if genre in books:
            del books[genre][input('Введите Книгу: ')]
        else:
            print('Данного жанра нет в библиотеке')