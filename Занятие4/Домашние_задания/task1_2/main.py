import re


#pattern = """(.|\n)+?"""
pattern = r'^\"{3}.+?\"{3}'

def task():
    book_pattern = re.compile(pattern, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open("input.txt", 'r', encoding="utf-8") as f:
        for book in book_pattern.finditer(f.read()):
            print(book.group())

if __name__ == "__main__":
    # Write your solution here
    task()
    print("------------------")
    task()
