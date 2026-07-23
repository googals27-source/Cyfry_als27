import tkinter as tk
from anim_class import SpriteAnimationApp

if __name__ == '__main__':
    IMAGE_FILE = 'schuler.png'
    root = tk.Tk()
    try:
        app = SpriteAnimationApp(root, IMAGE_FILE)
        root.mainloop()
    except FileNotFoundError:
        print(f'Ошибка. Файл {IMAGE_FILE} должен быть в папке со скриптом')