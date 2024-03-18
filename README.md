# django-backend-youtube

## 3월 14일 프로젝트 시작 ! 
    # 1. GitHub
        - 레포지토리 생성 -> github 셋팅 

    # 2. Docker Hub
        - 나의 컴퓨터에 가상환경을 구축 ( 리눅스 환경 )
        - Access Token 생성 -> secret Variable 등록
    
    # 3. 장고 프로젝트 셋팅
        - requirement.txt  => 실제 배포할 때 사용
        - requirement.dev.txt => 개발하고 연습할 떄 사용 (파이썬 패키지 관리) 
        - 실전 : 패키지 의존성 관리 => 버전 관리, 패키지들 간의 관계 관리




## 모델 구조 

1. User (Custom)
- email
- password
- nickname
- is_business(boolean): personal, business

2. Video
- title
- link
- description
- category
- views_count
- thumbnail
- video_uploaded_url (S3)
- video_file(FileField)
- User:FK

3. Reaction
- User:FK
- Video:FK
- reaction

4. Comment
- User:FK
- Video:FK
- like
- dislike
- content

5. Subcription (채널 구독)
- User:FK => subscriber (구독한) -> 내가 구독한 사람
- User:FK => subscribed_to (구독을 당한) -> 나를 구독한 사람

6. Common

- created_at
- updated_at

만들어야 하는 테이블 (모델)
 - users, video, reactions, comments, subsriptions, common
 - docker-compose run --rm app sh -c 'python manage.py startapp '

## Custom User Model Create
- TDD => 개발 및 디버깅 시간을 엄청나게 줄일 수 있다. PDB(Python Debugger)

      