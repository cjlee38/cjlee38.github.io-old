

덧셈 과제

# 22

덧셈과제해설

<div>
    <form action="adder" method="post">
        <div>
            <label> x </label>
            <input name = "x" type="text"/>
        </div>
        <div>
            <label> y </label>
            <input name = "y" type="text"/>
        </div>
        <div>
            <input type="submit" value="click here to add"/>
        </div>
    </form>
</div>


        String x_ = request.getParameter("x");
        String y_ = request.getParameter("y");


        int x = 0;
        int y = 0;

        if (!x_.equals("")) x = Integer.parseInt(x_);
        if (!y_.equals("")) y = Integer.parseInt(y_);

        response.getWriter().printf("result is %d", x+y);


# 23 

덧셈말고 뺄셈도 해보자.

그럴려면 input 태그에다가 name을 붙여주자

<input type="submit" name="op" value="add"/>
<input type="submit" name="op" value="subtract"/>

그러면 이렇게됌. 그럼 op이 넘어가는게 아니고, op이 key, add가 value로 들어감
그러면 사용법은 존나 간단하지
String op = request.getParameter("op"); 이렇게쓰면됌


# 24

이번에는 사용자 입력값을 배열로 받아보자. 그럼 일단 보내는쪽에서는 num으로 통일해보자
e.g. 

<input type="text" name="num">
<input type="text" name="num">
<input type="text" name="num">
<input type="text" name="num">

이런식으로 여러개를 보낼 수 있음.

그럼 받는쪽에서는, getParameterValues()로 써야함.
그리고 쓰는건 이렇게

        String[] num_ = request.getParameterValues("num");
        int result = 0;
        for(int i = 0; i < num_.length; i++) {
            int num = Integer.parseInt(num_[i]);
            result += num;
        }


# 25 
**상태유지**

계산기를 생각해보자
만약 우리가 2+5-3 을 하고싶다면, 박스를 여러개를 만들어야할까?
박스를 두개로 한정한다면, 사용자입장에서 2+5를 해보고 7인걸 보고 7을넣고 3을 넣고 뺼셈하고
해야할까? 이건 좀 에바임. 

즉, 값을 받아서 이걸 저장을 해놔야함.

이를 위해선 세가지의 도구가 필요함
application
session
cookie

그리고, 때에 따라서는 hidden input과 querystring을 떄에 따라 쓸수도 있음. 이건 나중에

그래서, 일단 준비를 해보자
html은 다음과같이

<div>
    <form action="calc" method="post">
        <div>
            <label> input </label>
            <input name = "v" type="text"/>
        </div>
        <div>
            <input type="submit" name="op" value="+"/>
            <input type="submit" name="op" value="-"/>
            <input type="submit" name="op" value="="/>
        </div>
    </form>
</div>

calc.java는 아직 다음장에


# 26

우선 어플리케이션을 쓸거다.
일단은, 지금 당장은 1번일을 하면, 일을 하고 그대로 메모리에서 죽어버림
그래서 1번 -> 2번으로 넘겨줄수도없고, 1번에서 쓴 일을 다시 1번에서 쓸수없음

그래서, 서블릿을 쓸 때, 데이터를 이어갈수 있는 저장소가 필요한데 그게 servlet context
이 안에서는 서로 데이터를 공유할수있음. 이를 application 저장소라고 얘기하기도함.

ServletContext app = req.getServletContext(); 를 쓰면 컨텍스트를 가져옴
app.setAttribute(); 를 쓰면, map이라고 생각하면 됌.

이런식으로

       app.setAttribute("value", v);
       app.setAttribute("op", op);

그럼 전체코드는 이렇게됌

       ServletContext app = req.getServletContext();
       String v_ = req.getParameter("v");
       String op = req.getParameter("op");

       int v = 0;
       if(!v_.equals("")) v = Integer.parseInt(v_);

       if(op.equals("=")) {
           int x = (Integer) app.getAttribute("value");
           int y = v;
           String opt = (String) app.getAttribute("op");

           int result = 0;
           if (opt.equals("+")) result = x+y;
           else result = x-y;
           
           res.getWriter().printf("RESULT IS %d", result);
       }
       else {
           app.setAttribute("value", v);
           app.setAttribute("op", op);
           
       }


이렇게하면 단점
1. 입력하고, 덧셈버튼을누르면 흰화면이 나와버림. 왜? =가 아니니까. 그래서 뒤로가기를 다시 눌러야함
2. 값을 여러개를 받을려고한다면?? -> 이건 로직만 바꾸면 될려나.
3. 사용자마자 분리할수는 없을까??


# 27
이번에는 application 대신 세션으로 해보자. 그리고 차이점을 알아보자

세션객체는 request.getSession(); 을 통해 얻을수 있음
HttpSession session = req.getSession();

그리고, app 으로 사용하던애들을 다 session으로 바꿔버리자

똑같이 작동한다. 근데 뭔차이일까?

app은 전역변수 session은 지역변수
즉, 현재접속한사용자. 즉 사용자별로 달라진다.

어떻게 테스트해볼까?
기존 chrome 말고 edge나 파폭에서 해보자

서버를 restart하고,
chrome에서 5, + 까지 해보고
6 = 을 해보자. 그럼 안나옴
app은 됌

같은 크롬, 다른 탭에서는 어떨까?
같은 세션으로 인식한다.

왜냐면, 여러개의 탭은 프로세스가 아닌 스레드로 보고있기때문에 같은 data를 공유하고있음.

자 이제, 세션이 어떻게 사용자를 구분하는지 알아보자

# 28

개발자도구 - 네트워크 탭에서 document - request headers - cookies 를 보면 JSESSIONID 이거를 사용함.
즉 이걸 기준으로 구분함.

그럼 만약 누군가의 session ID를 복붙해서 사용하면, 좆됄수도있음.
이를 대비하기위해 마소같은 경우에는 주기적으로 session id를 바꿈

근데 이 세션공간이 계속 유지됄까 아님 정리할까? 정리함. 언제정리할까?
invalidate라는 애로 정리함.
뭘 기준으로할까? 시간을 기준으로.
즉, 내가 만약 60초라고 기준을 두면, 60초동안 세션요청이없으면 invalidate를 하면 날려버림.

# 29
이번에는 쿠키.
상태값을 클라이언트가 갖고있다가, 그걸 서블릿으로 보내줌

클라이언트에서 서버로 데이터를 보낼때는, 크게 세가지가 있음
TCP/IP 정보, 헤더 정보, 사용자 정보(데이터). 

서버에서 클라이언트로, addCookie()라는걸로 보낼수도있음.

쿠키 만들어서 추가하기 ->
Cookie cookie = new Cookie("c", some value) // key value
response.addCookie(cookie);

서버에서 쿠키 읽기
Cookie[] cookies = req.getCookies();
String _c = "";

if (cookies != null) 
    for (Cookie cookie : cookies) 
        if ("c".equals(cookie.getName))
            _c = cookie.getValue();

이걸 계산기에다 적용하면 setAttribute 부분에다가.
주의 : Cookie 객체를 만들때 key-value는 반드시 String이어야함.
그중에서도 url에 사용할 수 있는 cookie
but, json 같은걸 쓰면 다양한 형태의 객체로 쿠키를 저장할수있음.
어쨌든, 이런식으로 쿠키를 만들음

            Cookie valueCookie = new Cookie("value", String.valueOf(v));
            Cookie OpCookie = new Cookie("op", op);

이제, 이거를 클라이언트에게 보내야함

            resp.addCookie(valueCookie);
            resp.addCookie(opCookie);

이렇게 추가.


# 30
cookie path
cookie.setPath("/")라고 하면, 모든 path가 들어올때마다 갖고오라는 뜻
cookie.setPath("/notice") 라고 하면, notice가 포함될때마다 갖고오라는 뜻.

만약, /add를 경로로 지정하면, 처음에 내가 calc를 실행할때 cookie가 저장이 되긴 됐는데,
add로 가야 cookie를 보낼 수 있음.

# 31
maxAge

내가 만약 브라우저를 닫더라도, 쿠키파일은 데이터로 클라이언트의 디스크에 저장이 돼있음
cookie.setMaxAge(60 * 60) 으로 하면(초단위임), 쿠키를 보낸 시각으로부터, 하루동안은 이 쿠키가 살아있음. 브라우저가 닫히고, 클라이언트가 안들어와도.
-> "오늘 하루동안 보지 않기" 를 생각하면 될듯

# 32

application / session / cookie 정리
app
사용범위 : 전역범위에서 사용하는 저장공간.
생명주기 : WAS가 시작해서 종료할때까지
저장위치 : WAS 서버의 메모리

session
사용 범위 : 세션 범위(특정사용자만)에서 사용하는 저장공간
생명 주기 : 세션이 시작해서 종료할때까지
저장 위치 : WAS 서버의 메모리

cookie
사용 범위 : 웹브라우저 별 지정한 path 범주 공간
생명 주기 : browser에 전달한 시간부터 만료시간까지
저장위치 : 웹브라우저의 메모리 또는 파일.

기간이 길면, cookie에 저장하는게 좋다. was 메모리에 저장하면 존나 터져버리지않겠어?

# 33

redirect

백지화면을 받는 것을 (즉, 뒤로가기를 눌러야 했던것을) 원래페이지로 쉽게 넘겨보자

servlet에서 calc.html으로 넘겨주자
how? =이 아니고 + 나 -가 들어왔을때는
resp.sendRedirect("calc.html");를 통해서 넘겨주자.

# 34
동적인 페이지.
즉, 내가 3이라고 넣고 + 를 눌렀으면, 
앞에 3이라는 숫자가 보여야함.
지금은 그냥 입력할 수 있는 input 태그밖에 안보임.

즉, 완전히 계산기랑 비슷한 모양을 갖도록 해보자.

html을 서블릿으로 만드는것.
다음부터는 어떻게? jsp로.

html을 만들어놓고, 자바코드(이건 밑에) 중간에다가 html페이지를 붙여넣기하자.

PrintWriter out = resp.getWriter();
이거를 만들어놓고, 
out.write()로 태그를 line별로 감싸주자. 존나 비효율적임;;
시발 따라할랬는데 안할래

그리고 숫자를 나타내는 곳은 write가 아니라 printf를 쓰자.


# 35 36은 pass...


# 37

쿠키 삭제하는 법. operator중에 C라는 얘가 들어오면 clear를 해주자. 즉 쿠키를 지워주자.

how?
exp = "";
-> 즉, 
Cookie expCookie = new Cookie("exp", exp);
맨 뒤의 exp를 날림.

근데, 해보니까 뭔가 이상함. default가 0으로 setting헀으므로 0이 와야하는데,
빈문자열이 오니까 그냥 비어있는게 오는듯.

그래서 이걸 해결하려면,
expCookie.setMaxAge(0); 를 
if (operator != null && operator.equals("C")) 일 때 걸어주면 됌.

# 38
지금까지 우리는 service() 함수 안에다가 모든 logic을 작성했음
즉, get이 와도 service()가 실행됐고 post가 와도 실행됐음.

이걸 구분하는 방법 1) service()에서 구분 2) get/post에 특화된 method 활용
두개를 배워보자.

일단은, 
calculator.html을만들어서 이렇게 작성하자

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form action="calculator" method="get">
        <input type="submit" value="request"/>

    </form>
</body>
</html>

그리고 calculator.java로 와서,
if (req.getMethod.equals("GET")) // 대문자 주의
그리고 나머지 하면 됌.
근데 딱봐도 안좋아보이지.

default로 service()를 자동완성했을때 super.service(req,resp) 이거를 쓰는거임.
즉, 지금까지는 service()라는 상위를 override했는데,
그 하위를 구성하고있는 doGET과 doPOST를 따로따로 override하자.
그냥 아무것도 없이 super.service()만 살려두면, 405 에러가 남.

기본적으로, url이없으면 404에러인데 우리가 받는 에러는 405에러.

그래서 그 밑에 doGET을 override하면 됨

@Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("doPOST method called !");
    }

    like this.


만약 공통으로 처리하고 싶은게 없다? 그러면 그냥 service()를 없애버리면 됨.
어차피 override를 안했으면 super 가 진행될테니까