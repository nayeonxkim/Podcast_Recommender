1. 웹 크롤링 과정 학습 : AWS 람다
- 크롤링할 사이트 : 팟방 
  
  - 팟캐스트는 애플의 어플리케이션. 웹사이트 따로 존재 X 애플 사이트에서 확인할 수 있지만 크롤링하기 어려워보임
  
  - 팟방도 충분히 컨텐츠가 많아서 가능할 듯. 
  
  - robot.txt 등의 문제도 없는 것 확인함.

- 논문 리뷰 : 방향성잡기

- 나동빈 AWS Lambda 강의

- aws API Gateway : API 생성을 쉽게 할 수 있도록 하는 서비스 보통 람다와 같이 사용하는 듯

-> 이번주에 해볼랬는데 aws가 가입안시켜줘서 실패

---

2. 크롤링한 데이터를 모아둘 곳.
- 온프레미스 X, 클라우드 기반의 데이터레이크 구축
  
  - 데이터가 크지 않고 나혼자하기 때문에 온프레미스가 효율적이지만 공부를 위해 클라우드 선택

- 데이터레이크 구성 서비스엔 어떤 것이 있는지 알아보아야함
  
  - 데이터브릭스 관심 생겨서 찾아볼 예정 : 아파치 스파크 실행환경을 제공하는 클라우드 플랫
3. 데이터 스트리밍 처리
- 팟캐스트 데이터는 생각보다 얻을 게 없었다.

- 사용자 데이터를 제대로 가져오거나 더 붙여볼만한 소스를 찾아봐야겠다.