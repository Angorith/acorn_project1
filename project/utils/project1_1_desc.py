import streamlit as st
from PIL import Image
def desc():
    st.subheader('프로젝트 환경 구축 절차 작성 제출')
    st.text('---구현 방법---')
    st.write('1. 가상환경 "pub" 생성하기 : powershell prompt실행 - "conda create -n pub python=3.9.7(3.7.4) ipython numpy matplotlib pandas scipy scikit-learn  tensorflow keras" ')

    image1 = Image.open('../project/images/1.PNG')
    st.image(image1, caption='-1-')

    st.write('1.1. 가상환경 구축여부 확인 : "conda env list" ')
    image1_1 = Image.open('../project/images/2.PNG')
    st.image(image1_1, caption='-1.1-')

    st.write('2. 가상환경 접속 활성화 : "conda activate pub" ')
    st.write('2.1. 가상환경 접속 비활성화 : "conda deactivate" ')
    
    image2 = Image.open('../project/images/3.PNG')
    st.image(image2, caption='-2-')

    st.write('3. pwd로 python 구동 가능한 디렉토리 확인 (*해당 디렉토리가 아닐경우, cd를 이용해 경로 설정)')
    st.write('4. 라이브러리 제대로된 설치가 되었는지 확인 ( import [sklearn,numpy,scipy,tensorflow, keras, pandas ])')
    st.write('4.1. 나머지 라이브러리 설치 (pip install[streamlit,seaborn,pandas_datareader,streamlit_folium,imageio-ffmpeg  ])')
    st.write('5. 설치된 목록(패키지)들을 ''requirements.txt'' 에 담기 : "pip freeze > requirements.txt" ')
    st.write('5.1. 목록 보기 : "more requirements.txt" ')
    image5 = Image.open('../project/images/5.PNG')
    st.image(image5, caption='-5-')

    st.write('6. 실행 : streamlit run 저장된 파일이름(app).py')
    
    image6 = Image.open('../project/images/6.PNG')
    
    st.image(image6, caption='-6-')
    

