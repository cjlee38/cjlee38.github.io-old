---
layout: post
title:  "# Flutter 기본 설치 ( Windows 10 )"
date:   2020-09-06 06:11:00 +0900
categories: [Flutter]
tags: 
---

---
> Note. (임의 선택) -> 제시된 것 이외의 다른 것을 선택해도 무방함.

---

# 1. Flutter 설치

**Windows 10 (64bit) 기준**

[다운로드 주소](https://flutter.dev/docs/get-started/install/windows)

1. stable version(2020.09.06 기준 1.20.3) 다운로드
![download_flutter](/assets/images/2020-09-06-06-14-05_2020-09-06-flutter_0.md.png){: .alignCenter}
2. zip 파일 압축 해제 이후, C:\src\flutter에 압축 해제
![extract_zip](/assets/images/2020-09-06-06-16-38_2020-09-06-flutter_0.md.png){: .alignCenter}

# 2. 환경 변수 편집

1. 제어판 - 시스템 - 좌측 "고급 시스템 설정" - "고급 탭" - "환경 변수" 클릭
![env_var](/assets/images/2020-09-06-06-33-59_2020-09-06-flutter_0.md.png){: .alignCenter}
2. 시스템 변수 - Path 클릭 및 편집 버튼 클릭 - 새로만들기 - C:\src\flutter\bin 추가 후 확인.
3. 시작 - 실행 - cmd - flutter --version 입력 후 나오는지 확인
![env_var2](/assets/images/2020-09-06-07-08-35_2020-09-06-flutter_0.md.png){: .alignCenter}


# 2. Android Studio 설치

[다운로드 주소](https://developer.android.com/studio?hl=ko)

1. 설치 파일 다운로드 이후, 설치 진행
![android_stduio_installation](/assets/images/2020-09-06-06-19-12_2020-09-06-flutter_0.md.png){: .alignCenter}
2. 안드로이드 스튜디오 실행
3. Import studio settings from -> Do not import settings 선택
4. Android Studio Setup wizard 실행 시  
   1) 첫 화면 : Next  
   2) Setup : Standard와 Custom 중 Standard 선택  
   3) Theme : (임의 선택) 취향대로 테마 선택. Darcula  
   4) Finish  
5. Welcome Screen에서, 우측 하단 Configure - Settings 클릭
![Welcome_screen](/assets/images/2020-09-06-06-37-23_2020-09-06-flutter_0.md.png){: .alignCenter}
6. 좌측 Plugin 클릭 - flutter 검색 - Install
![flutter_plugin](/assets/images/2020-09-06-06-39-13_2020-09-06-flutter_0.md.png){: .alignCenter}
7. 경고 메시지는 Accept & Install.
8. 플러그인 설치 완료 후, Restart IDE (재시작)
![success](/assets/images/2020-09-06-06-41-35_2020-09-06-flutter_0.md.png){: .alignCenter}
9. 재시작 후, Welcome screen 중앙에 "Start a new Flutter project" 이 보이면 설치 완료.


# 3. 첫 Application 만들기 (for test)

1. 3-9 에서 확인한 Start a new Flutter project 클릭
2. (임의 선택) project name은 원하는대로(e.g. myFirstApp, testFlutter, tesing_app ..)
3. Flutter SDK Path는 **"C:\src\flutter"** & Next click
4. (임의 선택) package name은 그대로 두고, Finish
5. 프로젝트 생성. 우측 상단 AVD manager 아이콘 클릭
![AVD](/assets/images/2020-09-06-06-48-45_2020-09-06-flutter_0.md.png){: .alignCenter}
6. Create Virtual Device 클릭
7. (임의 선택) Phone - Nexus 6 선택
![AVD2](/assets/images/2020-09-06-06-51-13_2020-09-06-flutter_0.md.png){: .alignCenter}
8. (임의 선택) Release Name : Q 우측 Download 버튼 클릭
![AVD3](/assets/images/2020-09-06-06-54-56_2020-09-06-flutter_0.md.png){: .alignCenter}
9. Accept 체크 후 설치(약 5 - 10분 소요) & Next click
10. Emulated Performance - Graphics : Automatic을 Hardware로 변경(하드웨어 가속) (Nexus 이외의 기종일 경우 해당 탭이 없을 수 있음.)
![AVD4](/assets/images/2020-09-06-06-57-37_2020-09-06-flutter_0.md.png){: .alignCenter}
11. Finish 이후 새로 생긴 Virtual Device 우측 Launch 버튼 클릭 및 AVD manager 닫기.
![AVD5](/assets/images/2020-09-06-07-02-42_2020-09-06-flutter_0.md.png){: .alignCenter}
12. 다시 안드로이드 스튜디오로 돌아와서, 우측 상단에, 아래 사진처럼 새로 만든 Virtual Device가 있는지 확인하고, Run 버튼 클릭
![run_app](/assets/images/2020-09-06-07-16-21_2020-09-06-flutter_0.md.png){: .alignCenter}
13. Run된 이후, 실행 중인 Virtual Device에서 다음 사진과 같이 나온다면 성공.
![finish](/assets/images/2020-09-06-07-10-59_2020-09-06-flutter_0.md.png){: .alignCenter}