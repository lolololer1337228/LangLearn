import Card
import Kit
import User
import subprocess
import Menues
import os
import time

def display_menu():
    print()
    print("Меню:")
    for key, item in Menues.menu_items.items():
        print(f"{key}. {item['name']}")
    print()
    print("Выберите пункт меню по номеру или введите 'q' для выхода")

def display_kits_menu():
    print()
    print("Меню:")
    for key, item in Menues.kit_show_items.items():
        print(f"{key}. {item['name']}")
    print()
    print("Выберите пункт меню по номеру или введите 'q' для выхода")

def display_cards_menu():
    print()
    print("Меню:")
    for key, item in Menues.card_show_items.items():
        print(f"{key}. {item['name']}")
    print()
    print("Выберите пункт меню по номеру или введите 'q' для выхода")

def handle_input():
    while True:
        user_input = input("Введите номер пункта меню: ")
        if user_input == 'q':
            break  # Выход из программы
        elif user_input in Menues.menu_items.keys():
            selected_item = Menues.menu_items[user_input]
            print(f"Выбран пункт меню: {selected_item['name']}")
            command = selected_item['command']
            execute_command(command)
        else:
            print("Некорректный ввод. Попробуйте снова.")


def execute_command(command):
    if command == 'main_menu_command_1':
        os.system('cls')
        kit = Kit.Kit(input("Введите название набора: "))
        if kit.get_name_kit() == 'q':
            display_menu()
            return
        u.add_kit(kit)
        print("Набор добавлен!")
        display_menu()
    elif command == 'main_menu_command_2':
        os.system('cls')
        u.show_kits()
        print()
        kit_number_input = input("Введите номер желаемого набора для взаимодействия с ним: ")
        if kit_number_input == 'q':
            display_menu()
            return
        kit_number_input = int(kit_number_input)
        u.show_element_of_kit(kit_number_input)
        print()
        display_kits_menu()

        while True:
            user_input = input("Введите номер пункта меню: ")
            if user_input == 'q':
                display_menu()
                break # Выход из программы
            elif user_input == '5':
                execute_command_kit('kit_menu_command_5', kit_number_input)
                break
            elif user_input in Menues.kit_show_items.keys():

                selected_item = Menues.kit_show_items[user_input]
                print(f"Выбран пункт меню: {selected_item['name']}")
                command = selected_item['command']
                execute_command_kit(command, kit_number_input)

            else:
                print("Некорректный ввод. Попробуйте снова.")

def execute_command_kit(command, kit_number_input):
    def kit_and_menu():
        print("Текущий набор:", end='')
        u.show_kit(kit_number_input)
        print()
        display_kits_menu()
        print()

    if command == 'kit_menu_command_1':
        os.system('cls')
        cardi = Card.Card()
        cardi_edit_input = input("Введите слово и его перевод: ").split()
        if (len(cardi_edit_input) == 1) and (cardi_edit_input[0] == 'q'):
            kit_and_menu()
            return
        elif len(cardi_edit_input) < 2:
            print("Неправильный ввод!")
            time.sleep(2)
            execute_command_kit('kit_menu_command_1', kit_number_input)
        cardi.edit_card(cardi_edit_input[0],cardi_edit_input[1])
        u.get_kit_by_ID(kit_number_input).add_card(cardi)
        os.system('cls')
        kit_and_menu()
    elif command == 'kit_menu_command_2':
        os.system('cls')
        print("Слова, содержащиеся в этом наборе:")
        u.show_element_of_kit(kit_number_input)
        print()
        card_number_input = input("Выберете карточку, с которой хотите взаимодейсвтовать:")
        if card_number_input == 'q':
            display_kits_menu()
            return
        card_number_input = int(card_number_input)
        #kit_and_menu()
        #Переход в меню карточек
        display_cards_menu()
        while True:
            user_input = input("Введите номер пункта меню: ")
            if user_input == 'q':
                display_kits_menu()
                break # Выход из программы
            elif user_input in Menues.card_show_items.keys():
                selected_item = Menues.card_show_items[user_input]
                print(f"Выбран пункт меню: {selected_item['name']}")
                command = selected_item['command']
                execute_command_card(command, kit_number_input, card_number_input)
            else:
                print("Некорректный ввод. Попробуйте снова.")

    elif command == 'kit_menu_command_3':
        os.system('cls')
        print("Ваш текущий прогресс по данному набору:", "{:.2f}%".format(u.get_kit_by_ID(kit_number_input).get_progress()*100))
        kit_and_menu()
    elif command == 'kit_menu_command_4':
        os.system('cls')
        u.get_kit_by_ID(kit_number_input).reset_counter()
        print("Ваш прогрес по данному набору сброшен!")
        display_kits_menu()
    elif command == 'kit_menu_command_5':
        u.remove_kit(kit_number_input)
        os.system('cls')
        print("Набор удален")
        display_menu()
        return
    #elif command == 'kit_menu_command_6': вызов режима ----------------------


def execute_command_card(command, kit_number_input, card_number_input):
    if command == 'card_menu_command_1':
        os.system('cls')
        edit_input = input("Введите измененное слово и его перевод: ").split()
        if edit_input == 'q':
            display_cards_menu()
            return
        u.get_kit_by_ID(kit_number_input).get_array_of_kit()[card_number_input].edit_card(edit_input[0],edit_input[1])
        print("Карточка успешно изменена!")
        display_cards_menu()
    elif command == 'card_menu_command_2':
        os.system('cls')
        u.get_kit_by_ID(kit_number_input).remove_card(card_number_input)
        print("Карточка успешно удалена!")
        display_cards_menu()

u = User.User(input("Добро пожаловать, введите ваш юернейм: "))

while True:
    display_menu()
    handle_input()
