# Создание собственной ошибки
class NoMoneyError(Exception):
    pass


# Блок ввода данных
user_name = input("Введите свой ник: ")
age = input("Введите свой возраст")
count_ticket = input("Введите кол-во билетов")
user_money = input("Введите сумму пополнения аккаунта")

# Функции для вызовов ошибок
def validate_name(user_name):
    if len(user_name) == 0:
        raise ValueError("Имя не может быть пустым")
    elif any([x in user_name for x in '0123456789']):
        raise ValueError("Цифры не могут быть в имени")

def validate_age(age):
    if not age.isdigit():
        raise ValueError("Возраст должен быть числом")
    elif int(age) < 12:
        raise ValueError("Слишком маленький возраст")

def validate_tickets(count):
    if not count.isdigit():
        raise ValueError("Количество должно быть цифрой")
    elif int(count) < 0:
        raise ValueError("Невозможное кол-во билетов")
    elif int(count) > 5:
        raise ValueError("Слишком большое кол-во билетов")

def validate_budget(budget):
    if not budget.isdigit():
        raise ValueError("Количество должно быть числом")
    elif int(budget) < 0:
        raise ValueError("Невозможное пополнить на отрицательное количество")
# функция подсчёта у билетов
def calculate_total(budget, price):
    if budget < price:
        raise NoMoneyError("Не хватает денег на балансе")
    elif budget >= price:
        return budget - price


def main(user_name, age, count, budget):
    try:
        validate_name(user_name)
        validate_age(age)
        validate_tickets(count)
        validate_budget(budget)
        total_prise = 500 * int(count)
        print(f"было куплено {count} шт., осталось на балансе: {calculate_total(int(budget), total_prise)}")
        print(f"Спасибо за покупку, {user_name}, Ждём вас в следующий раз!")

    except (ValueError, NoMoneyError) as e:
        print(e)


main(user_name, age, count_ticket, user_money)
