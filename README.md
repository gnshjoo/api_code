# api_code

1. 관련 스펙
 - postgresql, python3, flask

2. 기능 정의

   POST */users/login*

   body
      ```json
        {
          "email": "",
          "password": ""
        }
      ```
   response
      ```json
        {
          "access_token": ""
        }
      ```
   
   POST */users/signup*
   
   body
   ```json
      {
         "phone": "",
         "password": "",
         "name": "",
         "nickname": "",
         "email": ""
      }
   ```
   response
      ```json
        {
          "message": "{email} user created"
        }
      ```
   
   GET */users/detail*
   Header
   ```json
      {
         "Authorization": ""
      }
   ```
   response
      ```json
        {
           "email": "",
           "name": "",
           "nickname": "",
           "phone": ""
        }
      ```
   
   PUT */users/rest*
   header
   ```json
      {
         "Authorization": ""
      }
   ```
   body
   ```json
      {
         "before_password": "",
         "new_password": ""
      }
   ```
   response
      ```json
        {
           "email": "",
           "name": "",
           "nickname": "",
           "phone": ""
        }
      ```
   
   GET */users/verify/[< types >]/[< code >]*
   types = (signup or reset)
   body
      ```json
        {
           "type": ""
        }
      ```
   response
   ```json
      {"message": "phone verified"}
   ```
   
   POST */users/auth*
   body
      ```json
        {
           "phone": "",
           "type": "[signup/reset]"
        }
      ```
   response
   ```json
      {"message": 567873}
   ```
   
   실행방법 : 프로젝트 안에서 docker compose up -d 라고 실행하시면 됩니다.
   구현범위 : 전화번호 인증은 보내는 것을 구현 하지 않아도 된다고 하여 /users/auth 로 대체 개발하였습니다.
    회원가입, 비밀번호 재설정 전 type : signup, reset을 넣고 코드 생성 후 verify/code 로 승인 이후 회원 가입, 비밀번호 재설정을
    하시면 됩니다.
    login 후 access_token 을 이용하여 session 관리 할 수 있도록 하였으며, 토큰 만료 시간은 1시간으로 하였습니다.
    식별 가능한 모든 정보를 원하셨지만 패스워드는 노출이 되면 안된다고 생각하여 detail에서 제외하였습니다.
    
    문서 작성을 swagger로 할려고 했으나 원할하지 못해 수기 작성하였습니다.