import re

ip4 = re.compile(r"""
    (?:(?:25[0-5]| # 250-255
          2[0-4][0-9]|  # 200-249
          [01]?[0-9]?[0-9])\.){3}
          (?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])
""", re.VERBOSE)

def task():
    with open("input_ip.txt", 'r', encoding="UTF8") as f:
        #
        # for line in f:
        #     print(re.findall(ip4, line))

        for line in ip4.finditer(f.read()):
            print(line.group())

if __name__ == "__main__":
    task()

