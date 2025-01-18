# Обновление статуса заметки
current_status = "В процессе" #Текущий статус заметки

print(f"Текущий статус заметки: {current_status}") #Вывод на экран текущего статуса

new_status = input("""Выберите новый статус заметки:
1. Выполнено 
2. В процессе
3. Отложено
""") #Запрашиваем новый статуса заметки

while new_status not in ["1", "2", "3"]: # запускаю цикл ввода от 1 - 3 ответа, иначе возврат
    print("Неправильный ввод! Пожалуйста выберите число от 1 до 3!")
    new_status = input("""Выберите новый статус заметки: 
    1. Выполнено 
    2. В процессе
    3. Отложено 
    """)
# даю пользователю после ввода 1-3 увидеть статус
if new_status == "1":
    print("Статус заметки обновлён: Выполнено")
elif new_status == "2":
    print("Статус заметки обновлён: В процессе")
elif new_status == "3":
    print("Статус заметки обновлён: Отложено")



