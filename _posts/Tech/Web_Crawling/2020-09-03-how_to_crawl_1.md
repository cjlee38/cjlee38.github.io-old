---
layout: post
title:  "# Step by Step, Web crawling 학습하기 (1) - OpenAPI 이용하기"
date:   2020-09-03 02:49:00 +0900
categories: web-crawling
tags: 
author: cjlee
cover: /assets/covers/web-crawling.jpg
---

# 0. 들어가며
: [이전 포스팅](https://cjlee38.github.io/web_crawling/how_to_crawl_1) 에서, 웹 크롤링이 무엇인지 간략하게나마 이해했다. 이전 포스팅을 읽어보지 않았다면, 꼭 읽고오자.

그런데, 내가 수집하고자 하는 사이트의 robots.txt를 보면, 대부분이 제한되어 있다는 것을 알 수 있다.

그러나, 이에 대응하여 합법적으로 데이터를 수집할 수 있는 방법이 있으니, 그것이 바로 OpenAPI다.

[위키피디아](https://ko.wikipedia.org/wiki/%EC%98%A4%ED%94%88_API) 에서는, 다음과 같이 설명하고 있다.

<center> 오픈 API(Open Application Programming Interface, Open API, 공개 API)는 누구나 사용할 수 있도록 공개된 API를 말하며, 개발자에게 사유 응용 소프트웨어나 웹 서비스에 프로그래밍적인 권한을 제공한다. </center>

즉, 해당 웹사이트의 운영자가, "우리 웹사이트에서, 이러한 사용은 허락합니다." 하면서 서비스를 제공해주는 것이다.

**따라서, 이번 포스팅에서 작성하는 내용은 정확히는 Crawling이 아니며, Crawling을 하기 이전에, 데이터를 수집하는 과정에서, 합법적으로, 정당하게 이용할 수 있는 방법을 안내한다.**

# 1. 준비.
: 우선, 국내 최다 이용자를 보유한 웹사이트인 네이버에서 OpenAPI를 이용해보자. 그 중에서도, 뉴스 검색을 해볼 것이다.

이에 앞서, 다음과 같은 준비물이 필요하다.
1. Python
2. Python의 requests, json 모듈
3. 네이버 OpenAPI Application

본 포스팅에서, 파이썬의 설치와 requests module의 준비는 따로 다루지 않는다.Python 및 모듈 설치 방법은 너무 간단하므로, 본 포스팅을 읽는 사람들은 최소한 Python이 설치되어 있고, pip의 사용법을 알고, 따라서 requests,json 모듈까지 설치되어 있다고 가정한다. 

### - 네이버 OpenAPI Application 등록

[네이버 Developers](https://developers.naver.com/main/) 사이트에 들어가서, 상단의 Application - 애플리케이션 등록 버튼을 클릭하자.

![homepage](/assets/images/2020-09-03-02-59-21_2020-09-03-crawling_1.md.png){: .alignCenter}
가운데에 보이는 "애플리케이션 등록" 클릭
{: .caption}

로그인을 진행하고, 이용 약관에 동의한 뒤, 휴대폰인증까지 해주자.

---
![enrollment](/assets/images/2020-09-03-03-07-22_2020-09-03-crawling_1.md.png){: .alignCenter}

하고나면, 화면과 같이 Application에 대한 정보를 입력할 수 있다.
{: .caption}

Application 이름은 본인이 원하는대로 적고, 사용 API는 "검색"을, 뒤이어 나타나는 환경은 "WEB 설정"을, 그리고 도메인이 있다면 도메인을 적고, 없다면 "http://localhost"를 입력하자.

![enrollment2](/assets/images/2020-09-03-03-10-35_2020-09-03-crawling_1.md.png){: .alignCenter}
다 입력하고나면 이런식으로 된다.
{: .caption}

등록을 하고나면, **본인의 Client ID와 Client Secret**을 확인할 수 있다. 이를 어딘가에 메모해두자. 여기까지 하면, 준비는 끝났다.

# 2. 이용해보기
: Application 등록을 하고, 상단의 Docuemnts에서, 서비스 API 하위에 있는 "검색"을 클릭하면 OpenAPI 사용법이 나타나있다.

어느정도 프로그래밍에 익숙하다면, 본인이 사용하는 언어를 클릭해보면 쉽게 이해할 수 있지만, 아마 대부분의 독자들이 아직 익숙치 않은 상태일 것이므로, 이를 자세하게 설명해보고자 한다.

먼저, 파이썬에서 다음과 같이 두 개의 모듈을 import 해주자.

```python
import requests
import json
```

---
> Note. 2번의 API 기본 정보를 보면, xml과 json의 두가지 방식으로 요청을 할 수 있다는 것을 알 수 있다. XML을 파싱하기 위한 라이브러리가 따로 존재하지만, json을 이용하면 python의 dictionary로 쉽게 다룰 수 있으므로, 본 포스팅에서는 json을 사용하도록 한다.

---

다음으로, 네이버에 요청을 해주자. 공식 문서에서는, 다음과 같이 4개의 parameter를 받을 수 있다고 설명한다.

![parameter](/assets/images/2020-09-03-03-22-05_2020-09-03-crawling_1.md.png){: .alignCenter}

즉, 내가 OpenAPI에 요청을 하는데, 다음과 같은 인자를 넘김으로써, 결과 값을 튜닝할 수 있다는 이야기가 된다.

따라서, 우선은 다음과 같이 작성해보자.

```python

headers = {
    "X-Naver-Client-Id" : "본인이 발급받은 Client ID",
    "X-Naver-Client-Secret" : "본인이 발급받은 Client Secret"
}

params = {
    "query" : "검색하고자 하는 단어"
}

response = requests.get("https://openapi.naver.com/v1/search/blog.json", headers = headers, params = params)

```

requests 모듈은 python을 이용해 http 요청을 실행할 수 있는 라이브러리다.  
즉, 쉽게 생각하면, "해당 인터넷 창을 연다" 라고 보면 된다.

headers와 params, http의 headers에 내 Client ID와 Client Secret을 담아서,  
params에는 내가 만든 params라는 dictionary를 담아서 인자로 넘겨주겠다는 의미가 된다.

그 결과를 response로 받아서, status_code를 확인해보면 다음과 같이 200이 나타날 것이다.
```python
print(response.status_code)

200
```

http의 응답코드가 200이라면, 정상적으로 처리되었음을 의미한다. 혹여나 다른 코드가 나타났다면, [여기](https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C)에서 본인의 코드와 비교해서 확인해보도록 하자.

우리가 requests.get을 통해서 얻은 결과물은, .text를 통해서 확인할 수 있다.

```python
print(requests.text)

"결과물"
```

이는 **아직 json으로 해석되지 않은 단순 문자열**이며, 이를 json으로 해석해줘야한다.

```python
result = json.loads(response.text)
```

해당 result를 확인해보면, dictionary 형태로 결과물이 나타나 있는 것을 확인할 수 있으며, 적당한 key-value로 접근해서 본인이 원하는대로 정리하면 된다.

---
> Note. params에는, Document에 있는 다른 params를 추가해줘도 된다. 가령, "검색 결과 출력 건수" 를 기본값의 10개가 아닌 100개로 보고 싶다면, 다음과 같이 params를 추가해주면 된다.
>
```python
params = {
    "query" : "검색하고자 하는 단어"
    "display" : 100
}
```

---

# 3. 마치며
: 위와 같은 OpenAPI 사용법은 네이버에만 한정된 것이 아니며, OpenAPI를 제공하는 모든 서비스는 위와 거의 비슷한 흐름을 갖고 있다. 본인만이 사용할 수 있는 Key를 가지며, params 혹은 headers에 Key를 넣고, 여러 검색 옵션을 대입함으로써 원하는 결과를 제공 받을 수 있다.

사실, 너무 단순한 내용이라, 이 글을 이해할 수 있다면, 아마 공식문서만 보고도 이해할 수 있을 것이라 생각된다. 그러나, 최대한 초심자의 입장에서 설명하고자 했으니, 도움이 되었으면 좋겠다. 끝