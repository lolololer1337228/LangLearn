import keyboard

class ArrowKeyListener:
    def __init__(self):
        self.left_arrow_pressed = False
        self.right_arrow_pressed = False

    def on_key_release(self, event):
        if event.name == "left":
            self.left_arrow_pressed = True
        elif event.name == "right":
            self.right_arrow_pressed = True

    def start_listening(self):
        keyboard.on_release(self.on_key_release)

    def stop_listening(self):
        keyboard.unhook_all()

    def is_left_arrow_pressed(self):
        return self.left_arrow_pressed

    def is_right_arrow_pressed(self):
        return self.right_arrow_pressed

    def reset(self):
        self.left_arrow_pressed = False
        self.right_arrow_pressed = False


arrow_key_listener = ArrowKeyListener()
arrow_key_listener.start_listening()

while True:
    if arrow_key_listener.is_left_arrow_pressed():
        print("Стрелка влево нажата")
    elif arrow_key_listener.is_right_arrow_pressed():
        print("Стрелка вправо нажата")

    arrow_key_listener.reset()
