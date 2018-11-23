import unicodedata
import os
import glob
import shutil
from exception.exception import *

class NomalizationFormConverter:
    C_YELLOW = "\033[33m"
    C_GREEN = "\033[32m"
    C_RED = "\033[31m"
    C_BLUE = "\033[34m"
    C_PURPLE = "\033[35m"
    C_END = "\033[0m"

    def setPathGuide(self):
        os.system('clear')
        print(self.C_RED + "작업을 선택해 주세요(default : nfc)" + self.C_END)
        print(self.C_YELLOW + "(mac - nfd , windows - nfc)" + self.C_END)
        print("1. convert nfc to nfd")
        print("2. convert nfd to nfc")
        print(self.C_BLUE)
        self.mode = 'nfd' if int(input("선택 번호 : ")) == 1 else 'nfc'
        print(self.C_END)

        print(self.C_GREEN + "선택된 작업 : nfd\n" + self.C_END) if self.mode == 1 else print(
            self.C_GREEN + "선택된 작업 : nfc\n" + self.C_END)

        print(self.C_RED + "파일 경로를 선택해주세요" + self.C_END)
        print("1. 데스크탑(~/Desktop)")
        print("2. 다운로드(~/Download)")
        print("3. 직접 입력(full path)")
        print(self.C_BLUE)
        self.path_choice = int(
            input("선택 번호 : ")
        )
        print(self.C_END)

    def setPath(self):
        if self.path_choice == 1:
            self.path = os.path.expanduser("~/Desktop/")
        elif self.path_choice == 2:
            self.path = os.path.expanduser("~/Download/")
        else:
            print("경로를 입력해 주세요")
            self.path = str(input("입력 경로 : "))
            self.path = self.path if '~' not in self.path else self.path.replace("~", os.path.expanduser('~'))

        if os.path.isdir(self.path):
            print(self.C_GREEN + "선택된 경로 : " + self.path + "\n" + self.C_END)
            self.path = self.path if self.path.endswith("/") else self.path + "/"
            self.setFile()

        if os.path.isfile(self.path):
            self.selected_file = os.path.basename(self.path)
            self.path = os.path.dirname(self.path) + "/"
            self.nameConverter()

        if not os.path.isfile(self.path) and not os.path.isdir(self.path):
            raise PathNotExists

    def getFiles(self):
        file_list = glob.glob(str(self.path) + "/*")
        if not file_list:
            raise FileNotExists
        for file in file_list:
            yield os.path.basename(file)

    def setFile(self):
        it = self.getFiles()
        files = list(it)
        print(self.C_RED + "파일을 선택해주세요 : " + self.C_END)
        file_list = [file for file in files if os.path.isfile(self.path+file)]

        for num, file in enumerate(file_list, 1):
            print(str(num) + " : " + str(file))

        print(self.C_BLUE)
        num = input("선택된 번호 : ")
        print(self.C_END)
        self.selected_file = file_list[int(num) - 1]
        self.nameConverter()

    def nameConverter(self):
        self.nfc_file = unicodedata.normalize('NFC', self.selected_file)
        self.nfd_file = unicodedata.normalize('NFD', self.selected_file)

    def convert(self):
        self.setPathGuide()
        self.setPath()
        print(self.C_GREEN + "선택된 파일 : " + self.selected_file + self.C_END)

        if self.mode == 'nfd':
            print(self.C_YELLOW + "파일 경로 : " + shutil.move(self.path+str(self.selected_file), self.path+self.nfd_file) + self.C_END + "\n")
        else:
            print(self.C_YELLOW + "파일 경로 : " + shutil.move(self.path + str(self.selected_file), self.path + self.nfc_file) + self.C_END + "\n")

        print(self.C_BLUE + "선택된 경로의 파일 목록 : " + self.C_END)

        it = self.getFiles()
        files = list(it)
        file_list = [file for file in files if os.path.isfile(self.path + file)]
        for num, file in enumerate(file_list, 1):
            if file == self.nfc_file or file == self.nfd_file:
                print(self.C_RED + str(file) + " (변환 작업 파일) " + self.C_END)
            else:
                print(self.C_GREEN + str(file) + self.C_END)


NomalizationFormConverter().convert()

