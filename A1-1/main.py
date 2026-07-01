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

# 6. 프롬프트 목록 (브랜치 활용)
def show_list():
    print("\n--- 프롬프트 목록 ---")

    if not prompts: # 리스트가 비어있으면(길이 0) 안내 메시지 출력 후 함수 종료
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, start=1):
        star = "⭐" if p["favorite"] else "" # 즐겨찾기 여부에 따라 별 표시 여부 결정
        print(f"{i}. [{p['category']}] {p['title']} {star}") # 요구사항에 명시된 표시 항목(번호, 제목, 카테고리, 즐겨찾기)

# 7. 카테고리별 조회
def show_by_category():
    # 1. 사용 가능한 카테고리 목록을 사용자에게 보여준다
    print("\n--- 카테고리별 조회 ---")
    print("카테고리 목록:", ", ".join(CATEGORIES))

    # 2. 사용자로부터 조회하고 싶은 카테고리를 입력받는다
    selected_category = input("조회할 카테고리를 입력하세요: ").strip()

    # 3. 입력받은 카테고리와 일치하는 프롬프트만 리스트로 걸러낸다 (필터링)
    filtered = [p for p in prompts if p["category"] == selected_category]

    # 4. 해당 카테고리에 프롬프트가 하나도 없는 경우 안내 메시지 출력
    if not filtered:
        print(f"'{selected_category}' 카테고리에 등록된 프롬프트가 없습니다.")
        return

    # 5. 필터링된 프롬프트들을 번호, 제목, 즐겨찾기 여부와 함께 출력
    print(f"\n[{selected_category}] 카테고리의 프롬프트 목록")
    for i, p in enumerate(filtered, start=1):
        star = "⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']} {star}")


# 8. 프롬프트 검색
def search_prompt():
    # 1. 검색할 키워드를 사용자로부터 입력받는다
    print("\n--- 프롬프트 검색 ---")
    keyword = input("검색할 키워드를 입력하세요: ").strip()

    # 2. 키워드가 제목(title) 또는 내용(content)에 포함되어 있는 프롬프트만 필터링
    #    대소문자 구분 없이 검색되도록 둘 다 소문자로 변환하여 비교
    filtered = [
        p for p in prompts
        if keyword.lower() in p["title"].lower() or keyword.lower() in p["content"].lower()
    ]

    # 3. 검색 결과가 없는 경우 안내 메시지 출력
    if not filtered:
        print(f"'{keyword}'를 포함하는 프롬프트가 없습니다.")
        return

    # 4. 검색된 프롬프트들을 번호, 제목, 카테고리, 즐겨찾기 여부와 함께 출력
    print(f"\n'{keyword}' 검색 결과 ({len(filtered)}건)")
    for i, p in enumerate(filtered, start=1):
        star = "⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']} {star}")


# 9. 프롬프트 상세 보기
def show_detail():
    # 1. 먼저 전체 목록을 번호와 함께 보여줘서, 사용자가 몇 번을 볼지 참고할 수 있게 한다
    print("\n--- 프롬프트 상세 보기 ---")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, start=1):
        print(f"{i}. {p['title']}")

    # 2. 사용자로부터 상세히 보고 싶은 프롬프트의 번호를 입력받는다
    user_input = input("상세히 볼 프롬프트 번호를 입력하세요: ").strip()

    # 3. 입력값이 숫자인지 확인 (숫자가 아니면 잘못된 입력으로 처리)
    if not user_input.isdigit():
        print("올바른 번호를 입력해주세요.")
        return

    index = int(user_input) - 1  # 리스트는 0번부터 시작하므로 1을 빼줌

    # 4. 입력한 번호가 실제 목록 범위 안에 있는지 확인
    if index < 0 or index >= len(prompts):
        print("존재하지 않는 번호입니다.")
        return

    # 5. 범위 안에 있으면 해당 프롬프트의 전체 정보를 출력
    p = prompts[index]
    star = "⭐ 즐겨찾기됨" if p["favorite"] else "즐겨찾기 안됨"

    print("\n===== 프롬프트 상세 정보 =====")
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print(f"내용:\n{p['content']}")
    print("===============================")

# 10. 즐겨찾기 관리
def show_favorites():
    print("\n--- 즐겨찾기 관리 ---")
    print("1. 즐겨찾기 추가/해제")
    print("2. 즐겨찾기 목록 보기")

    # 1. 하위 메뉴 선택
    sub_choice = input("원하는 기능을 선택하세요: ").strip()

    if sub_choice == "1":
        # ---- 즐겨찾기 추가/해제 ----

        # 참고용으로 전체 목록(번호, 제목, 현재 즐겨찾기 상태)을 보여준다
        if not prompts:
            print("등록된 프롬프트가 없습니다.")
            return

        for i, p in enumerate(prompts, start=1):
            star = "⭐" if p["favorite"] else ""
            print(f"{i}. {p['title']} {star}")

        # 즐겨찾기를 토글(추가↔해제)할 번호를 입력받는다
        user_input = input("즐겨찾기를 변경할 번호를 입력하세요: ").strip()

        if not user_input.isdigit():
            print("올바른 번호를 입력해주세요.")
            return

        index = int(user_input) - 1

        if index < 0 or index >= len(prompts):
            print("존재하지 않는 번호입니다.")
            return

        # 현재 값의 반대로 바꿔준다 (True면 False로, False면 True로 = 토글)
        prompts[index]["favorite"] = not prompts[index]["favorite"]

        status = "추가" if prompts[index]["favorite"] else "해제"
        print(f"'{prompts[index]['title']}' 프롬프트의 즐겨찾기가 {status}되었습니다.")

    elif sub_choice == "2":
        # ---- 즐겨찾기 목록만 모아서 보기 ----

        # favorite가 True인 항목만 필터링
        favorites = [p for p in prompts if p["favorite"]]

        if not favorites:
            print("즐겨찾기된 프롬프트가 없습니다.")
            return

        print("\n⭐ 즐겨찾기 목록")
        for i, p in enumerate(favorites, start=1):
            print(f"{i}. [{p['category']}] {p['title']}")

    else:
        print("잘못된 선택입니다.")


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