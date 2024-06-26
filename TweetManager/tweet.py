import time

class Tweet:
    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = time.time()

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        convert = abs(time.time() - self.__age)

        if convert < 60:
            return f"{int(convert)}s"
        elif convert < 3600:
            return f"{int(convert // 60)}m"
        elif convert < 86400:
            return f"{int(convert // 3600)}h"
        else:
            return f"{int(convert // 86400)}d"
