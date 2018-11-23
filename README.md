# 이슈

- Mac OS와 Windows에서는 각기 다른 Unicode Nomalization Form을 사용하기 때문에
다른 os에서 만든 파일명이 깨지는 현상이 발생합니다.

- Mac OS (NFD), Windows(NFC)

- Mac OS 에서는 "한글.docx" 라고 이름을 지으면, 내부적으로 "ㅎㅏㄴㄱㅡㄹ.docx" 로 풀어서 유니코드를 저장해 놓고 이것을 보여줄 때 "한글.docx" 이라고 조합해서 보여줍니다. 반면 Windows 에서는 "한글.docx"이라고 파일명을 지으면 실제로 "한글.docx"으로 조합된 글자의 유니코드를 저장합니다.

출처 : https://blogs.technet.microsoft.com/spsofficesupportko/2017/01/06/%ED%8C%8C%EC%9D%BC%EB%AA%85%EC%9D%98-%ED%95%9C%EA%B8%80%EC%9E%90%EB%AA%A8%EA%B0%80-%EB%B6%84%ED%95%B4%EB%90%98%EC%96%B4-%EB%B3%B4%EC%97%AC%EC%A7%80%EB%8A%94-%ED%98%84%EC%83%81-unicode-nfd/

# 목적
- 따라서 본 소스 코드는 NFD(Mac OS) -> NFC(Windows) 또는 NFC(Windows) -> NFD(Mac OS)로 변환해 주는 기능을 제공합니다.

# 사용법
 - 1. 본 소스를 내려받습니다.
 - 2. nomalizationFormConverter.py 파일이 있는 경로에서 terminal(mac) 혹은 cmd(Windows)를 열거나
 해당 툴들을 open 후 해당 경로로 이동합니다.
 - 3. python nomalizationFormConverter.py 명령어를 입력합니다.(python이 설치되 있지 않은 경우 python을 설치해야 됩니다.
 - 4. 입력 메뉴얼대로 입력 하시면 됩니다.

 # 주의
 - 본 소스코드는 mac 기준으로 작성되어 windows에서는 정상작동 하지 않을 수도 있습니다.
 - mac directory 기준으로 작성 및 테스트를 진행하여 windows에서 작동하지 않을 수도 있습니다.