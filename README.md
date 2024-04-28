# CodeEdChatbot
논문 "BERT를 활용한 순차적 답변 제시를 통한 코딩교육 챗봇 시스템"의 코드입니다.

## Abstract
인공지능 챗봇은 고객 대응이나 심심풀이와 같은 다양한 용도로 활용된다. 챗봇은 교육 분야에도 사용되고 있는데, 코딩 컨벤션이나 프로그래밍 언어의 서브루틴에 관한 질문에 답해주는 챗봇(또는 QA 시스템)을 확인할 수 있다. 본 논문은 코딩교육을 위한 챗봇을 구현하기 위해 다음을 제안한다: 1) 소셜미디어 웹사이트(유튜브) 크롤링 질의응답에 관한 데이터셋 생성 및 학습 2) BERT를 활용한 임베딩 성능 향상.

## How to run
1. Code > Download ZIP을 눌러 이 레포지토리를 다운받아 압축을 풉니다.
2. 모델 가중치를 [링크]에서 다운받아 압축을 풀어 본 폴더로 옯깁니다.
3. `python -m venv .venv`로 Python 가상환경을 생성합니다.
4. `.venv/Scripts/activate`로 가상환경을 활성화시킵니다.
5. `pip install transformers torch`로 패키지를 설치합니다.
6. `python main.py`로 `main.py`를 실행합니다.

## 가이드 영상
[개발환경 세팅]
[코드 실행]

---

## EN
Code for the paper "A Chatbot System for Coding Education through Sequential Answering with BERT".

## Abstract
AI chatbots are applied on various tasks such as customer service or idling. Chatbots are also used for educational purposes, such as a chatbot(or a QA system) that provides answers to questions about coding conventions or subroutines of programming languages. In this paper, we propose the following: 1) creation of a social media website(YouTube) crawling Q&A dataset and training 2) embedding performance enhancement using BERT.

## How to run
1. Click Code > Download ZIP to download this repository and unzip it.
2. Download model weights from [here], unzip it and add it to the current directory.
3. Run `python -m venv .venv` to create a Python virtual environment.
4. Run `.venv/Scripts/activate` to activate the virtual environment.
5. Run `pip install transformers torch` to install packages.
6. Run `python main.py` to execute `main.py`.
