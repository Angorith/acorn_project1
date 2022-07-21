# -*- coding: utf-8 -*-
import streamlit as st
from utils import project2_desc as p2d

def desc():
    
    st.markdown("##### 시계열 데이터를 활용하여  그래프와 표로 나타내기")
    st.markdown("###### link :https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36 ")
    st.markdown("###### 1. 2022-06-01~ 06-07 기온 QC검사표")
    st.text('pandas를 활용해 표로 나타냄')
    #기본 dataframe
    st.dataframe(p2d.df)
    st.text('- 기본 Dataframe(결측처리 전) -')
    #물리한계검사
    result_physical_test=p2d.physical_test(p2d.df)
    st.dataframe(result_physical_test)
    st.text('- 물리 한계 검사 후 -')
    #단계검사
    result_step_check = p2d.step_check(p2d.df)
    st.dataframe(result_step_check)
    st.text('- 단계 검사 후 -')
    #지속성검사
    result_persistence_check=p2d.persistence_check(p2d.df)
    st.dataframe(result_persistence_check)
    st.text('- 지속성 검사 후 -')
    
    st.text('='*100)
    st.markdown("###### 2. 2021-06-01 ~ 2022-06-01 기온 그래프 &표")
    #1년 일/월평균 그래프 & 표
    st.dataframe(p2d.df2)
    st.text('- 기본 Dataframe -')
    st.dataframe(p2d.day_mean)
    st.text('- 일(하루) 평균기온 -')
    
    st.dataframe(p2d.month_mean)
    st.text('- 월 평균기온 -')
    fig=p2d.plt_seoul(p2d.day_mean,p2d.month_mean)
    st.pyplot(fig)