import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df1 = pd.read_csv('../project/files/0601.csv', encoding='cp949',skiprows=[0], names=['site','loc','time','temp'])
df2 = pd.read_csv('../project/files/0602.csv', encoding='cp949',skiprows=[0], names=['site','loc','time','temp'])
df3 = pd.read_csv('../project/files/0603.csv', encoding='cp949',skiprows=[0], names=['site','loc','time','temp'])
df4 = pd.read_csv('../project/files/0604.csv', encoding='cp949',skiprows=[0], names=['site','loc','time','temp'])
df5 = pd.read_csv('../project/files/0605.csv', encoding='cp949',skiprows=[0], names=['site','loc','time','temp'])
df6 = pd.read_csv('../project/files/0606.csv', encoding='cp949',skiprows=[0], names=['site','loc','time','temp'])
df7 = pd.read_csv('../project/files/0607.csv', encoding='cp949',skiprows=[0], names=['site','loc','time','temp'])

df = pd.concat([df1, df2, df3,df4, df5 , df6 ,df7])
df = df[['time','temp']]
df['time'] = pd.to_datetime(df['time'], infer_datetime_format=True)
df = df.set_index(['time'])
df = df.resample(rule='min').last()  


def missing_check(df, freqs):
    start = df.index[0]
    end = df.index[-1]
    timestamp = pd.date_range(start, end, freq = freqs)
    df = df.reindex(timestamp)
    return (df)

def physical_test(df):
    df[df >40] = np.nan
    df[df <-33] = np.nan
    return (df)


def step_check(df):
    temp = df.iloc[0,0]
    df['step_check'] = df.diff().fillna(-999999.9)
    df[df.step_check<-3.0] = np.nan
    df[df.step_check>3.0] = np.nan
    if temp:
        df.iloc[0,0] = temp 
    return (df)

def persistence_check(df):
    df['persis'] = df.step_check.abs()
    dummy_data = df.resample('H').sum()
    #다음날 00시를 drop -> counting 제외
    dummy_data.drop(dummy_data.index[-1], inplace=True)
    hour = dummy_data[dummy_data.persis<0.1].index.hour
    #print(hour)
    if len(hour):
        for i in hour:
            df[df.index.hour == i] = np.nan
    return (df)

df2 = pd.read_csv('../project/files/21_06_01_to_22_06_01.csv', encoding='cp949',skiprows=[0], names=['site','loc','time','temp'])
df2 = df2[['time','temp']]
df2['time'] = pd.to_datetime(df2['time'], infer_datetime_format=True)
df2 = df2.set_index(['time'])

day_mean = df2['temp'].resample('D').mean()
month_mean = df2['temp'].resample('M').mean()

def plt_seoul(day_mean,month_mean):
    fig = plt.figure(figsize = (16, 8))
    chart = fig.add_subplot(1,1,1)

    plt.title('2021-06-01 ~ 2022-06-01 Temperature change in Seoul',fontsize= 25)
    chart.plot(day_mean, color='blue' , label='daily Temp. change')
    chart.plot(month_mean, color='red' , label='monthly Temp. change')
    plt.xlabel('Date', fontsize= 23)
    plt.ylabel('Temp.', fontsize= 23)
    plt.legend(loc = 'best', fontsize=17)
    plt.show()

















