import tkinter as tk  # Импортируем модуль для создания графического интерфейса
import ctypes  # Импортируем модуль для взаимодействия с системными ресурсами в Windows

# Функция для установки скорости мыши
def set_mouse_speed(speed):
    SPI_SETMOUSESPEED = 113  # Константа для установки скорости мыши
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETMOUSESPEED, 0, speed, 0)  # Вызов функции Windows API для установки скорости мыши

# Функция для сохранения настроек скорости мыши
def save_settings(speed):
    with open("mouse_speed_config.txt", "w") as file:  # Открываем файл на запись
        file.write(str(speed))  # Записываем скорость в файл

# Функция для загрузки сохраненных настроек скорости мыши
def load_settings():
    try:
        with open("mouse_speed_config.txt", "r") as file:  # Открываем файл на чтение
            speed = int(file.read())  # Читаем сохраненную скорость из файла
            return speed
    except FileNotFoundError:
        return 10  # Возвращаем значение по умолчанию, если файл не найден

# Функция для обработки изменения скорости на ползунке
def on_speed_changed(value):
    set_mouse_speed(int(value))  # Устанавливаем новую скорость мыши
    save_settings(value)  # Сохраняем новую скорость в файл

# Определение функций как чистых функций с использованием lambda
set_mouse_speed_func = lambda speed: ctypes.windll.user32.SystemParametersInfoW(113, 0, speed, 0)  # Функция установки скорости мыши
save_settings_func = lambda speed: open("mouse_speed_config.txt", "w").write(str(speed))  # Функция сохранения настроек
load_settings_func = lambda: int(open("mouse_speed_config.txt", "r").read()) if open("mouse_speed_config.txt", "r").read() else 10  # Функция загрузки сохраненных настроек
on_speed_changed_func = lambda value: (set_mouse_speed_func(int(value)), save_settings_func(value))  # Функция обработки изменения скорости

root = tk.Tk()  # Создаем главное окно приложения tkinter
root.title("Утилита для изменения скорости мыши")  # Устанавливаем заголовок окна

speed_scale = tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, label="Скорость мыши", command=on_speed_changed_func)  # Создаем шкалу для изменения скорости мыши
speed_scale.pack(pady=20)  # Размещаем шкалу на главном окне

saved_speed = load_settings_func()  # Загружаем сохраненную скорость
speed_scale.set(saved_speed)  # Устанавливаем загруженное значение на шкале

root.mainloop()  # Запускаем основной цикл обработки событий интерфейса