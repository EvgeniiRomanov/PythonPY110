import json
import re

BOOKS_FILE = "books.md"
POSITION = r'[#]{4}\s(?P<position>\d+)'
#BOOK = r'(?P<book>\[(\w+\s{0,}){1,}\])' #почему то не выводит 25 книгу
BOOK = r'\[(?P<book>.+?)\]'
BOOK_URL = r'\((?P<URL>.+?)\)'
AUTHOR = r'(?P<author>.+?)\s+\('
RECOMMEND = r'\((?P<recommend>\d{1,3}\.\d+%)'
COVER_URL = 
BOOK_REGEX = f"{POSITION}\.\s+{BOOK}{BOOK_URL}\s+by\s+{AUTHOR}"  # TODO записать ругулярное выражения для поиска книги


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
