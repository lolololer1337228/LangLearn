import Card
import Kit
import User
import subprocess

menu_items = {
    '1': {
        'name': 'Добавить набор',
        'command': 'command_1',
    },
    '2': {
        'name': 'Изменить набор',
        'command': 'command_2',
    },
    '3': {
        'name': 'Просмотреть имеющиеся наборы',
        'command': 'command_3',
    },
    '4': {
        'name': 'Пункт 4',
        'command': 'command_4',
    },
}

kit_show_items = {
    '1': {
        'name': 'Добавить карточку',
        'command': 'command_1',
    },
    '2': {
        'name': 'Посмотреть карточки набора',
        'command': 'command_2',
    },
    '3': {
        'name': 'Посмотреть прогресс по набору',
        'command': 'command_3',
    },
    '4': {
        'name': 'Сбросить прогресс',
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
def execute_command_kit(command, kit_number_input):
    if command == 'command_1':
        cardi = Card.Card()
        cardi.edit_card(input("Введите слово и его перевод: ").split(' '))
        u.get_kit_by_ID(kit_number_input).add_card(cardi)

    elif command == 'command_2':
        u.show_element_of_kit(kit_number_input)

    elif command == 'command_3':
        print()
    elif command == 'command_4':
        print("Выполняется команда 4")


def execute_command(command):
    if command == 'command_1':
        kit = Kit.Kit(input("Введите название набора: "))
        u.add_kit(kit)
        print("Набор добавлен!")
    elif command == 'command_2':
        print("Выполняется команда 2")
    elif command == 'command_3':
        u.show_kits()
        kit_number_input = input("Введите номер желаемого набора для просмотра карточек: ")
        u.show_element_of_kit(kit_number_input)
        while True:
            user_input = input("Введите номер пункта меню: ")
            if user_input == 'q':
                break  # Выход из программы
            elif user_input in menu_items.keys():
                selected_item = menu_items[user_input]
                print(f"Выбран пункт меню: {selected_item['name']}")
                command = selected_item['command']
                execute_command_kit(command, kit_number_input)
            else:
                print("Некорректный ввод. Попробуйте снова.")
    elif command == 'command_4':
        print("Выполняется команда 4")

u = User.User(input("Добро пожаловать, введите ваш юернейм: "))

while True:
    display_menu()
    handle_input()
