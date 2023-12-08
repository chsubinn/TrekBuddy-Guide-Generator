# TrekBuddy Guide Text Generator


### 프로젝트 소개
<a href=https://github.com/Yang-ga-hyeon/TrekBuddy>한국어 텍스트 모델 기반 여행 가이드 어플리케이션 TrekBuddy</a>의 가이드 텍스트 생성 모델입니다.

## ⏲개발 기간
* 2023.08.01 ~ 2023.11.10

### 🧑‍🤝‍🧑멤버
- 조수빈: Project Leader, ML Data Collection & Preprocess, App Develop, Database Management, 가이드 페이지, 검색 페이지, 스크랩 페이지
- 양가현: Main App Developer, Database Management, 로그인 페이지, 회원가입 페이지, 가이드 페이지, 가이드 상세 페이지
- 김윤선: Data Preprocess & Model Finetuning, App Develop, Database Management, 가이드 페이지, 개인정보 수정 페이지, 리뷰 페이지, 로그 페이지

### 💻개발 환경
- **Pretrained-model** : 한국어 Bart 모델 오픈 소스 (https://github.com/SKT-AI/KoBART) <img src="https://img.shields.io/badge/google colab-F9AB00?style=for-the-badge&logo=google colab&logoColor=white">
- **Training data** : AI hub 요약문 및 레포트 생성 데이터 (https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=582) <img width="100" height="20" src="https://github.com/Yang-ga-hyeon/TrekBuddy/assets/111068038/f4264824-e151-4a5b-94ea-c257113cf0b8">
- **Deep Learning Framework** :<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
- **TTS** : NAVER CLOVA <img width="50" height="50" src="https://github.com/Yang-ga-hyeon/TrekBuddy/assets/111068038/9af716e9-dd8c-411c-bffb-7ab7c03a04b3">
- **Database** : <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=Firebase&logoColor=white">

## 아키텍처
<img width="500" alt="아키텍처" src="https://github.com/Yang-ga-hyeon/TrekBuddy/assets/111068038/2f32b512-d40b-4d81-9c86-66f3da123b4d"> <br/>

<img width="500" alt="아키텍처-기술" src="https://github.com/Yang-ga-hyeon/TrekBuddy/assets/111068038/3fe28e87-8341-44bc-86b0-77526c2b430d">
  
  *Selenium이 아닌 Scrapy로 변경


## 설치방법 How to Build
- Directory 구조
<img width="300" height="400" src="https://github.com/chsubinn/TrekBuddy-Guide-Generator/assets/111068038/280821e7-6258-4488-a3bd-394ffcebff40">

- **Data folder**: train data, test data 넣기
- **checkpoint folder**: model binary
- **wandb folder**: Weights & Biases. 모델이 학습한 결과 저장 및 시각화, 하이퍼파라미터 저장, 시스템(GPU, CPU, memory 등) 모니터링
- **SKT KoBart open source files** 


## 사용방법 How to Test
**1) 개발 환경 setting**
  - GPU 사용
  - SKT KoBart open source download
  - 필요한 라이브러리 install

**2) Dataset 준비 & preprocess**
  - training data (his-cul, public 등)을 고르고 해당 데이터를 csv 파일로 형식 변환, 실행 전 ROOT 경로 및 csv 파일명 지정 필수 
     ```python
       python json2csv.py
     ```

  - csv 파일을 tsv 파일로 형식 변환
     ```python
       python csvTotsv.py
     ```
**3) Train(finetuning)**
  - dataset.py에서 input_ids와 label_ids를 본인의 데이터셋에 맞게 변경
    ```python
       input_ids = self.tokenizer.encode(instance['passage'])
       label_ids = self.tokenizer.encode(instance['utterance'])      
     ```
  - train.py에서 Model checkpoint 파라미터 변경
    ```python
       checkpoint_callback = ModelCheckpoint(monitor='val_loss',
                                          dirpath=args.checkpoint,
                                          filename='model_chp/{epoch:02d}-{val_loss:.3f}',
                                          verbose=True,
                                          save_last=False,                                         
                                          mode='min',
                                          save_top_k=3, 
                                          every_n_epochs=25)      
     ```
  - train.py에 best accurary model checkpoint 출력하는 부분 추가
    ```python
      #print best_checkpoint path
      best_checkpoint = checkpoint_callback.best_model_path
      print('\n best checkpoint path:', best_checkpoint)    
    ```
   - 학습하기
     ```python
      python train.py --gradient_clip_val 1.0 \
                      --max_epochs 100 \
                      --checkpoint checkpoint \
                      --accelerator gpu \
                      --num_gpus 1 \
                      --batch_size 4 \
                      --num_workers 4
     ```

**4) Evaluation**
  - output과 사람이 직접 요약한 문장을 비교하여 rouge score로 평가
     ```python
       python rouge.py
     ```
 - 학습한 모델로 측정한 결과

    |         |rouge-1|rouge-2|rouge-l|
    |---------|-------|-------|-------|
    |Precision|0.61702|0.42857|0.61702|
    |Recal    |0.58   |0.38182|0.58   |
    |F1       |0.59794|0.40385|0.59794|
    
     
**5) Test**
  - 학습한 model binary 추출
    ```python
       python get_model_binary.py --model_binary '추출할 checkpoint 경로를 입력하세요'
    ```
  - 학습한 model load하여 사용
    ```python
       import torch
        from transformers import PreTrainedTokenizerFast
        from transformers.models.bart import BartForConditionalGeneration
        
        # 모델 바이너리 파일 경로
        model_binary_path = 'model binary 경로를 입력하세요'
        
        # KoBART 모델 및 토크나이저 로드
        tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-base-v1')
        model = BartForConditionalGeneration.from_pretrained(model_binary_path)

        # 입력 텍스트
        input_text =  "요약할 텍스트를 입력하세요"
        # 입력 텍스트를 토큰화하여 인코딩
        input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=1024, truncation=True)
        
        # 모델을 사용하여 요약 생성
        summary_ids = model.generate(input_ids, max_length=150, min_length=15, length_penalty=2.0, num_beams=4, early_stopping=True)
        
        # 요약 결과 디코딩
        summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        # 요약 출력
        print("요약 텍스트:", summary_text)
    ```
    

## Data Description
-  AI hub 요약문 및 레포트 생성 데이터 사용
   (https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=97)
- Data Set 구조
  ```bash
  ├── Meta(Acqusition)
  │   ├── doc_id
  │   ├── doc_category
  │   ├── doc_type
  │   ├── doc_name
  │   ├── author
  │   ├── publisher
  │   ├── publisher_year
  │   └── doc_origin
  ├── Meta(Refine)
  │   ├── passage_id
  │   ├── passage // 원문
  │   └── passage_Cnt // 원문 글자 수
  └── Annotation
      ├── summary1 // 추출 요약
      ├── summary2
      ├── summary3
      └── summary_3_cnt // 생성 요약
  ``` 
- json2csv.py에서는 passage와 summary1, 2, 3를 모은 추출 요약 데이터를 모아 (passage, summary) 쌍으로 만들고 이를 csv로 변환합니다.
- csvTotsv.py에서는 json2csv.py파일에서 변환한 csv를 tsv로 변환하여 요약 모델의 데이터로 입력합니다.

