# PDF ↔ JPG Converter

Набор утилит для конвертации между форматами PDF и JPG.

## Описание

Проект содержит два скрипта Python для двунаправленной конвертации между PDF и JPG:

- **join-jpg-to-pdf.py** - объединяет JPG-файлы в один PDF-документ
- **pdf_to_jpg.py** - конвертирует PDF в JPG-изображения

## Зависимости

```bash
pip install pillow pdf2image
```

### Дополнительные системные зависимости для pdf2image:

**Ubuntu/Debian:**
```bash
sudo apt-get install poppler-utils
```

**macOS:**
```bash
brew install poppler
```

**Windows:**
Скачайте poppler для Windows и добавьте в PATH, или используйте conda:
```bash
conda install -c conda-forge poppler
```

## Использование

### Конвертация JPG в PDF

```bash
python3 join-jpg-to-pdf.py
```

**Особенности:**
- Обрабатывает все JPG/JPEG файлы в текущей директории
- Сортирует файлы по имени перед объединением
- Поддерживает различные регистры расширений (jpg, jpeg, JPG, JPEG)
- Создает файл `result.pdf` в той же директории
- Автоматически конвертирует изображения в RGB

### Конвертация PDF в JPG

```bash
python3 pdf_to_jpg.py input.pdf
```

**Особенности:**
- Конвертирует каждую страницу PDF в отдельный JPG-файл
- Использует разрешение 300 DPI для высокого качества
- Сохраняет файлы в той же директории, что и исходный PDF
- Автоматически генерирует имена файлов на основе имени PDF

**Примеры имен выходных файлов:**
- Для многостраничного PDF `document.pdf`: `document_page_1.jpg`, `document_page_2.jpg`, etc.
- Для одностраничного PDF `scan.pdf`: `scan.jpg`

## Примеры использования

### Сценарий 1: Создание PDF из сканов

```bash
# В папке со сканами (scan001.jpg, scan002.jpg, ...)
python3 join-jpg-to-pdf.py
# Результат: result.pdf
```

### Сценарий 2: Извлечение страниц из PDF

```bash
python3 pdf_to_jpg.py my_document.pdf
# Результат: my_document_page_1.jpg, my_document_page_2.jpg, ...
```

### Сценарий 3: Круговая конвертация

```bash
# JPG → PDF → JPG (например, для обработки или сжатия)
python3 join-jpg-to-pdf.py          # Создает result.pdf
python3 pdf_to_jpg.py result.pdf    # Создает result_page_1.jpg, result_page_2.jpg, ...
```

## Структура проекта

```
.
├── join-jpg-to-pdf.py    # JPG → PDF конвертер
├── pdf_to_jpg.py         # PDF → JPG конвертер
└── README.md             # Этот файл
```

## Обработка ошибок

Оба скрипта включают обработку ошибок:

- **join-jpg-to-pdf.py**: Выводит сообщения об ошибках при обработке поврежденных изображений
- **pdf_to_jpg.py**: Использует argparse для валидации аргументов командной строки

## Технические детали

### join-jpg-to-pdf.py
- Использует `PIL (Pillow)` для обработки изображений
- Конвертирует все изображения в RGB перед сохранением
- Сортирует файлы для предсказуемого порядка страниц
- Поддерживает glob-паттерны для поиска файлов

### pdf_to_jpg.py
- Использует `pdf2image` для рендеринга PDF
- Настроен на 300 DPI для высокого качества
- Поддерживает многостраничные PDF
- Сохраняет файлы в формате JPEG

## Совместимость

- **Python**: 3.6+
- **ОС**: Linux, macOS, Windows
- **Форматы**: JPG, JPEG, PDF

## Лицензия

Свободное использование для личных и коммерческих целей.
