# 적용할 프롬프트
prompts = [
    {
        "title": "종균 배포 시스템 요구사항 분석 (Few-shot)",
        "content": (
            "당신은 스마트팜 IT 시스템 설계 전문가입니다. "
            "아래 예시들을 참고하여, 종균(버섯 배양균) 유통 및 재고 관리를 위한 "
            "소프트웨어 시스템의 기능 요구사항을 사용자 스토리 형식으로 도출해주세요. "
            "안전 가드레일: 재고 부족/유통기한 임박 상황에 대한 경고 로직을 반드시 포함할 것."
        ),
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "QUANTA 핀테크 광고 영상 컨셉 프롬프트",
        "content": (
            "가상의 핀테크 플랫폼 'QUANTA'의 브랜드 광고 영상을 제작하려 합니다. "
            "타겟은 20~30대 초기 투자자이며, 톤앤매너는 신뢰감 있고 미래지향적입니다. "
            "15초 분량의 광고 스토리보드(장면별 비주얼 설명, 카피 문구)를 작성해주세요."
        ),
        "category": "영상 생성",
        "favorite": True
    },
    {
        "title": "SNS 자동화 파이프라인 - Instagram 캡션 생성",
        "content": (
            "다음 주제에 대해 Instagram 게시물용 캡션을 작성해주세요. "
            "조건: 이모지 2~3개 포함, 해시태그 5개 포함, 친근하고 활기찬 톤, "
            "전체 글자 수는 300자 이내로 작성할 것. 주제: {topic}"
        ),
        "category": "자동화",
        "favorite": False
    },
]

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

def show_menu():
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("0. 종료")
    print("===================================")

def add_prompt():
    print("\n--- 새 프롬프트 추가 ---")

    # 제목 입력 (빈 값 방지)
    while True:
        title = input("제목을 입력하세요: ").strip()
        if title:
            break
        print("제목은 비워둘 수 없습니다. 다시 입력해주세요.")

    # 내용 입력 (빈 값 방지)
    while True:
        content = input("내용을 입력하세요: ").strip()
        if content:
            break
        print("내용은 비워둘 수 없습니다. 다시 입력해주세요.")

    # 카테고리 선택
    print("카테고리 목록:", ", ".join(CATEGORIES))
    category = input("카테고리를 선택하거나 직접 입력하세요: ").strip()
    if not category:
        category = "기타"

    # 리스트에 새 프롬프트 추가
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_prompt)

    print(f"'{title}' 프롬프트가 추가되었습니다.")


def show_list():
    print("[프롬프트 목록] 기능은 준비 중입니다.")


def show_by_category():
    print("[카테고리별 조회] 기능은 준비 중입니다.")


def search_prompt():
    print("[프롬프트 검색] 기능은 준비 중입니다.")


def show_detail():
    print("[프롬프트 상세 보기] 기능은 준비 중입니다.")


def show_favorites():
    print("[즐겨찾기 관리] 기능은 준비 중입니다.")


#def main():
def main():
    while True:
        show_menu()
        choice = input("메뉴 번호를 입력하세요: ")

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            show_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()