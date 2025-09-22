from django.urls import path
from . import views   # 같은 앱(chatbot)의 views.py에 있는 함수들을 불러옴

urlpatterns = [
    # -------------------- 인증 관련 --------------------
    path("login/", views.login_view, name="login"),      
    # 👉 /login/ 경로로 들어오면 views.login_view 실행
    #    - GET 요청 → 로그인 폼 렌더링
    #    - POST 요청 → 입력한 username/password 확인 후 로그인 처리
    #    - 성공 시 chatbot 페이지로 redirect

    path("logout/", views.logout_view, name="logout"),   
    # 👉 /logout/ 경로 → views.logout_view 실행
    #    - 현재 로그인한 사용자를 로그아웃 시키고 다시 chatbot 메인으로 redirect

    path("register/", views.register_view, name="register"),  
    # 👉 /register/ 경로 → 회원가입 처리
    #    - GET 요청 → 회원가입 폼 렌더링
    #    - POST 요청 → 새 User 생성 후 로그인 페이지로 redirect
    
    path('check-username/', views.check_username, name='check_username'),

    path("find-account/", views.find_account_view, name="find_account"), 


    # -------------------- 챗봇 메인 --------------------
    path("", views.chatbot_view, name="chatbot"),            
    # 👉 사이트 루트("/") 접근 시 → views.chatbot_view 실행
    #    - GET 요청 → 챗봇 메인화면 로딩 (현재 세션 불러오기 + 사이드바 목록 표시)
    #    - POST 요청 → 사용자가 메시지를 보냈을 때 LLM 호출 후 응답 반환

    path("chatbot/", views.chatbot_view, name="chatbot2"), 
    # 👉 /chatbot/ 경로도 동일하게 chatbot_view 실행
    #    - 즉, "/"와 "/chatbot/" 두 주소 모두 챗봇 메인으로 진입 가능하게 설정


    # -------------------- 세션 관리 --------------------
    path("delete_session/<int:session_id>/", views.delete_session, name="delete_session"), 
    # 👉 /delete_session/3/ → views.delete_session 실행
    #    - 특정 세션 ID(session_id)를 받아서 DB에서 삭제
    #    - 성공 시 {"success": True} JSON 반환

    path("load_session/<int:session_id>/", views.load_session_messages, name="load_session"),
    # 👉 /load_session/3/ → views.load_session_messages 실행  ⏰ 2025-09-07 추가
    #    - 특정 세션 ID(session_id)의 모든 ChatMessage 불러옴
    #    - JSON 형태로 메시지 목록 반환
    #    - 프론트엔드에서는 사이드바 클릭 시 이 API를 호출해서 채팅창 갱신

    path("start_new_session/", views.start_new_session, name="start_new_session"),
    # 👉 /start_new_session/ → views.start_new_session 실행  ⏰ 2025-01-09 추가
    #    - 새로운 대화 세션을 생성하는 API
    #    - POST 요청으로 새 ChatSession 생성
    #    - JSON 형태로 새 세션 ID 반환


    # -------------------- 여행 관련 --------------------
    path("map/", views.map_view, name="map"),  
    # 👉 /map/ → views.map_view 실행
    #    - DB에 저장된 Place 목록 불러오기
    #    - pybo/map.html 템플릿 렌더링
    #    - 카카오 지도 API 키도 함께 전달됨

    path("save_schedule/", views.save_schedule, name="save_schedule"),
    # 👉 /save_schedule/ (POST 전용)
    #    - 챗봇이 생성한 일정 데이터를 DB(Schedule 모델)에 저장
    #    - 세션(ChatSession)과 연결
    #    - 성공 시 {"success": True, "session_id": ...} JSON 반환

    path("get_schedule/<int:sid>/", views.get_schedule, name="get_schedule"),
    # 👉 /get_schedule/5/ → views.get_schedule 실행
    #    - 특정 ID(sid)의 일정(Schedule)을 불러옴
    #    - JSON으로 반환 (프론트에서 일정 불러오기 기능에 사용)

    # -------------------- 세션 → 일정 매핑 --------------------
    path("find_schedule_by_session/<int:session_id>/", views.find_schedule_by_session, name="find_schedule_by_session"),

    # -------------------- 경로 API --------------------
    path("api/get-route/", views.get_route, name="get_route"),
    # 👉 /api/get-route/ → views.get_route 실행
    #    - 카카오 지도 길찾기 API 연동
    #    - 출발지, 도착지, 경유지 정보를 받아서 경로 검색
    #    - JSON 형태로 경로 정보 반환

    # -------------------- 다중 삭제 API --------------------
    path("api/bulk-delete-sessions/", views.bulk_delete_sessions, name="bulk_delete_sessions"),
    # 👉 /api/bulk-delete-sessions/ → views.bulk_delete_sessions 실행
    #    - 여러 세션을 한 번에 삭제하는 API
    #    - POST 요청으로 session_ids 배열을 받아서 처리
    #    - JSON 형태로 삭제 결과 반환
]
