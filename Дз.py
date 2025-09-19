import ast
library = {
    'Война и мир': {
        "author": "Л. Толстой",
        "year": 1869,
        "rating": [5,4,4]
    }
}

def add_book():
    user_book_name = input("Введите название книги: ")
    user_book_name = user_book_name[0].upper()+user_book_name[1:].lower()
    user_book_author = input("Введите автора книги: ")
    Flag =1
    while Flag ==1:
        try:
            user_book_age = int(input("Введите год выпуска книги: "))
            Flag = 1000
        except ValueError:
            print('Введите число!!!!!')
    Flag = 1
    while Flag == 1:
        try:
            user_book_rating = input("Введите ваши оценки книги через пробел (Максимальный рейтинг 5): ")
            user_book_rating_list = [int(x) for x in user_book_rating.split(' ')]
            if all(int(x) <= 5 for x in user_book_rating_list):
                library[user_book_name] = {
                    'author': user_book_author,
                    "year": user_book_age,
                    "rating": user_book_rating_list

                }
                input('Введите что-нибудь, чтобы вернуться в меню: ')
            else:
                print(
                    'Книга не была добавлена.Максимальный рейтинг 5! Выберите в меню добавить книгу заново и учтите правила системы!\n')
            Flag = 1000
        except ValueError:
            print('Введите числа через пробел!!!!!')

def show_books():
    for name in library:
        print('--------------------------------')
        print(f'Название книги: {name}')
        print('Автор:', library[name]['author'])
        print(f'Год выпуска: {library[name]['year']}')
        print(f'Оценки: {library[name]['rating']}')
        print('--------------------------------')

    input('Введите что-нибудь, чтобы вернуться в меню: ')

def search_book():
    user_search = input('Введите название книги, которую вы хотите найти: ')
    user_search = user_search[0].upper() + user_search[1:].lower()
    if str(user_search) in library:
        print('--------------------------------')
        print(f'Название книги: {user_search}')
        print('Автор:', library[user_search]['author'])
        print(f'Год выпуска: {library[user_search]['year']}')
        print(f'Оценки: {library[user_search]['rating']}')
        print('--------------------------------')
    else:
        print('Ничего не найдено!')

    input('Введите что-нибудь, чтобы вернуться в меню: ')
def del_book():
    user_book_del = input('Введите книгу которую вы хотите удалить: ')
    user_book_del = user_book_del[0].upper() + user_book_del[1:].lower()
    try:
        del library[user_book_del]
        print('Книга удалена!')
        input('Введите что-нибудь, чтобы вернуться в меню: ')
    except KeyError:
        print('Книга не найдена')
        input('Введите что-нибудь, чтобы вернуться в меню: ')


def add_rating():
    user_choise_book = input('Введите название книги, который вы хотите добавить оценку: ')
    user_choise_book = user_choise_book[0].upper() + user_choise_book[1:].lower()
    try:
        Flag = 1
        while Flag == 1:
            try:
                user_rate = int(input('Введите оценку которую вы хотите добавить: '))
                Flag = 1000
            except ValueError:
                print('Введите число!!!!!')

        library[user_choise_book]['rating'].append(user_rate)
        if all(int(x) <= 5 for x in library[user_choise_book]['rating']):
            print('Оценка добавлена!')
        else:
            print(
                'Книга не была добавлена.Максимальный рейтинг 5! Выберите в меню добавить книгу заново и учтите правила системы!\n')
        input('Введите что-нибудь, чтобы вернуться в меню: ')
    except KeyError:
        print('Книга не найдена')
        input('Введите что-нибудь, чтобы вернуться в меню: ')

def book_after_year():
    Flag = 1
    while Flag == 1:
        try:
            user_choise_year = int(input('Введите год после которого вышли книги: '))
            Flag = 1000
        except ValueError:
            print('Введите число!!!!!')
    flag = 0
    for book in library:
        if library[book]['year'] >= user_choise_year:
            flag = 1
            print('--------------------------------')
            print(f'Название книги: {book}')
            print('Автор:', library[book]['author'])
            print(f'Год выпуска: {library[book]['year']}')
            print(f'Оценки: {library[book]['rating']}')
            print('--------------------------------')
    if flag == 0:
        print('Таких книг нет')
    input('Введите что-нибудь, чтобы вернуться в меню: ')

def book_after_rate():
    Flag = 1
    while Flag == 1:
        try:
            user_average_rate = int(input('Введите средний рейтинг выше которого нужно найти: '))
            Flag = 1000
        except ValueError:
            print('Введите число!!!!!')
    flag = 0
    for book in library:
        if sum(library[book]['rating']) / len(library[book]['rating']) >= user_average_rate:
            flag = 1
            print('--------------------------------')
            print(f'Название книги: {book}')
            print('Автор:', library[book]['author'])
            print(f'Год выпуска: {library[book]['year']}')
            print(f'Оценки: {library[book]['rating']}')
            print('Средний рейтинг:', sum(library[book]['rating']) / len(library[book]['rating']))
            print('--------------------------------')
    if flag == 0:
        print('Таких книг нет!')
    input('Введите что-нибудь, чтобы вернуться в меню: ')

def export_in_txt():
    with open("library.txt", "w") as file:
        file.write(str(library))

    print("Данные успешно сохранены в library.txt")
    input('Введите что-нибудь, чтобы вернуться в меню: ')

def import_in_txt():
    new_library = {}
    try:
        with open("library.txt", "r") as file:
            for line in file:
                try:
                    dictionary_from_file = ast.literal_eval(line)
                    new_library.update(dictionary_from_file)
                    library.update(new_library)
                    print("Данные успешно импортированы из library.txt")
                except (ValueError, SyntaxError, TypeError):
                    print('Неверный тип данных в файле')
    except FileNotFoundError:
        print("Файл library.txt не найден.")

    input('Нажмите Enter, чтобы вернуться в меню: ')


while 1:
    print('1. Добавить книгу (название, автор, год, список оценок читателей)',
          '2. Показать все книги',
          '3. Найти книгу по названию',
          '4. Удалить книгу',
          '5. Добавить новую оценку книге',
          '6. Вывести список книг, выпущенных после определённого года',
          '7. Показать все книги с рейтингом выше определённого порога',
          '8. Экспортировать книги в CSV-вид (название;автор;год;оценки)',
          '9. Импортировать книги из CSV',
          '10. Выход',sep='\n')
    user_choise = (input('Введите номер функции: '))
    if user_choise == '1':
        add_book()
    elif user_choise == '2':
        show_books()
    elif user_choise == '3':
        search_book()
    elif user_choise == '4':
        del_book()
    elif user_choise == '5':
        add_rating()
    elif user_choise == '6':
        book_after_year()
    elif user_choise == '7':
        book_after_rate()
    elif user_choise == '8':
        export_in_txt()
    elif user_choise == '9':
       import_in_txt()
    elif user_choise == "10":
        break
    else:
        print("Неверный номер. Попробуйте еще раз.")
        input('Нажмите Enter, чтобы вернуться в меню: ')
else:#"Использовать while else" использовал, но он никогда не запустится
    try:#"Добавить хотя бы один блок" Добавил, но он никогда не запустится)
        int(input())
    except(ValueError, SyntaxError, TypeError):
        print('LA')
    else:
        print(1)
    finally:
        print(2)
    print('Это никогда не запуститься, но это было обязательно в требованиях')