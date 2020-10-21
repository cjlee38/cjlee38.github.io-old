---
layout: post
title:  "# Step by Step, Github(Jekyll) 블로그 제작기 (2) - 구글애널리틱스, 게시글 개수"
date:   2020-08-26 01:03:36 +0900
categories: [Githublog]
tags: [github]
---

# 0. 무엇을 할 것인가?

: [지난 1편](https://cjlee38.github.io/github/githublog/2020/08/25/githublog_1.html)에서, Github의 호스팅과 Jekyll 을 이용해서 초기 사이트를 제작했다.  
다음으로, 구글 애널리틱스를 걸어놓고, 본격적인 블로그 커스터마이징을 시작해보자.  

* Google Analytics 
* Customizing (feat. Understanding of Jekyll Directory Structure)

# 1. Google Analytics

### 1) Google Analytics 생성

: 먼저, [구글 애널리틱스](https://analytics.google.com/)에 가입한 이후, 새 계정을 만든다. 

계정의 이름, 웹사이트 이름을 원하는 대로 짓고, 웹사이트 URL은 username.github.io 로, 그리고 카테고리와 사용시간대를 설정해준다. 

![ga1](/assets/images/2020-08-27-02-51-12.png){: .alignCenter}
<center>( 나는 기존에 티스토리를 위해 계정을 생성했기 때문에, 새로운 속성을 추가했다.) </center>


다음으로, **좌측하단의 톱니바퀴** 를 눌러, 관리 페이지로 이동한 뒤, 추적 정보 - 추적 코드에 있는 내 추적 ID를 복사했다.

### 2) Jekyll 설정

: 내 웹사이트에 방문자가 생길 때마다 Google Analytics로 Data를 보내주려면, 내 웹사이트에도 무언가가 있어야 함은 자명하다. 

[Plainwhite Theme](https://github.com/samarsault/plainwhite-jekyll)의 제작자는 친절하게도 이 기능을 _config.yml 에서 간단하게 이용할 수 있도록 해 주었다.

![ga2](/assets/images/2020-08-27-03-10-05_2020-08-27-githublog_2.md.png){: .alignCenter}

따라서, _config.yml 파일에, plainwhite 하위에 위 사진과 같이 추가해주면 손쉽게 해결할 수 있다.

---
> ### **Note. PlainWhite Theme가 아닌 경우** 
> 본인이 사용하는 테마가 이러한 기능을 지원해주지 않는 경우, 직접 만들면 된다.  
>
> 앞서, 내가 Git으로 Clone한 폴더(username.github.io)로 이동한 뒤, _layouts 폴더 하위에 있는 default.html을 수정해주면 된다.
>
>앞서 추적 ID를 확인했던 Google Analytics 관리 페이지를 가보면, 이러한 것을 볼 수 있다.
>
> ![ga3](/assets/images/2020-08-27-03-17-08_2020-08-27-githublog_2.md.png){: .alignCenter}
> <center> (ID는 본인의 ID가 입력이 되어 있을 것이다.) </center>  

>해당 코드를 html,header 태그 사이에 Copy & Paste 해주면 된다.

---

# 2. Customizing (feat. Understanding of Jekyll Directory Structure)

: 구글링을 통해, 다른 사람들이 깃허브 블로그를 어떻게 꾸몄는지를 보면, 알쏭달쏭하다.
뭔가 비슷하면서도 묘하게 다른것이, 처음 봤을때 단박에 이해하기가 어려웠다. (지금도 완벽하게 이해하지는 못했지만, 필요한 만큼 커스텀은 할 수 있다.)

[Jekyll Documentation](https://jekyllrb-ko.github.io/docs/structure/)의 설명을 보면, 조금은 도움이 될 지 모르겠다.


가장 먼저, 우리가 크게 신경써야 할 폴더 및 파일은 다음과 같다
1. _config.yml
2. _layouts
3. _includes
4. _posts

### 1) _config.yml

: 핵심이 되는 _config.yml 에서는 기본적인 환경설정에 대한 정보를 입력할 수 있다. YAML 형식으로 입력되는 이 파일에 있는 데이터를, HTML 내에서 [Liquid](https://shopify.github.io/liquid/) 라는 언어를 통해 사용할 수 있다. 아주 직관적이고 간단한 언어라, 습득하는데 30분도 채 걸리지 않을 것이다. 

간단하게 살펴보자면, HTML내에 Liquid 를 삽입하려면 다음과 같은 두가지 방식이 있다.
* \{\{ \}\}
* {{ "{% " }}%}  

그리고, Liquid 에서는 **assign**이라는 Keyword를 통해 변수를 할당할 수 있다.  
따라서, 위 내용을 종합하여, 다음을 따라해보자.

1. _config.yml에 **test_var = "Hello world!"** 를 추가한다
2. _layouts 폴더에 있는 default.html 에, 다음 사진과 같이 추가한다.
3. bundle exec jekyll serve를 통해 Jekyll을 실행시킨다.
 
![default.html](/assets/images/2020-08-27-03-51-31_2020-08-27-githublog_2.md.png){: .alignCenter}
  
--- 
> Note. 1편에서도 말했지만, _config.yml 파일의 수정은 즉시 적용되지 않는다. 반드시 Ctrl + C를 통해 종료 후 다시 실행시켜주자.

---

localhost:4000 으로 들어가면, Hello world! 가 추가된 것을 확인할 수 있다.  
이렇게 보면, html 파일들 내에 있던 Liquid 가 무엇을 의미하는지 알 수 있을 것이다.

### 2) _layouts

: _layouts 폴더는 말 그대로 레이아웃을 의미한다. 그런데, default.html을 제외한 나머지 .html 파일들의 최상단을 보면 


\-\-\-  
layout: default  
\-\-\-  

이렇게 생긴 것들이 포함되어 있다. 이는, 계층 구조를 의미한다.  

default.html <-- foo.html <-- bar.html ...

이런식으로, bar.html의 내용이 foo.html에 들어가고, foo.html이 default.html에 들어간다는 뜻이다. 이쯤되면 슬슬 감이 잡힌다.

### 3) _include

: _include 폴더는, 재사용 될 수 있는 .html 파일들을 의미한다. 

얼핏 보면 _layouts과 비슷하지만, "재사용성" 이라는 맥락에서 보면 이해가 될 것이다. 일종의 "변수" 인 셈인 것이다. 

### 4) _posts

: _posts 폴더는 내가 작성한 게시글들을 작성하는 곳이다. .md의 마크다운 파일을 작성하고, YYYY-mm-dd-title.md 의 양식을 지켜 파일명을 작성하고, 내부에 작성하면 된다.

마찬가지로, 해당 마크다운 파일들에도 

\-\-\-  
layout: post  
title:  제목  
date:   날짜  
categories: 카테고리  
tags: 태그  
\-\-\-

이런식으로 작성되어 있다. 여기에도 layout이 있으므로, "내가 작성한 게시글이 HTML로 변환된 뒤에, Post의 하위로 들어가는구나" 라는 것을 알 수 있다.

### 5) Practice ( feat. Post Counter )

: 이제 대충 어떻게 돌아가는지 알았으니, 한번 연습을 해보자. vanilla 상태의 PlainWhite Theme는 너무 단순해보인다. 그냥 게시글의 List만 존재하는 것은 너무 밋밋해보인다.

따라서, 나는 게시글마다 게시글 개수의 List가 나타났으면 한다.

먼저, Chrome의 DevTools를 이용해 HTML을 살펴보니, 게시글의 List는 다음의 태그에 해당한다.
```html
<ul class="posts"> <ul>
```
따라서, 가장 먼저 default.html을 살펴보니, 해당 부분은 \{\{ contnet \}\} 임을 알 수 있었다.
그리고, home.html 을 열어보니, \<ul class="posts"> 가 존재하는 것을 확인할 수 있다. 

그렇다면, 우리가 localhost:4000 을 열었을 때의 Landing Page는 default.html을 상위로 두는 home.html임을 알 수 있다.

[Jekyll Documentation](https://jekyllrb-ko.github.io/docs/variables/) 의 사이트 변수를 살펴보면, 
site.posts 는 "시간 역순의 모든 포스트 목록" 이라고 한다. 

---
> Note. 게시글의 개수는 유동적이므로, for문을 통해 각각의 게시글이 표현될 것임은 당연하다.  
> 따라서, home.html의 for문을 살펴보면 for post in site.posts 가 존재하므로, 이것이 게시글의 목록을 표현해줌 역시 자명하다.  

---

또한, [Liquid Documentation](https://shopify.github.io/liquid/filters/size/) 의 size Filter를 보면, 개수를 나타내준다는 것도 알았다.

이쯤되면, 이제 답은 나왔다.

\<ul class="posts"> 바로 밑에, 다음의 태그를 추가해주자.

```html
<ul class="posts">

    <p class="post-counter"> Entire ({{ "{{ site.posts | size " }}}}) </p>
    ...
</ul>
```

그리고, /assets/css 에 존재하는 style.scss를 열어 내 입맛대로 css를 추가해줬다.

```css
.post-object,
.post-counter {
  border-bottom: 1px solid silver;
  padding: 1em;
}
.post-counter {
  text-align: right;
  font-size: xx-large;
  font-style: italic;
}
```

웹브라우저의 새로고침을 해보자. 

![custom1](/assets/images/2020-08-27-04-34-20_2020-08-27-githublog_2.md.png){: .alignCenter}

잘 작동하는 것을 확인할 수 있다.
