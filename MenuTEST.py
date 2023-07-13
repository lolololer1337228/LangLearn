import card
import Kit
import User

menu_items = {
    '1': {
        'name': 'Пункт 1',
        'command': 'command_1',
    },
    '2': {
        'name': 'Пункт 2',
        'command': 'command_2',
    },
    '3': {
        'name': 'Пункт 3',
        'command': 'command_3',
    },
    '4': {
        'name': 'Пункт 4',
        'command': 'command_4',
    },
}

def display_menu():
    print("Меню:")
    for key, item in menu_items.items():
        print(f"{key}. {item['name']}")
    print("Выберите пункт меню по номеру или введите 'q' для выхода")

def handle_input():
    while True:
        user_input = input("Введите номер пункта меню: ")
        if user_input == 'q':
            break  # Выход из программы
        elif user_input in menu_items.keys():
            selected_item = menu_items[user_input]
            print(f"Выбран пункт меню: {selected_item['name']}")
            command = selected_item['command']
            execute_command(command)
        else:
            print("Некорректный ввод. Попробуйте снова.")

def execute_command(command):
    if command == 'command_1':
        print("Введите Юзернейм")
        u = User.User(input())
        print(u.get_username())
    elif command == 'command_2':
        print("Выполняется команда 2")
    elif command == 'command_3':
        print("Выполняется команда 3")
    elif command == 'command_4':
        print("Выполняется команда 4")

while True:
    display_menu()
    handle_input()
