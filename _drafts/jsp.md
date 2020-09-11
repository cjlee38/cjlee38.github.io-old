
기존에는 완전 static한 데이터만 제공함. 즉, 10개만 만들어놓고 줄 수 있음. 근데,
나는 전체목록이 아니라 일부만 갖고오고 싶다면? 회원명단만 주면 되는데 스태프명단까지 줄수는 없으니까..

코드를 실행해서 문서를 만들어서, 그거를 전달을 해줘야 함. 즉 가공이 필요한데, 이거를 was라고 함
was(web application server)

즉, web server(통신용), was(web application server)(코드 실행용), web application(코드) 의 세 개가 가장 기본 뼈대.

그리고, client가 del, post, get 등의 여러 작업을 할 수 있으므로, 이 조각들을 모아놓은게? servlet.