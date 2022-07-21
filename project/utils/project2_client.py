from utils import project2_module as p2m
import streamlit as st
def desc():
    #파일 불러오기
    paths = 'C:/Users/Administrator/project/timeseries/data/'
    #파일 저장소 생성
    file_list_dict = p2m.get_filelist(paths)
    data = p2m.get_data(file_list_dict['MI'])
    
    
    m_data = {}
    for key, value in data.items():
        df = p2m.missing_check(value, 'T')
        df = p2m.physical_check(df)
        df = p2m.step_check1(df)
        df = p2m.persistence_check(df)
        key_f = p2m.keep_data(df)
        m_data[key_f] = df

    st.markdown("##### 1. 2022-06-01~06-08 시계열 그래프")
    st.dataframe(m_data[key_f])
    st.text(" *결측자료를 나타낸 그래프* ")

    #시간자료
    hourly = p2m.resample_hour(m_data)
    p2m.keep_data(hourly, 'OBS_108_AirTemp_hourly_data')
    
    
    diurnal = p2m.resample_day(hourly)
    p2m.keep_data(diurnal, 'OBS_108_AirTemp_diurnal_data')

    h_data = p2m.get_data(file_list_dict['TIM'])

    for i in h_data:
        df = h_data[i]
        df = p2m.resample_day(df,'temp')
        p2m.keep_data(df, 'OBS_108_AIRTemp_2021_data')
        
    df_month = p2m.resample_month(df)
    st.dataframe(df_month)
    
    
    #일자료
    
    fig=p2m.timeseries_plot(df)
    st.pyplot(fig)
