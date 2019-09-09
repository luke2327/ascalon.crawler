## Ascalon crawler

_Ascalon crawler_

eim 에서 사용하는 크롤러 입니다
  
  
Scrapy version : [추가바람]

Python : 2.7

- - -

지속적인 크롤링을 위해 EC2 에 놓는 크롤러 입니다

## 코드관리
1. 간단한 수정은 EC2 에 접속하여 수정합니다
2. 보통은 로컬에서 짠 후 클론 받아 테스트 진행합니다
+ 현재 Ruso 가 외부 테스트 진행 방안 검토 중

## 폴더 구조
#### spiders [ascalon/spiders/]
실제로 크롤링 되는 코드들이 모여져 있는 곳 입니다

#### pipelines [ascalon/pipelines/]
스파이더에서 넘겨받은 크롤링 데이터들을 처리하는 곳 입니다

#### settings [ascalon/settings]
크롤러의 각종 셋팅이 모여 있는 곳 입니다

## 사용법
scrapy [명령] [스파이더 이름]

ex) scrapy crawl vod_youtube_list

## 스파이더 명명 규칙
vod_youtube_list

첫 언더바 앞에 있는 단어는 크롤링 형식에 맞게 씁니다. 추후 추가될 예정

ex) vod, hlvod, rating, game, blog, ...
