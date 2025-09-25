import sys
import exifread

def show_metadata(image_path):
    with open(image_path, "rb") as f:
        tags = exifread.process_file(f)

    if tags:
        for tag, value in tags.items():
            print(f"{tag:35}: {value}")
    else:
        print("메타데이터가 없습니다.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("이미지 파일을 드래그 앤 드롭해서 실행하세요.")
    else:
        image_path = sys.argv[1]
        print(f"분석할 파일: {image_path}\n")
        show_metadata(image_path)
