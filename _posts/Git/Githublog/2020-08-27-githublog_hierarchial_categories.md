---
layout: post
title:  "# Step by Step, Github(Jekyll) 블로그 제작기 (3) - 카테고리, 계층 카테고리"
date:   2020-08-27 06:16:00 +0900
categories: [Githublog]
tags: 
author: cjlee
cover: /assets/covers/githublog.jpg
---

# 1. 무엇을 할 것인가?

: 카테고리를 만들어서, 관리해보자. 일반적인 카테고리, 그리고 계층을 갖는 카테고리까지 만들어보자. 

1. 좌측 Navigation Bar
2. Category ( without Hierarchy )
3. Category ( with Hierarchy )


# 2. Navigation Bar
: [PlainWhite Theme](https://github.com/samarsault/plainwhite-jekyll) 에서 기본적으로 Navigation Bar를 지원해준다. 

![navigation_bar](/assets/images/2020-08-27-06-18-34_2020-08-27-githublog_3.md.png){: .alignCenter}

_config.yml 파일을 열어, 위 양식대로, 그리고 내가 원하는대로 title을 붙여주자. 나는 Language, Algorithm라는 두개의 카테고리를 만들 예정이다. 

그리고, **url은 앞에 "/category"를 붙여주자.** 즉, 최종 모양은 이렇게 생길 것이다.
```yaml
plainwhite: 
  navigation:
    - title: "Language"
      url: "/category/Language"
    - title: "Algorithm"
      url: "/category/Algorithm"
```

그리고 실행하면, 404 Not Found 가 뜰 것이다. 이는 내가 원하는 url을 붙여주긴 했는데, Jekyll에선 이것이 뭘 의미하는지 알지 못해서 발생하는 일이다. 

마치 "우리 집으로 와" 했는데, "우리 집"의 실제 주소를 알려주지 않은 것과 같다.

---
> Note. default.html에서 navigation에 해당하는 부분은 다음의 코드와 같다.   
> 혹시 다른 테마를 쓰고 있는 사람이라면, 이 부분을 참고하자.

 ```html
 {{ "{% this " }}%}
 {{ "{% if site.plainwhite.navigation " }}%}
      <nav class="navigation">
        <ul>
            {{ "{% for link in site.plainwhite.navigation " }}%}
          <li>
            <a href="{{ link.url }}">\{\{ link.title \}\}</a>
          </li>
          {{ "{% endfor " }}%}
        </ul>
      </nav>
{{ "{% endif " }}%}
```
---

# 3. Category ( without Hierarchy )

: 이제, 실제 카테고리에 해당하는 부분을 만들어보자.  
먼저, 내가 원하는 것은, 해당 카테고리를 눌렀을 때, 그 카테고리에 해당하는 게시글의 List가 등장하는 것이다.

지난 2편에서, 전체 게시글의 List는 site.posts 임을 확인하였다. 이를 조금 응용하면, **내가 원하는 카테고리에 해당하는 게시글의 List**만 가져올 수 있다.

가장 먼저, root 폴더 하위에 (즉, username.github.io 폴더 바로 밑에 ) category 라는 폴더를 만들어주자. 
그리고 그 밑에, foo.md, bar.md 라는 새로운 파일을 만들고, 다음과 같이 넣어주자

```yaml
---
layout: category
title: Language (혹은 Algorithm)
---
```

다음으로, _layouts 폴더 하위에 category.html 을 만들고, **home.html의 다음 사진에 해당하는 코드 부분을 Copy & Paste** 하자.

![home.html](/assets/images/2020-08-27-06-32-51_2020-08-27-githublog_3.md.png){: .alignCenter}

또한, 코드 가장 상단에
```yaml
---  
layout: default  
---  
```
를 입력하는 것도 **잊지 말자**.

다음으로, \<ul class = "posts"> **바로 밑에**  
**{{ "{% assign category = page.category | default: page.title " }}%}&**
를 넣고,

{{ "{% for post in site.posts " }}%}  
에 해당하는 부분을   
**{{ "{% for post in site.categories[category] " }}%}**
로 바꿔준다.

page.category는 현재 category 이름을 의미한다.  
즉, 기존에 "전체 post에 대하여 for loop" 가 아닌, **"현재 category에 해당하는 post에 대하여 for loop"를 사용하겠다**는 의미이다.

여기까지 했으면, 1차 카테고리는 완성이 된다.


# 4. Category ( with Hierarchy )

나는 계층이 없는 카테고리로는 만족할 수 없다. 따라서, 계층이 존재하는 카테고리를 만들것이다. Language 밑에는 Java, Python, Kotlin 등이 있었으면 좋겠고, Algorithm 밑에는 Theory와 PS가 있었으면 한다.

마찬가지로, 위 내용을 응용하면 된다.

우선, category 폴더 하위에, 상위가 되었으면 하는 카테고리 이름의 폴더를 만들어주자. 따라서, Language라는 폴더와, Algorithm 이라는 폴더를 만든다. 그리고 Language 폴더 하위에, Java.md, Python.md, Kotlin.md, Algorithm 폴더 하위에 Theory.md, PS.md를 각각 만들어준다.

그리고 localhost:4000/category/Language/Python 등을 쳐보면, 잘 나올 것이다. 문제는 Navigation이다.

Navigation Bar를 손보기 위해, _config.yml과 default.html을 손봐야 한다.

먼저, _config.yml의 navigation은 지금같은 구조로는 계층을 표현하기 어렵다. 조금 수정하자

```yaml
plainwhite:
  navigation:
    - title: Language
      url: "/category/Language"
      children:
        - title: Java
          url: "/category/Language/Java"
        - title: Python
          url: "/category/Language/Python"
...
이하 생략
```

children 이라는 새로운 key를 추가해서, 계층을 만들었다. 그리고, default.html을 다음과 같이 수정했다


![before](/assets/images/2020-08-27-07-11-26_2020-08-27-githublog_3.md.png){: .alignCenter}  
<center> Before </center>  

![after](/assets/images/2020-08-27-07-13-35_2020-08-27-githublog_3.md.png){: .alignCenter}
<center> After </center>  

기존의 navigation bar에, 주석처리의 가운데 부분을 새로이 추가해줬다. 이 말인 즉슨,

link라는 이름을 갖고 있는 **site.plainwhite.navigation의 하위 element들에 대하여**, 
이 link라는 녀석이 children 이라는 요소를 갖고있으면,
link의 children에 해당하는 element들에 대하여 navigation bar에 추가해라.

라는 의미를 갖고 있다.

또한, 상위와 하위에 각각 parent, child 라는 class를 부여한 뒤,  
/assets/css/styles.scss를 수정하여 Font 크기의 구분도 주고,

카테고리가 많아지면서 "about" section이 조금 밀려나서, 
/_sass/ext/plain.scss 에서 class navigation에 해당하는 css도 찾아 조금 수정했다.

# 5. 마치며

머리가 나쁘면 몸이 고생한다고, 글을 쓰다보니, 뭔가 반복적인 행위를 하는 것도 있고, 조금 비효율적인 부분도 있는 것 같은데, 이를 해결하려면 또 다시 뜯어고쳐야 할 것 같아서 그만두었다. 

나중에 필요할 때 수정해야지..