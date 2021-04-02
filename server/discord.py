import re


def format_is_correct(username):
    format = r"\w{2,32}#\d{4}"
    res = re.search(username, format)
    print(res)
    return res
