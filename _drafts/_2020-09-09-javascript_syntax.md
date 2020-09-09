---
layout: post
title:  "# Javascript 기초 문법"
date:   2020-09-09 03:56:00 +0900
categories: [Javascript]
tags: 
---

(타 프로그래밍 언어를 모른다면, 이해하기 어려울 수 있음)

# 1. Variable

## A. Declartion
: javascript의 변수는 데이터 타입을 따로 지정하지 않음.  

대신, let, const, var 의 세 가지 키워드로 변수를 선언 할 수 있음.

1. var
2. let
3. const

### 1) var
- 변수를 선언. 추가로 동시에 값을 초기화
- 변수를 다시 선언할 수 있음
> ```javascript
> var num = 1;
> var num = 2; // 에러 발생하지 않음.
> ```
- 대부분, var 대신 let을 사용하는 것이 권장됨.

--- 

> Note. var 변수는 function 스코프 내에서 위치에 관계 없이 선언할 수 있다.(정의는 불가능)
> 이를 호이스팅이라고 한다. 
> ```javascript
> console.log(_var);
> var _var;
> --> Undefined // var가 아닌 let, const 라면 ReferenceError 발생
> ```
> 

---


### 2) let
- 블록 범위 지역변수를 선언. 추가로 동시에 값을 초기화
- 선언 이후, 재선언 불가능.

> ```javascript
> let num = 1;
> let num = 2; // SyntaxError 발생
> ```

### 3) const
- 블록 범위 읽기 전용 상수를 선언. 선언 시 반드시 정의해줘야 한다.
- 선언할 때, 반드시 정의(초기화)가 병행되어야 함.
- const로 선언한 객체, 혹은 배열의 속성 및 내용은 보호되지 않음.

> ```javascript
> const some_object = { 'some_key' : 'some_value' };
> some_object.some_key = 'other_value'; // applied
> some_object = "something_else" // TypeError 발생
> ```


### 4) none
- (a = 1) 처럼 선언되지 않은 전역 변수를 만들 수도 있지만, 사용하지 않는 것을 권장.


## B. Array, Object

### 1) Array
- 여러개의 변수를 담을 수 있는 자료 구조.
- 쉼표를 두 번 작성할 경우, undefined
> ```javascript
> var language = ['python', , 'javascript']
> console.log(language[1]) // undefined
> ```
- 변수의 Data Type에 구애받지 않고 삽입 가능.

### 2) Object
- key-value로 이루어진 자료 구조.
- key는 변수, value는 리터럴이 됨.
- 온점으로 객체 속성에 접근 가능
> ```javascript
> const myInfo = {
>   age : 25,
>   name : "cjlee",
>   gender : "male"
> }
> console.log(myInfo.age) // 25
> ```

# 2. 함수
- 함수는 **"선언"** 될 수도 있고, **"표현"** 될 수도 있음.
> ```javascript
> function statement() { // 선언
>     console.log("this is statement");
> }
> 
> var expression = function () { // 표현
>     console.log("this is expression");
> }
> 
> statement();
> expression(); 
> ```

---

> Note. statement는 Hoisting 가능, expression은 불가능.

---





- Reference
: [MDN web docs](https://developer.mozilla.org/ko/docs/Web/JavaScript)
: [javascript functions](https://medium.com/@pks2974/javascript%EC%99%80-function-%ED%95%A8%EC%88%981-a35281b56f8a)