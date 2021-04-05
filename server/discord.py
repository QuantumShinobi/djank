import re


def format_is_correct(username):
    format = r".{2,32}#\d{4}"
    only_whitespace = r'\s*#\d{4}'
    res = re.fullmatch(format, username)
    res2 = re.fullmatch(only_whitespace, username)
    if res2:
        res = "Blank Username"
    print(res)
    return res
