from quiz import Quiz
from quiz_data import create_default_quizzes

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


def play_quiz(quizzes):
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    correct_count = 0
    total = len(quizzes)

    for number, quiz in enumerate(quizzes, start=1):
        print(f"\n[문제 {number}/{total}]")
        quiz.display()
        selected = read_number("정답 번호(1~4): ", 1, 4)

        if quiz.is_correct(selected):
            print("정답입니다!")
            correct_count += 1
        else:
            answer_text = quiz.choices[quiz.answer - 1]
            print(f"오답입니다. 정답은 {quiz.answer}번 '{answer_text}'입니다.")

    print(f"\n결과: {total}문제 중 {correct_count}문제 정답")
    return correct_count

def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("내용을 입력해주세요.")


def add_quiz(quizzes):
    print("\n[퀴즈 추가]")
    question = read_text("문제: ")

    choices = []
    for number in range(1, 5):
        choice = read_text(f"선택지 {number}: ")
        choices.append(choice)

    answer = read_number("정답 번호(1~4): ", 1, 4)
    new_quiz = Quiz(question=question, choices=choices, answer=answer)
    quizzes.append(new_quiz)

    print(f"퀴즈를 추가했습니다. 현재 총 {len(quizzes)}문제입니다.")

def main():
    quizzes = create_default_quizzes()

    while True:
        show_menu()
        choice = read_number("선택: ", 1, 5)

        if choice == 5:
            print("게임을 종료합니다.")
            break
        elif choice == 1:
            play_quiz(quizzes)
        elif choice == 2:
            add_quiz(quizzes)
        elif choice == 3:
            print("퀴즈 목록을 선택했어요.")
        elif choice == 4:
            print("점수 확인을 선택했어요.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 게임을 종료합니다.")