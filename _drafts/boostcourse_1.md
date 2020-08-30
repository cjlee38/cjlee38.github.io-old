---
layout: post
title:  "#[부스트코스] 안드로이드 프로그래밍, Project A"
date:   2020-08-28 16:05:00 +0900
categories: [App, BoostCourse]
tags: 
---

[링크](https://www.edwith.org/boostcourse-android/project/5/content/4#summary)
# 1. 요구사항 (Requirements)

**부스트코스 학습을 기반으로 진행하는 프로젝트이기에 JAVA언어를 활용하여 개발하여야 합니다.

단일 레이아웃

1) 영화 상세 정보를 표시하기 위한 화면 레이아웃을 만듭니다.

화면 레이아웃 구성은 아래 그림을 참조하세요.
2) 화면을 구성하기 위해서는 레이아웃과 위젯을 사용합니다. 종류는 아래와 같습니다.

제약 레이아웃(ConstraintLayout), 리니어 레이아웃(LinearLayout), 상대 레이아웃(RelativeLayout) 등의 레이아웃
이미지뷰(ImageView), 텍스트뷰(TextView) 등의 위젯
평점에 사용되는 별의 경우 RatingBar 위젯 사용 (RatingBar 사용방법 : https://developer.android.com/reference/android/widget/RatingBar.html) 
3) 화면에 표시될 내용은 다음과 같습니다.

영화 이미지와 영화 간단 정보(관람등급, 이름, 개봉일, 장르, 시간 등)
좋아요/싫어요 아이콘과 예매율, 평점, 관객 수
줄거리와 감독/출연 배우
페이스북 등으로의 링크 이미지, 예매하기 버튼 표시
4) 한 줄 평을 표시할 공간을 만들어둡니다. (한 줄 평 데이터는 표시하지 않습니다.)

# 2. 설계
* 최상위 Layout : Linear(Vertical)
* Section 구분 명명  
  1. 영화개요
  2. 줄거리
  3. 감독/출연
  4. 한줄평
  5. 예매하기
* 기타  
  1. Application Icon 사용할 것
  2. Application Title은 "시네마천국"
* Custom  
  1. 영화 정보는 JSON으로 저장하기.
  2. 예매하기 Section을 항상 보여주게 하기

# 3. Section 별 상세 설계

### 1) 영화 개요
1. 좌측에는 영화 ImageView
2. 중앙에는 ConstraintLayout
3. ImageView와 영화 정보 Layout은 1:2 비율
4. 영화 연령정보 Icon은 영화의 정보에서 불러와 가져올 것.
5. Thumb-up/Thumb-down Button은 Exclusive하게 작성할 것
6. Thumb-up/Thumb-down Button 클릭 시 현재 숫자 += 1, 재 클릭시 현재 숫자 -= 1
7. Background - Gradient Color

   
### 2) 줄거리
1. "줄거리" String은 Bold, 그리고 본문보다 font-size를 키울 것.

### 3) 감독/출연
1. "감독/출연"은 String은 Bold, 그리고 본문보다 font-size를 키울 것.
2. "감독", "출연" String은 Bold

### 4) 한줄평
1. 한줄평이 작성될 곳은 비워둘 것
2. 작성하기, 모두보기 Button은 아직 연결하지 않을 것

### 5) 예매하기
1. 예매하기, Facbook, KakaoTalk Button 링크는 아직 연결하지 않을 것.

# 4. 결과


# 5. 배운점
: 직접 설계하는 웹/앱 프로젝트는 처음이다보니, 처음 다뤄보는 것들이 많다.
 1. Gradle 빌드
 2. Lombok
 3. VO object 관리
 4. Java에서 JSON 다루기