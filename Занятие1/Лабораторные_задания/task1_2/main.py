def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return max(map(len, list_words))
    #return max(list_words, key=len)

if __name__ == "__main__":
    print(task())
