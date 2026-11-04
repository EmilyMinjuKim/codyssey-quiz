def show_menu():
    print("=== 나만의 퀴즈 게임 ===")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")


def read_number(prompt, minimum, maximum):
    while True:
        text = input(prompt).strip()

        if not text:
            print("입력이 비어 있어요. 번호를 입력해주세요.")
            continue

        try:
            number = int(text)
        except ValueError:
            print("숫자로 입력해주세요.")
            continue

        if minimum <= number <= maximum:
            return number

        print(f"{minimum}부터 {maximum} 사이의 번호를 입력해주세요.")


def main():
    while True:
        show_menu()
        choice = read_number("선택: ", 1, 5)

        if choice == 5:
            print("게임을 종료합니다.")
            break
        elif choice == 1:
            print("퀴즈 풀기를 선택했어요.")
        elif choice == 2:
            print("퀴즈 추가를 선택했어요.")
        elif choice == 3:
            print("퀴즈 목록을 선택했어요.")
        elif choice == 4:
            print("점수 확인을 선택했어요.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 게임을 종료합니다.")