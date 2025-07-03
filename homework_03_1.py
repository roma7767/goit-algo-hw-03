from datetime import datetime

def get_days_from_today(date_str):
    try:
        #поточна дата
        current_date = datetime.today().date()
        # перетворення рядка дати в об'єкт datetime
        specified_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        # обчислення різниці в днях
        delta = specified_date - current_date
        # повертаємо різницю в днях
        return delta.days
    except ValueError:
        return "Невірний формат дати. Використовуйте YYYY-MM-DD."

print(get_days_from_today("2025-06-13"))  # Виведе кількість днів до 31 жовтня 2023 року

