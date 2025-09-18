from enum import Enum

class Text_Color(Enum):
    RESET = "\033[0m"
    RED = "\033[31m"
    GRENN = "\033[32m"
    YELLOW = "\033[33m"


print(f"{Text_Color.GRENN.value}Test_Green{Text_Color.RESET.value}")