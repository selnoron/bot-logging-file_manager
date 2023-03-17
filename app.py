import datetime
from random import choice as ch


def get_timestamp() -> str:
    current_timestamp: datetime.datetime = \
            datetime.datetime.now()
    format_timestamp = \
        current_timestamp.strftime(
            '%d/%m/%Y, %H:%M:%S'
        )
    return format_timestamp

def get_error_code(func, el: str) -> str:
    try:
        func(el)
        return "200"
    except:
        return "fail"

def logar(func, el: str) -> None:
    with open('log.txt', 'a') as file:
        file.write(
            '[{0}] {1} - {2}\n'
            .format(
                get_timestamp(),
                func.__name__,
                get_error_code(func, el)
            )
        )
    
def log(funcc):
    def wrapper(arg1: int):
        logar(func=funcc, el=arg1)

    return wrapper

@log
def add_bot(text: int):
    with open('bot.txt', 'r+') as bot:
        bot.write(f"{text}\n")
        text_content: list[str] = bot.readlines()
        print(ch(text_content))

add_bot(input("Enter phrase - "))



