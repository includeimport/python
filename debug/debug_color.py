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
        
    def debug_text(self, title, text, frame: FrameType):
        func_name, file_name, line_no = frame
        output_text = (
            f"[{title}]: {text}"
            f" (File \"{file_name}\", line {line_no} in \"{func_name}\")"

        )
        return output_text

    def check_simple(self, text):
        modified_text = (f"[Check]: {text}")
        self.print_with_color(Text_Color.CYAN, modified_text)

    def check(self, text):
        modified_text = self.debug_text("check", text, self.get_frame_info(inspect.currentframe()))
        self.print_with_color(Text_Color.CYAN, modified_text)

obj = Debug()
obj.check_simple("simple test")
obj.check("deep test")

