class PathNotExists(Exception):
    def __init__(self):
        super().__init__("존재하지 않는 path 입니다.")

class FileNotExists(Exception):
    def __init__(self):
        super().__init__("파일이 존재하지 않습니다.")