---
layout: post
title:  "# Step by Step, Github(Jekyll) 블로그 제작기 (4) - 카테고리 Remake"
date:   2020-08-29 19:16:00 +0900
categories: [Githublog]
tags: 
---

# 1. 무엇을 할 것인가?
 : 카테고리를 바꾼지 얼마 지나지 않아, 몇 가지 불만족스러운 점이 생겼다.

 1. 우선, 카테고리가 아주 많이 늘어날 것 같은데, 이를 일일히 마크다운을 생성하는 것이 비효율적이라 느껴졌다.
 2. 글을 작성할 때마다 Front Matter의 categories에 상위 카테고리 또한 작성해야 한다.
 3. 또한, 좌측 Navigation Bar가 고정되어 있어서, 카테고리가 늘어남에 따라 Size를 조절해줘야 하는 문제가 생겼다.
 4. 게시글이 늘어나면 Paging이 필요하다.

우선 1,2번을 먼저 해결하고, 다음 포스팅 때 3,4번에 대해서 작성해보고자 한다.
# 2. 어떻게 할 것인가?

### 1) Markdown 파일 생성
: 이를 해결하기 위해선, 다음의 방법들이 떠올랐다.
1. Jekyll을 빌드할 때에, category를 확인하여 Build하게 하는 방법
2. categories.md 라는 하나의 파일을 생성해놓고, 카테고리를 클릭하면 이에 해당하는 category가 rendering 되게 하는 방법
   
그러나, 1번의 방법은 내가 Github의 호스팅을 이용하고 있기도 했고, Ruby라는 언어를 새로 공부하고, 프레임워크를 뜯어고치고.. 일일히 이걸 다 할 자신이 없어서 그만뒀다.

2번의 방법은 나름 타당해보였는데, 여러 시도 끝에 결국 사용하지 않기로 하였다. 2번의 방법을 사용하기 위해선 다음과 같은 조건들이 필요했다.  
* categories 라는 하나의 URL에서, "내가 현재 어느 카테고리인지" 구분할 수 있는 "current_category" 변수를 얻는 것.
* layout 간 current_category 의 변수 전달이 가능해야 할 것.
* 같은 URL(/categories)에서, 다른 "current_category" 변수일 경우, 다시 rendering 하는 것.

아마, 동적 사이트였다면 이를 해결하기가 그리 어렵지 않았을텐데, **정적 사이트라는 한계**에서 이를 모두 구현하기란 쉽지 않았다. 

이것저것 시도해보다가 "그나마" 하나 배운 점이라면, liquid Variable을  
{% raw %} 
{% assign myVar = "hello world!" %}  
이와 같이 선언 및 정의했다면, 이를 Javascript의 Function으로 넘겨주려면     
myFunction('{{ myVar }}')    
이렇게 해주어야 한다는 것이다.
{% endraw %}  

좌우지간, 위와 같은 이유로 1번은 하지 않는 것으로 결정내렸다.

### 2) category를 하나만 적기.
: 현재 상태는, 하위 카테고리에 속한 게시글을 하나 작성하려면, 작성한 글에그 상위에 해당하는 카테고리도 포함시켜야 한다. 

![1](/assets/images/2020-08-29-23-41-03_2020-08-27-githublog_4.md.png){: .alignCenter}
<center> 현재는 이렇게 카테고리를 두 개씩 적어야 했다. </center>


또한, category 하위의 URL을 하나하나 적는 것도 꽤나 수고스러운 일이다.   
해서, 일단 _config.yml을 다음과 같이 수정하였다.

```yaml
plainwhite: 
...

  navigation: 
    - title: Diary
    - title: Linux
    - title: App
    - title: Data
      children: [Data_Engineering]
...

이하 생략
```

그리고, default.html의 Navigation Bar에 해당하는 부분 또한 수정하였다.
{% raw %}
```html
      {%- if site.plainwhite.navigation -%}
      <nav class="navigation">
        <ul>
          <!-- edited for sub category -->
          {% for parent in site.plainwhite.navigation %}
          <li>
            <a class="parent" href="{{ "/category/" | append: parent.title }}">{{ parent.title }}</a>
          </li>
          {% if parent.children %}
          <ul>
            {% for child in parent.children %}
            <li>
              <a class="child" href="{{ "/category/" | append: parent.title | append: "/" | append: child }}"> - {{ child }}</a>
            </li>
            {% endfor %}
          </ul>
          {% endif %}
          {% endfor %}
          <!-- edited for sub category -->
        </ul>
      </nav>
      {%- endif -%}
```
{% endraw %}
해당 코드가 이해가 되지 않는다면, [지난 3편](https://cjlee38.github.io/git/githublog/2020/08/26/githublog_3.html)의 내용을 복습해보자.
{: .caption}

그리고, _layouts 폴더 하위에 있는 category.html의 list를 나타내는 내용도 수정해주자.
```html
{% raw %}
{%- if site.posts.size > 0 -%}
<ul class="posts">
  
  {%- assign category = page.category | default: page.title -%} 
  <!-- 여기서부터 -->
  {% assign posts = site.categories[category] %}
  {% for parent in site.plainwhite.navigation %}
    {% if parent.title == category and parent.children %}
      {% for child in parent.children %}
        {% if site.categories[child].size > 0 %}
          {% assign posts = posts | concat: site.categories[child] %}
        {% endif %}
      {% endfor %}
    {% endif %}
  {% endfor %}
  <!-- 여기까지 -->

  <p class="post-counter" > {{ category }} ({{ posts | size }}) </p>
  {%- for post in posts -%}

{% endraw %}
```
중간에 Liquid로 새로 추가(주석처리된 부분)하고, post-counter와 for loop 부분을 수정하였다.

새로 추가된 부분은, 다음과 같다.

* Line 1 : 우선, site.categories[category] 로, **"현재 카테고리"**에 해당하는 post를 posts 라는 변수에 넣는다.
* Line 2-3 : 그리고, _config.yml의 navigation 을 돌면서, **"현재 카테고리"**에 해당하는 title을 찾고, Children 이라는 Key 까지 갖고 있다면, 
* Line 4-6 : Children의 요소들을 돌면서, "하위 카테고리"의 posts를 기존 posts에 추가한다.

즉, 정리하면,

* 현재 카테고리가 상위(부모) 카테고리이고, 하위(자식)이 없음 -> Line 3 이 False이므로, 상위 Posts 만 가져옴
* 현재 카테고리가 상위(부모) 카테고리이고, 하위(자식)이 있음 -> Line 3 이 True이므로, 상위 Posts에 하위 Posts를 더함.
* 현재 카테고리가 하위 카테고리라면 -> Line 3이 False(첫번째 조건에 의해)이므로, 하위 Posts만 가져옴.

그리고, 기존에 현재 카테고리에 한해서만 가져오던 것들을, 위 조건에 의해 선택된 posts 모두를 가져오게 된다.

![after](/assets/images/2020-08-30-01-36-57_2020-08-27-githublog_4.md.png){: .alignCenter}
아직 하위 카테고리가 하나씩 밖에 없지만, 우측 상단의 Algorithm이 상위 카테고리를 클릭했음을 보여준다.
{: .caption}

# 3. 마치며
: 결과는 사소한데, 과정은 사소하지 않았다. 괜히 했나 싶기도 하고.. ㅠ  
그리고, Markdown 테마와 글꼴이 약간 마음에 들지 않아, 추후에 시간이 나면 이것도 수정해봐야겠다.