from enum import Enum
import sys
import os
from types import FrameType

class Text_Color(Enum):
    RESET = "\033[0m"
    RED = "\033[31m"
    GRENN = "\033[32m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"

class Debug:
    def get_frame(self):
        """

        """
        frame = sys._getframe()
        while frame.f_back and frame.f_back.f_back:
            frame = frame.f_back
        return frame

    def get_frame_info(self, frame: FrameType):
        """
        호출한 함수의 이름, 파일명, 줄 번호 반환
        """
        
        func_name = frame.f_code.co_name
        full_path = frame.f_code.co_filename
        file_name = os.path.basename(full_path)
        line_no = frame.f_back.f_lineno

        return (func_name, file_name, line_no)

    def format_text_color(self, color: Text_Color, text):
        return f"{color.value}{text}{Text_Color.RESET.value}"

    def print_with_color(self, color: Text_Color, text):
        print(f"{color.value}{text}{Text_Color.RESET.value}")
        
    def debug_text(self, frame: FrameType):
        func_name, file_name, line_no = frame
        output_text = (
            f"(File \"{file_name}\", line {line_no} in \"{func_name}\")"

        )
        return output_text

    def error(self, text):
        frame = self.get_frame()
        frame_data = self.get_frame_info(frame)

        edited_text = f"[Error]: {text} "
        modified_text = self.format_text_color(Text_Color.RED, edited_text) + self.debug_text(frame_data)
        self.print_with_color(Text_Color.RED, modified_text)

    def test(self, text):
        print(self.format_text_color(Text_Color.CYAN, text))

obj = Debug()

def test():
    data = 1
    if data > 0:
        obj.error("test func failed")
        obj.test("hello")

test()


"""
입력한 텍스트 + 자동 생성 텍스트 구분
- 입력한 텍스트
    - 가독성을 위해 지정된 색상으로 출력
- 자동 생성 텍스트 = 사용된 함수명, 파일명, 줄번호
    - 색상x

함수 기능 세분화 및 단일책임을 지도록 변경해야함
"""