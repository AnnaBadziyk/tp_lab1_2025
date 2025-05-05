tasks = []

print("Вітаємо у вашому ToDo List!")

while True:
    print("\nОберіть дію:")
    print("1. Додати завдання")
    print("2. Переглянути завдання")
    print("3. Позначити як виконане")
    print("4. Видалити завдання")
    print("5. Вийти")
    
    choice = input("Введіть номер дії: ")
    
    if choice == "1":
        description = input("Введіть опис завдання: ")
        tasks.append({"text": description, "done": False})
        
    elif choice == "2":
        if not tasks:
            print("Список завдань порожній.")
        else:
            print("Список завдань:")
            for idx, task in enumerate(tasks, start=1):
                status = "[x]" if task["done"] else "[ ]"
                print(f"{idx}. {status} {task['text']}")
                
    elif choice == "3":
        number = input("Введіть номер виконаного завдання: ")
        if number.isdigit():
            number = int(number)
            if 1 <= number <= len(tasks):
                tasks[number - 1]["done"] = True
                print("Завдання позначено як виконане.")
            else:
                print("Неправильний номер завдання.")
        else:
            print("Будь ласка, введіть число.")
            
    elif choice == "4":
        number = input("Введіть номер завдання для видалення: ")
        if number.isdigit():
            number = int(number)
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Завдання \"{removed['text']}\" видалено.")
            else:
                print("Неправильний номер завдання.")
        else:
            print("Будь ласка, введіть число.")
            
    elif choice == "5":
        print("Дякую за використання!")
        break
        
    else:
        print("Невідома дія. Спробуйте ще раз.")
