import re


def changeText(text: str) -> list:
    """
    Функция принимает строку с текстом.
    Убирает все знаки препинания и возвращает
    список, состоящий из слов текста.
    """
    return re.findall(r"\w+", text)


def mostCommon(words_list: list, length: int = 0) -> list:
    """
    Функция принимает список и ограничение по длине.
    Возвращает самый часто встречающийся элемент.
    Если есть несколько элементов с одинаковой самой большой частотой, то вернёт их все.
    """
    word_count: dict = {
        word: words_list.count(word) for word in list(set(words_list)) if len(word) > length
    }
    return [word for word, count in word_count.items() if count == max(word_count.values())]


def mostLength(words_list: list) -> list:
    """
    Функция принимает список.
    Возвращает самый длинный элемент.
    Если есть несколько элементов с одинаковой самой большой длиной, то вернёт их все.
    """
    unique_eng_words = [word for word in list(set(words_list)) if re.match(r"[A-Za-z]+", word)]
    return [word for word in unique_eng_words if len(word) == max(map(len, unique_eng_words))]


nameFile = input('Название файла: ')

with open(nameFile, encoding="utf8") as f:
    fileText = f.read()

fileText = changeText(fileText)
print(f"Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 3)}")
print(f"Список самых длинных английских слов: {mostLength(fileText)}")
