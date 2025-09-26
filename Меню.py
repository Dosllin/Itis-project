from functools import reduce

menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100
}

def sort_alphavit():
    print(sorted(menu.items()))
    input('Введите что-нибудь, чтобы вернуться в меню: ')
def sort_price():
    print(sorted(menu.items(), key=lambda x: x[1]))
    input('Введите что-нибудь, чтобы вернуться в меню: ')
def average_price_menu():
    average_price = sum(list(map(int, [x[1] for x in list(menu.items())]))) / len([x[1] for x in list(menu.items())]) # не придумал как здесь использовать lambda
    print(f'Средняя цена вашего меню составляет: {average_price}')
    input('Введите что-нибудь, чтобы вернуться в меню: ')
def add_dish():
    name_dish = input("Введите название блюда: ").lower()
    flag = 1
    while flag == 1:
        try:
            price_dish = int(input('Укажите стоймость блюда: '))
            flag = 1000
        except ValueError:
            print('Введите число!')

    if name_dish not in menu:
        menu.update({name_dish: price_dish})  # Я не понимаю зачем тут лямда
        print('Блюдо успешно добавлено!')
    else:
        menu[name_dish] = price_dish
        print('Стоймость блюда успешно изменено!')
    input('Введите что-нибудь, чтобы вернуться в меню: ')

def del_dish():
    user_dish = input('Введите название блюда: ').lower()
    menu.pop(user_dish) if user_dish in menu else print('Такого блюда в меню нет!')
    input('Введите что-нибудь, чтобы вернуться в меню: ')
def all_cheaper_dish():
    flag = 1
    while flag == 1:
        try:
            user_price = int(input('Укажите стоймость для поиска: '))
            flag = 1000
        except ValueError:
            print('Введите число!')
    print(list(filter(lambda x: x[1] < user_price, [x for x in list(menu.items())])))
    input('Введите что-нибудь, чтобы вернуться в меню: ')
def cheap_expencive_dish():
    print('Самое дешёвое блюдо: ', min([x for x in list(menu.items())], key=lambda x: x[1]))
    print('Самое дорогое блюдо: ', max([x for x in list(menu.items())], key=lambda x: x[1]))
    input('Введите что-нибудь, чтобы вернуться в меню: ')

def only_drinks():
    print(list(filter(
        lambda x: x[0] in ['coffee', 'tea', 'water', 'juice', 'soda', 'smoothie', 'milkshake', 'hot chocolate',
                           'lemonade', 'beer', 'wine', 'cocktail', 'iced tea', 'kombucha', 'cider', 'sparkling water',
                           'energy drink'], [x for x in list(sorted(menu.items(), key=lambda x: x[1]))]))) #Хз как вы хотели, чтобы мы реализовали проверку на напитки, можно было бы конечно добавить значения в словариках, но вы сами указали как должен обязательно выглядить словарик

def form_order():
    try:
        order = {

        }
        user_dishes = input('Введите названия блюд через запятую: ').lower()
        user_dishes = user_dishes.replace(' ', '')
        user_dishes = user_dishes.split(',')
        not_found_dishes = []
        order.update({str(dish[0]).upper() + str(dish[1:]): menu[dish] for dish in
                      list(filter(lambda x: x in menu, user_dishes))})  # опять хз где тут нужен map
        sum_order = reduce(lambda a, b: a + b, [x[1] for x in list(order.items())])
        print('=' * 40)
        print('Ваш заказ:')
        for i, value in enumerate([x[0] for x in list(order.items())], start=1):
            print(f'{i}. {value} - {order[value]} руб.')
        if sum_order > 500:
            print('Поздравляем, у вас скидка 10%!')
            print(f'Итого: {sum_order * 0.9} руб.')
        print('=' * 40)
        input('Введите что-нибудь, чтобы вернуться в меню: ')
    except TypeError:
        print('Вы ничего не выбрали')
        input('Введите что-нибудь, чтобы вернуться в меню: ')
def exit(f):
    return 0



while 1:
    print('='*60)
    print('1. Вывести меню отсортированное по названию',
          '2. Вывести меню отсортированное по цене',
          '3. Посчитать среднюю цену блюда в меню',
          '4. Добавить новые блюда в меню',
          '5. Удалить блюдо из меню',
          '6. Показать все блюда дешевле определённой цены',
          '7. Найти самое дешёвое и самое дорогое блюдо',
          '8. Сделать список только напитков',
          '9. Сформировать заказ',
          '10. Выйти',sep='\n')
    print('=' * 60)
    comand = {
        '1': sort_alphavit,
        '2': sort_price,
        '3': average_price_menu,
        '4': add_dish,
        '5': del_dish,
        '6': all_cheaper_dish,
        '7': cheap_expencive_dish,
        '8': only_drinks,
        '9': form_order,
    }
    user_choice = (input('Введите команду: '))
    if user_choice == '10':
        break
    try:
        comand.get(user_choice)()
    except TypeError:
        print('Такой команды нет, попробуйте снова')
        input('Введите что-нибудь, чтобы вернуться в меню: ')
