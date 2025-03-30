import os

# 기존 + 추가된 대학교 목록
universities = [
    "충남대학교", "한국외국어대학교(서울)", "한서대학교", "한양대학교ERICA",
    "한국교통대학교", "명지대학교", "광운대학교", "인하대학교", "삼육대학교",
    "고려대학교", "한성대학교", "남서울대학교", "성균관대학교", "서경대학교",
    "한밭대학교", "영남이공대학교", "서울대학교", "동국대학교", "중앙대학교"
]

# 기본 경로
base_path = r"C:\Users\jjm02\OneDrive\바탕 화면\대학\LikeLion\학술부"

# 하위 폴더 카테고리
categories = ["프론트엔드", "백엔드", "디자인", "공통세션"]

# 폴더 생성
for university in universities:
    for category in categories:
        # 전체 경로
        path = os.path.join(base_path, university, category)
        os.makedirs(path, exist_ok=True)  # 이미 존재하면 생략
        print(f"폴더 생성: {path}")
