import re


def BLACK():
    return "\\u00A70"


def DARK_BLUE():
    return "\\u00A71"


def GOLD():
    return "\\u00A76"


def GRAY():
    return "\\u00A77"


def DARK_GRAY():
    return "\\u00A78"


def BLUE():
    return "\\u00A79"


def GREEN():
    return "\\u00A7a"


def AQUA():
    return "\\u00A7b"


def RED():
    return "\\u00A7c"


def LIGHT_PURPLE():
    return "\\u00A7d"


def YELLOW():
    return "\\u00A7e"


def WHITE():
    return "\\u00A7f"


def MAGIC():
    return "\\u00A7k"


def BOLD():
    return "\\u00A7l"


def STRIKETHROUGH():
    return "\\u00A7m"


def UNDERLINE():
    return "\\u00A7n"


def ITALIC():
    return "\\u00A7o"


def RESET():
    return "\\u00A7r"


def getByChar(code):
    if len(code) == 1 and code in "0123456789abcdefklmsnor":
        return "\\u00A7" + code
    return None


def getChar():
    return "\\u00A7"


def stripColor(message):
    return re.sub(r"(?i)\\u00A7[0-9A-FK-OR]", "", message)


def translateAlternateColorCodes(altColorChar, textToTranslate):
    return textToTranslate.replace(altColorChar, '\\u00A7')