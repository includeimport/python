import sys
from PIL import Image
import os

def remove_metadata(image_path):
    img = Image.open(image_path)

    data = list(img.getdata())
    clean_img = Image.new(img.mode, img.size)
    clean_img.putdata(data)

    base, ext = os.path.splitext(image_path)
    output_path = f"{base}_cleaned{ext}"

    clean_img.save(output_path)
    print(f"메타데이터 제거 완료 → {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("이미지 파일을 드래그 앤 드롭해서 실행하세요.")
    else:
        for image_path in sys.argv[1:]:
            print(f"처리 중: {image_path}")
            remove_metadata(image_path)
