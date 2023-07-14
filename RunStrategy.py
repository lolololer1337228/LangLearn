import os
import  time
import MenuTEST
import Kit
import Mode_interface

def StartModule(kit: Kit, mode):
    if mode == 1:
        Mod = Mode_interface.ModeWrite(kit, mode)
    elif mode == 2:
        Mod = Mode_interface.ModeChoice(kit, mode)

    Mod.create_sequence(kit, mode)
    i = 0
    while (i != Mod.get_len()):
        print("Введите 'q' чтобы выйти из режима", '\n')
        current_card = Mod.get_card(i)
        print("Как переводится это слово:", current_card.get_card_content()[0], '\n')
        user_input = input("Введите перевод")
        if (user_input == 'q') or ():
            break

        if mode == 1:
            answer = Mod.check(user_input, i)
        #elif mode == 2:
        #    answer =
        if answer:
            print("Правильно!")
        else:
            print("Неправильно")
        Mod.change_rate(kit, mode, i, answer)
        i += 1
        time.sleep(2)
        os.system('cls')

