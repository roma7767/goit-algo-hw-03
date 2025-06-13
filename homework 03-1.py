from datetime import datetime

def get_days_from_today(date_str):
    #поточна дата
    current_date = datetime.today()
    # перетворення рядка дати в об'єкт datetime
    specified_date = datetime.strptime(date_str, "%Y-%m-%d")
    # обчислення різниці в днях
    delta = specified_date - current_date
    # повертаємо різницю в днях
    return delta.days

print(get_days_from_today("2024-06-24"))  # Виведе кількість днів до 31 жовтня 2023 року

