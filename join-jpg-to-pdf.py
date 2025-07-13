#!/usr/bin/env python3

from PIL import Image
import os
import glob

def convert_jpgs_to_pdf(output_filename="result.pdf"):
    # Ищем все файлы JPG и JPEG (регистр не важен)
    jpg_files = sorted(
        glob.glob("*.jpg") + 
        glob.glob("*.jpeg") + 
        glob.glob("*.JPG") + 
        glob.glob("*.JPEG")
    )
    
    if not jpg_files:
        print("Не найдено ни одного JPG-файла в текущей директории.")
        return

    images = []
    for file in jpg_files:
        try:
            img = Image.open(file).convert("RGB")
            images.append(img)
        except Exception as e:
            print(f"Ошибка при обработке файла {file}: {e}")

    if not images:
        print("Нет подходящих изображений для конвертации.")
        return

    # Сохраняем как PDF
    images[0].save(output_filename, save_all=True, append_images=images[1:])
    print(f"PDF создан: {output_filename}")

if __name__ == "__main__":
    convert_jpgs_to_pdf()
