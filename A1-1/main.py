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
    print("[프롬프트 추가] 기능은 준비 중입니다.")


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