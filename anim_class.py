import tkinter as tk
from PIL import ImageTk, Image


class SpriteAnimationApp:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title('Анимация спрайта')
        self.root.resizable(False, False)
        # Настройки нашего SpriteSheet 4x2
        self.rows = 2
        self.cols = 4
        self.frames = []  # Список кадров
        self.current_frame = 0
        self.animation_delay = 100  # Задержка между кадрами в мс
        self.load_and_slice_sprites(image_path)  # Нарезка SpriteSheet
        self.setup_ui()  # Создание интерфейса
        self.animate()  # Собственно анимация

    def load_and_slice_sprites(self, path):
        sheet = Image.open(path)  # открываем наш SpriteSheet

        sheet_width, sheet_height = sheet.size
        # Вычисляем ширину и высоту кадра
        frame_width = sheet_width // self.cols
        frame_height = sheet_height // self.rows

        for row in range(self.rows):
            for col in range(self.cols):
                # Границы кадра
                left = col * frame_width
                top = row * frame_height
                right = left + frame_width
                bottom = top + frame_height
                frame = sheet.crop((
                    left, top, right, bottom))
                photo_img = ImageTk.PhotoImage(frame)
                self.frames.append(photo_img)

    def setup_ui(self):
        # Вытащили размеры первого кадра из списка self.frames
        w = self.frames[0].width()
        h = self.frames[0].height()
        self.canvas = tk.Canvas(self.root, width=w, height=h, bg='white')
        self.canvas.pack(padx=10, pady=10)
        self.sprite_container = self.canvas.create_image(
            w // 2, h // 2, image=self.frames[0]
        )
        self.slider = tk.Scale(self.root, from_=20, to=300,
                               orient=tk.HORIZONTAL, label='Задержка кадров',
                               command=self.update_speed)
        self.slider.set(self.animation_delay)
        self.slider.pack(fill=tk.X, padx=10, pady=10)

    def update_speed(self, value):
        self.animation_delay = int(value)

    def animate(self):
        current_img = self.frames[self.current_frame]
        self.canvas.itemconfig(self.sprite_container, image=current_img)
        # Защита от Garbage Collector
        self.canvas.image = current_img
        # Переход к следующему кадру
        self.current_frame += 1
        if self.current_frame >= len(self.frames) - 1:
            self.current_frame = 0
        # Можно и так было
        # self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.root.after(self.animation_delay, self.animate)