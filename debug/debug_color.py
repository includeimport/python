from enum import Enum
import inspect
import os
from types import FrameType

class Text_Color(Enum):
    RESET = "\033[0m"
    RED = "\033[31m"
    GRENN = "\033[32m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"

class Debug:

    def get_frame_info(self, frame: FrameType):
        """
        호출한 함수의 이름, 파일명, 줄 번호 반환
        """
        func_name = frame.f_code.co_name
        full_path = frame.f_code.co_filename
        file_name = os.path.basename(full_path)
        line_no = frame.f_back.f_lineno

        return (func_name, file_name, line_no)

    def print_with_color(self, color: Text_Color, text):
        print(f"{color.value}{text}{Text_Color.RESET.value}")
        
    def simple_check(self, text):
        self.print_with_color(Text_Color.CYAN, text)

    def check(self, text):
        func_name, file_name, line_no = self.get_frame_info(inspect.currentframe())
        edit_text = (
                f"[Check]: {text}"
                f" (File \"{file_name}\", line {line_no} in \"{func_name}\")"

            )
        self.print_with_color(Text_Color.CYAN, edit_text)

obj = Debug()
obj.simple_check("simple test")
obj.check("deep test")

