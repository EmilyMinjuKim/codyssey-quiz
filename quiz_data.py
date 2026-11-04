from quiz import Quiz


def create_default_quizzes():
    return [
        Quiz(
            question="git init을 실행하기 전에 현재 폴더의 전체 경로를 확인하려면?",
            choices=["ls", "pwd", "cd", "mkdir"],
            answer=2,
        ),
        Quiz(
            question="스테이징한 변경 사항을 내 Mac의 Git 이력에 기록하는 명령은?",
            choices=["git push", "git status", "git add", "git commit"],
            answer=4,
        ),
        Quiz(
            question="실행을 마친 hello-world 컨테이너까지 목록에 표시하는 명령은?",
            choices=["docker ps -a", "docker ps", "docker images", "docker info"],
            answer=1,
        ),
        Quiz(
            question="포트를 8080:80으로 연결했다. Mac의 브라우저에서 접속할 포트는?",
            choices=["80", "443", "8080", "8000"],
            answer=3,
        ),
        Quiz(
            question="Mac의 site 폴더를 컨테이너에 직접 연결한 방식은?",
            choices=["이미지 빌드", "바인드 마운트", "포트 매핑", "볼륨 생성"],
            answer=2,
        ),
    ]