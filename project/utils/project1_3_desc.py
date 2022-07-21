import streamlit as st
from utils import project1_3_desc_web as p3dw
from utils import project1_3_desc_json as p3dj

def desc():
    st.markdown('### API, 웹 스크래핑(크롤링), 공공데이터를 이용하여 자료 수집\n')
    st.markdown('url = https://www.sta1.com/shops?gndr=F&shopType=S')
    st.markdown('##### 1. 웹 스크래핑을 활용한 자료(데이터 수집)')
    st.text('='*100)
    
    
    st.dataframe(p3dw.df, width = 700)


    st.text('='*100)
    
    st.markdown('##### 2. 경기도 명소의 정보가 담긴 json 파일을 활용해 지도에 Mapping하기')
    st.markdown('url = https://data.gg.go.kr/portal/data/service/selectServicePage.do?infId=BM4IHHEFJAEFIJMM6SC031171354&infSeq=1&loc=')
    #지도 표시  
    p3dj.desc2()


