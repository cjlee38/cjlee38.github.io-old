
기존에는 완전 static한 데이터만 제공함. 즉, 10개만 만들어놓고 줄 수 있음. 근데,
나는 전체목록이 아니라 일부만 갖고오고 싶다면? 회원명단만 주면 되는데 스태프명단까지 줄수는 없으니까..

코드를 실행해서 문서를 만들어서, 그거를 전달을 해줘야 함. 즉 가공이 필요한데, 이거를 was라고 함
was(web application server)

즉, web server(통신용), was(web application server)(코드 실행용), web application(코드) 의 세 개가 가장 기본 뼈대.

그리고, client가 del, post, get 등의 여러 작업을 할 수 있으므로, 이 조각들을 모아놓은게? servlet.


#

Tomcat binary버전 다운로드(서비스는 불가)
환경변수 jdk 설정
포트번호 충돌 확인

/bin/startup.bat -> localhost:8080

# 5

홈디렉토리(/webapps/ROOT)에 웹문서를 저장하고, 브라우저를 통해서 달라고 해보자.

demo.txt파일을 하나 만들어서 홈디렉토리에 저장하고 localhost:8080/demo.txt에 저장하자. -> 잘됌. Good

localhost:8080으로 봤던 화면은 index.jsp 를 통해서 구성된것임. 즉 localhost:8080/index.jsp를 하면 잘 됌
없는놈을 요청하면 404 error

# 6
context: 일종의 디렉토리 같은 것. admin/dealer/community .. 이런애들  
근데, 물리적으로 디렉토리를 나눠버리면, 팀 별로 일하기가 좀 껄끄럽겠지?  
그 대신에, 새로운 Root에서 출발해서, 새로운 프로젝트를 만듬.  
기존의 프로젝트는 linking만 함.  

돌아가는건 마치 하나인것처럼.

뭐 예를들어 일단 디렉토리를 하나 만들었다고
/it/computer.txt 만들면 잘 나옴. 근데 엘레강트하지않음.

이걸 옮겨보자. /webapps/it 이렇게 옮겨보자(딴데로 옮겨도됌 상관X)
그러면 이상태로는 당연히 안나옴. /conf로 가면 server.xml 있음.
맨밑에 <Host name="localhost"  appBase="webapps"
            unpackWARs="true" autoDeploy="true"> 
            
            밑에 
            <context path="itt" docBase="C:\TOOLS\apache-tomcat-9.0.37\webapps\it" privileged="true"/>


            
            이런식으로 추가해줌

            itt는 테스트해보는용도로 임의로 바꾼것. 근데 적용안되네 그냥 /it/computer.txt로 해야함

근데 이렇게 xml을 추가하는건 좋지않음.왜? 서버를 껐다켜야 적용되니까. "일단은 이렇게 하자"


# 7

서블릿이라는걸 이제 만들어보자. 이게 무슨의미일까? 서버 어플리케이션을 만드는것.
서블릿은 기능별로 코드가 나눠져있고, 선택적으로 실행될 수 있게 만들어져있음.

즉, GET /notice/list ... GET /notice/reg ... 이런 애들이 들어오면 거기에 맞는애들만 Load됨  
따라서 필요한 것 하나씩 만들면 된다. 어떻게? 우리가 지금까지 만든거는 main()을 실행했는데,
이제부터는 service()라고하는 이름의 함수를 통해서 프로그램을 만들면됌.

그럼 , 클래스랑 함수이름을 어떻게 만들어야할까? 
이름은 알바 아니고, extends HttpServlet 이라는 걸 붙여줘야함. 
클래스는 아무거나 ㄱㅊ 대신 extend했으니 service()함수는 고정.
클래스 이름을 nana라고 해보자.

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class nana extends HttpServlet {
    public void service(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        sysout something
    }
}

그러면 이제부터 애를 나나서블릿이라고 부름.(nana.java)로 저장

얘를 내가 원하는 폴더에 넣고

javac -cp C:\TOOLS\apache-tomcat-9.0.37\lib\servlet-api.jar nana.java 하면 실행됌. 

# 8
클래스파일은 그럼 어떻게 실행시킬것인가? web-inf 라는 폴더내에 classes 내에 둬야함.
만약 class를 만들때 다른데서도 또 갖고왔다면 또 내부에 더 넣어야함
예를들어 com.google이면 그 내부에도 com폴더 google폴더를 넣어야함.

얘는 좀 특수한 존재임. 클라이언트쪽에서 볼수도없고, 요청할수도 없게 되어있음
e.g. localhost:8080/web-inf/classes/nana.class 는 안됌

그럼 어떻게 해야하느냐? 즉 WAS, 톰캣이 URL와 매핑된 servlet 코드를 찾아서 실행시켜줘야함

이걸 세팅하려면 web.xml 이거 어디서 본거같지 ㅋㅋ 
여기다가 세팅을 해줘야함.

  <servlet>
    <servlet-name>na</servlet-name>
    <servlet-class>nana</servlet-class>
  </servlet>

  <servlet-mapping>
    <servlet-name>na</servlet-name>
    <url-pattern>/hello</url-pattern>
  </servlet-mapping>

했더니 어떻게되? 클라이언트는 백지인데, 서버에서 sysout이 튀어나옴.
# 여기까지 2편 ------------------------



# 9
이제 클라 web에서 hello world 할 수 있도록 해보자.

service() 함수는 두개의 인자를 받음. request, response 객체
근데 void인데 어떻게?? 신기하네;

OutputStream os = response.getOutputStream();
PrintStream out = new PrintStream(os, true);

이걸로 아웃풋 스트림을 만듬. 근데 버퍼가 8kb라서 쌓여야보내니까,
이걸 flush를 해줘야함 어떻게?

out.println("hello servlet!");

근데 여기서, 잠깐. 하나고칠때마다 존나귀찮다. IDE를쓰자
딱 여기까지만 기존에 하던대로 하자.

# 10

인텔리제이 - jsp project with intellij.md

# 11 & # 12

src/main/java 안에 java 파일 만들고

@WebServlet("/hi")
public class nana extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        PrintWriter out = resp.getWriter();
        out.println("Hello fucking Intellij. its from annotation");
    }
}

위 어노테이션은 web.xml에서 metadata-complete를 false
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0"
        metadata-complete="false">

이렇게해줘야 쓸수있음. 서블릿 3.0부터 가능함 2 버전대에서는 안됌


# 13

service() 함수 안에 for문으로 println()을 찍어보자. 크롬에서는 줄바꿈이되는데  
엣지에서는 줄바꿈이 안됌. 

왜이럴까? 

서버가 보냈을 때, "웹문서"로 받는게 정상이다. 즉 줄바꿈이 안되어야 정상이다.
소스를 보면 줄바꿈이 되어있는데, 보는데에서는 안됌. 왜? 이건 HTML이니까. 그래서 <br> 태그를 넣어줘야 함.

근데 이렇게 하니까 크롬에서는 <br> 태그를 그냥 그대로 출력해버림. 이건 브라우저의 차이 자의적인 해석을 했냐안했냐 차이임.
그래서, 문서 형식을 알려줘야함. 엣지는 html로 해석했고, 크롬은 text로 해석했으니까 이런 결과가 나오는거임.
게다가, 한글도 깨짐 이거는 14강에서 알아보자.

# 14

테스트해보자.

for(int i = 0; i < 100; i++) {
  out.println((i+1)+ " : 안녕하세요 This is servlet<br/>");
}

보니까 한글이 ????? 이렇게나옴. 깨졌음.

왜냐면, 웹서버의 인코딩은 ISO-8859-1 임. 얘는 1바이트 단위임.
근데 한글 인코딩은 2바이트씩쓰니까 이걸 이해를 못함.

resp.setCharacterEncoding("UTF-8"); 를 넣어줘야 한다.

근데 해보니까 땜꿦 이렇게나옴. 시발. 이걸로 끝내면 안됀다

웹브라우저가 euc-kr 이라서 그런것같다. ? 이걸 클라이언트에서 세팅할수도있긴하다
보면, 익스플로러에서는 인코딩을 utf-8로 세팅할 수 있음. 

근데 클라이언트에서 세팅하는건 우리가 바라는게 아니잖아.
response header에다가 utf-8로 읽어야한다고 심어줘야함. 이렇게.

resp.setContentType("text/html; charset=UTF-8");


# 15 
출력을 해봤으니까, 이제는 입력을 받아보자. 입력을 어떻게 처리할것인가에 대해 배워보자.

사용자 요청이라고하면 기본적으로는 Get 요청.
예를 들면

http://localhost/hello?cnt=3

여기서 cnt=3이 쿼리스트링. 

이걸 어떻게하느냐?

int cnt = Integer.parseInt(req.getParameter("cnt"));

그리고 http://localhost:8080/hi?cnt=10 이렇게 걸면 잘 나옴. 근데 카운트가없으면 에러가나.
왜? 무조건 받는것으로 되어있었으니까. 이걸 핸들링해보자

# 16

case는
 /hi?cnt=3 일때 -> 3이 넘어옴
 /hi?cnt= 일때 -> ""이 넘어옴
 /hello? 일때 -> null이 넘어옴
 /hello 일때 -> null이 넘어옴

그럼 

        String cnt_ = req.getParameter("cnt");
        int cnt = 0;
        if (cnt_ != null) {
            cnt = Integer.parseInt(cnt_);
        }
        
이렇게 쓸수 있음. 근데 case2 일때가 문제가 되겠지. 그래서 조건문에 하나 더 추가
if (cnt_ != null && !cnt_.equals(""))

근데, 사람이 query string을 입력하지는 않으니까, index.html의 a 태그를 활용해보자

    <a href="/hi"> hello 100 times</a>
    <a href="/hi?cnt=5"> hello 5 times</a>

  를 index에 넣어보자

그러면 잘 됌

# 17

이번에는 한번 더 업그레이드 시켜보자. 안녕하세요를 사용자가 입력해서 넣은값으로 할 수 있도록 해보자.

바디 태그안에
    <div>
        <form action="hello">
            <div>
                <label> input your hello</label>
            </div>
            <input type="text" name="cnt" />
            <input type="submit" value="click here to out"/>
        </form>
    </div>

    를 넣어보자

    근데 주의할게 action이 내가 원하는 주소로 입력되어있어야함.
즉, localhost:8080/hi 로 보내고싶으면, action이 hi로 되어있어야함.

WEB-CONTENT(이클립스 기준. 인텔리제이는 webapp인듯) 밑에다가 hellow.html을 만들어보자.

그리고 body 안에 위 내용을 넣고, 서버를 실행시켜보자

localhost:8080/hellow.html 로 가면, 우리가 원하는 모습이 나온다(근데 뒤에 꼭 .html을 붙여야 한다 없애려면 어떻게해야할까? 이건 아직 안다룬다)

그리고 값을 넣고 submit을 하면 원하는대로 됨


# 18 
이번에는 POST를 받아보자. 예를들어, 회원가입을 한다고해보자

그러면 id=뭐시기,비밀번호는 뭐시기, 주소는 뭐시기 이렇게 쓰는건 좀 에바임

이거를 일정한 양식을 통해서 전해주자.

이번에는 reg.html을 역시 webapp안에 만들어보자(hellow를 복사해서)

그리고, 똑같이 

<div>
    <form action="hi">
        <div>
            <label> input your title </label>
            <input name = "title" type="text"/>
        </div>
        <div>
            <label> input your content </label>
            <textarea name="content"></textarea>
        </div>
        <div>
            <input type="submit" value="click here to out"/>
        </div>
    </form>
</div>


를 넣고,

새로 java file을 만들어서

        resp.setCharacterEncoding("UTF-8");
        resp.setContentType("text/html; charset=UTF-8");

        PrintWriter out = resp.getWriter();

        String title = req.getParameter("title");
        String content = req.getParameter("content");

        out.println("title : " + title);
        out.println("content : " + content);

        를 넣자


그럼 이렇게하면, 얘는 기존의 get이랑 다를바가 없게됌. parameter로 들어가는것을 볼 수 있음

http://localhost:8080/notice-reg?title=this+is+title&content=this+is+fucking+content

그러므로, form aciton="notice-reg" method="post"를 넣어줘야함

이렇게하면, network 탭으로 가서 보면, 
일단 헤더메소드가 PSOT인걸 볼 수 있고,
밑에 form-data에 title과 content를 볼 수 있음.

또, 회원가입도 생각해보자. 회원가입에서 get을 보내면 url에서 보이니까 좆되지않겟어?ㅋㅋ

자 여기서 문제, title과 content에 한글을 입력해보자. 깨져서나온다.

# 19

생각해보자, 이건 어디의 문제일까? 내가봤을땐 클라이언트에서 utf-8로 보내지 않아서 그런거같음.
출력할때는 잘 되는걸 봤으니까, 

근데 알고보니까 서버문제네 ㅋㅋ 서버가 출력할때 utf8로 세팅을 했는데, 읽어들일때는 여전히 ISO-8859-1인가봄. 맞네.

왜냐면, 우리가 아까 쓴 코드는 resp.setCharacterEncoding("UTF-8"); 얘는 resp에 세팅을 한거니까. request에도 setting을 해줘야지 

이게 귀찮으면? 톰캣에서 server.xml에서 connector 태그에다가 URIEncoding="UTF-8"로 세팅해주면됌
근데 일반적으로 톰캣서버는 잘 안건드린다. 왜? 여러개의 서비스를 돌릴수가 잇으니까. A 서비스가 utf-8이라고해서, B서비스도 utf-8이어야할 이유가 없는이상..

req.setCharacterEncoding("UTF-8");

# 20

서블릿 필터를 활용해보자. 얘도아마 인코딩과 관련된 내용인듯?

톰캣이 서블릿컨테이너라는 소프트웨어를 실행함. 이게 메모리에 존재할텐데, 그 공간이 컨테이너. was는 서블릿을 실행시켜서 컨테이너에 넣어놓고, response를 줌. 그리고 사용되지않으면 메모리에서 비워짐

지금까지는 서블릿만 만들었는데, 서블릿말고 또 만들수있는게 바로 서블릿필터

지금까지 우리가 setCharacterEncoding을 써왔는데, 이걸 계~~속 쓰는건 존나 귀찮음. 
그렇다고해서, 톰캣자체를 바꾸면? 모든 서비스에 적용되니까 안됌.
즉, 특정 서블릿컨테이너에다 세팅을 해주고 싶다.

말 그대로 수문장 역할. 접근권한이있는지 없는지도 책임지게 할 수 있음. 인증/권한을 줄것인가 말것인가 이런것도.

또한, 나가는것에도 세팅할수있음. 사전/사후 코드를 건드릴 수 있다.

새로운 패키지, 그리고 클래스를 만들어보자

package com.example.filter;

import javax.servlet.*;
import java.io.IOException;

public class CharacterEncodingFilter implements Filter {
    @Override
    public void doFilter(ServletRequest servletRequest,
                         ServletResponse servletResponse,
                         FilterChain filterChain)
            throws IOException, ServletException {
        System.out.println("filter");
    }
}

그리고, 얘도 매핑을 시켜줘야하는데, 마찬가지로 두가지 방법이 있다.
1번은 web.xml에가서

<filter>
<filter-name>myFilter</filter-name>
<filter-class>com.example.filter.CharacterEncodingFilter</filter-class>
</filter>

<filter-mapping>
<filter-name>myFilter</filter-name>
<url-pattern>/*</url-pattern> <!-- 모든 주소에 대해서 필터링하겠다 -->
</filter-mapping>

그리고 이렇게 실행하면, 아무것도안나옴.
왜그럴까? 필터가 nana로 넘겨주지 않아서 그런거같다.
즉 chain이 넘겨줄것인가 말것인가를 결정해준다.

filterChain.doFilter(servletRequest, servletResponse);

즉, 이 코드를 기점으로 위쪽으로하면 사전처리, 밑쪽으로하면 사후처리인것.
따라서, 인코딩세팅을하려면

servletRequest.setCharacterEncoding("UTF-8");
servletResponse.setCharacterEncoding("UTF-8");
filterChain.doFilter(servletRequest, servletResponse);

이렇게.

@@근데 setContentType은 ..? 얘도 가능하네 ㅋㅋ

# 21 

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