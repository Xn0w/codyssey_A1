# Git Command 정리 — codyssey_A1 프로젝트

`https://github.com/Xn0w/codyssey_A1` 저장소를 만들고 진행하면서 사용한 Git 명령어를 순서대로 정리한 문서입니다.

## 1. 개발 환경 설정

```bash
python3 --version                            # Python 버전 확인 (3.12.13)
git --version                                # Git 버전 확인 (2.54.0)
git config --global user.name "Xn0w"
git config --global user.email "lyinsics@gmail.com"
git config --global init.defaultBranch main  # 앞으로 만들 저장소 기본 브랜치를 main으로 설정
```

## 2. 로컬 저장소 초기화 및 첫 커밋

```bash
cd ~/Documents/wonkyu
git init                                     # wonkyu 폴더를 Git 저장소로 초기화
git add .
git commit -m "Initial commit: hello.py"
git branch                                   # 확인해보니 master로 생성됨
git branch -M main                           # master를 main으로 이름 변경
```

## 3. GitHub 원격 저장소 연결 및 첫 push

```bash
git remote add origin https://github.com/Xn0w/codyssey_A1.git
git push --set-upstream origin main          # 최초 push (upstream 연결)
```

## 4. 로컬-원격 히스토리 충돌 해결

GitHub 웹에서 파일을 직접 업로드하여 로컬과 원격의 커밋이 갈라진(diverged) 상황을 해결.

```bash
git config pull.rebase false                 # merge 방식으로 병합하도록 설정
git pull                                      # 원격 변경사항 가져와서 병합
git push                                      # 병합 결과 다시 push
```

## 5. 폴더/파일 구성 정리

```bash
mkdir A1-1                                   # 과제용 폴더 생성 (또는 GitHub 웹에서 생성 후 pull)
git mv main.py A1-1/main.py                  # 파일 이동
touch .gitignore
touch README.md
git add .
git commit -m "Add A1-1/hello.py, .gitignore, README"
git push
```

## 6. 공개 샘플 저장소 clone 실습 (별도 폴더, 학습용)

```bash
cd ~/Desktop
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
ls -la
git log
cd ..
rm -rf Hello-World                           # 구조/로그 확인 후 삭제
```

## 7. 기능별 브랜치 작업 (요구사항 6번: 목록 보기)

```bash
cd ~/Documents/wonkyu
git checkout -b feature/prompt-list          # 새 브랜치 생성 + 이동

# ... show_list() 구현 및 테스트 ...

git add .
git commit -m "Implement show_list() with favorite star display"
git push -u origin feature/prompt-list       # 새 브랜치를 원격에도 올림
git checkout main                            # main으로 복귀
git merge feature/prompt-list                # feature 브랜치를 main에 병합
git push                                     # 병합 결과 push
```

## 8. 나머지 기능 구현 (main 브랜치에서 계속 진행)

```bash
# 카테고리별 조회
git add .
git commit -m "Implement show_by_category() with filtering"
git push

# 프롬프트 검색
git add .
git commit -m "Implement search_prompt() by title and content"
git push

# 상세 보기
git add .
git commit -m "Implement show_detail() with input validation"
git push

# 즐겨찾기 관리
git add .
git commit -m "Implement show_favorites() with toggle and filtering"
git push
```

## 9. README 완성

```bash
git add .
git commit -m "Complete README.md with usage, features, and categories"
git push
```

## 10. 폴더 구조 재정리 (code, images, report 폴더)

```bash
git pull                                     # GitHub 웹에서 만든 code 폴더 반영
git mv A1-1/main.py A1-1/code/main.py
git mv A1-1/hello.py A1-1/code/hello.py
mkdir A1-1/report A1-1/images
mv A1-1/*.png A1-1/images/                   # 스크린샷 이동
touch A1-1/report/.gitkeep                   # 빈 폴더 유지용 더미 파일
git add .
git commit -m "Move screenshots into A1-1/images folder"
git commit -m "Add report folder with .gitkeep placeholder"
git push
```

## 11. 최종 검증용 명령어

```bash
git log --oneline --graph                    # 전체 커밋 및 병합 기록 확인
git log --oneline | wc -l                    # 커밋 개수 세기
git status                                   # 현재 작업 상태 확인
```

---

## 명령어 개념 정리

| 명령어 | 역할 |
|---|---|
| `git init` | 현재 폴더를 Git 저장소로 초기화 |
| `git remote add origin <url>` | 로컬 저장소를 GitHub 원격 저장소와 연결 |
| `git add .` | 변경된 모든 파일을 커밋 대상(스테이징)으로 등록 |
| `git commit -m "메시지"` | 스테이징된 변경사항을 하나의 기록(커밋)으로 저장 |
| `git push` | 로컬 커밋을 원격 저장소에 업로드 |
| `git pull` | 원격 저장소의 변경사항을 로컬로 가져와 병합 |
| `git branch -M main` | 현재 브랜치 이름을 main으로 변경 |
| `git checkout -b <이름>` | 새 브랜치를 생성하면서 동시에 그 브랜치로 이동 |
| `git checkout <이름>` | 이미 존재하는 브랜치로 이동 |
| `git merge <브랜치명>` | 현재 브랜치에 다른 브랜치의 변경사항을 합침 |
| `git mv <원본> <대상>` | 파일을 이동하면서 Git에게 "이동"으로 인식시킴 |
| `git log --oneline --graph` | 커밋 히스토리를 그래프 형태로 한눈에 확인 |
