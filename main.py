from tkinter import Tk, filedialog
from PIL import Image

root = Tk()
root.withdraw()

# Открываем диалоговое окно для выбора файла
file_path = filedialog.askopenfilename(title="Выберите изображение", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])

# Если путь к файлу был выбран, продолжаем работу
print("stage 01")
if file_path:
    # Открываем изображение
    img = Image.open(file_path)
    
    print("stage 02")

    # Преобразуем изображение в список пикселей
    pixels = list(img.getdata())
    
    print("stage 03")

    # Ищем все чёрные пиксели
    black_pixels = [pixel for pixel in pixels if pixel == (0, 0, 0)]

    
    print("stage 04")
    
    
    # Определяем количество пикселей
    total_pixels = len(pixels)
    
    print("stage 05")

    print(f"Число чёрных пикселей: {len(black_pixels)}")
    print(f"Общее число пикселей: {total_pixels}")
    print(f"Perforation ration is: {len(black_pixels)/total_pixels}")

else:
    print("Файл не был выбран.")
