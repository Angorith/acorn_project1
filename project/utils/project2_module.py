import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import glob


def get_filelist(paths):
    file_list = glob.glob(paths+'*')
    hourly_data = []
    every_minute_data = []
    file_list_dict = {}
    for i in file_list:
        if 'TIM' in i:
            hourly_data.append(i)
        else:
            every_minute_data.append(i)
    file_list_dict['TIM'] = hourly_data
    file_list_dict['MI'] = every_minute_data
    return file_list_dict

def get_data(file_list, index_column=2, parse_date=[2]):
    file_list.sort()
    data={}
    for fn in file_list:
        df = pd.read_csv(fn, index_col = index_column,\
            parse_dates = parse_date, encoding='cp949',\
            skiprows=[0], \
            names = ['site', 'name','time','temp'])
        df.drop(['site','name'], axis=1, inplace=True)
        data[fn] = df
    return (data)


paths = '../timeseries/data/'

file_list_dict = get_filelist(paths)

#print(file_list_dict)

data = get_data(file_list_dict['MI'])

#print(data)


#인덱스 비는 시간 없게 재설정
def missing_check(df, freqs):
    start = df.index[0]
    end = df.index[-1]
    timestamp = pd.date_range(start, end, freq = freqs)
    df = df.reindex(timestamp)
    return (df)
#물리 한계 검사
def physical_check(df):
    df[df<-33.0] = np.nan
    df[df>40] = np.nan
    return (df)

#단계 검사
def step_check1(df):
    temp = df.iloc[0,0]
    df['step_check'] = df.diff().fillna(-999999.9)
    df[df.step_check<-3.0] = np.nan
    df[df.step_check>3.0] = np.nan
    if temp:
        df.iloc[0,0] = temp  
    return (df)

#지속성 검사
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
def keep_data(df, file_name='bird'):
    start = dt.datetime.strftime(df.index[0], '%Y%m%d%H%M%S')
    end = dt.datetime.strftime(df.index[-1],'%Y%m%d%H%M%S' )
    if file_name =='bird':
        file_name = 'OBS_108_AirTemp' + start+'_'+end+'.csv'
    df.to_csv(file_name)
    return (file_name)




def resample_hour(m_data):
	for key, df in m_data.items():
		df = df.dropna().resample('H').agg({'temp':['size', 'mean']})
		df = df.droplevel(level=0, axis=1)
		df.loc[df['size']<48, 'mean'] = np.nan
		df.dropna(inplace=True)
		df = missing_check(df, 'H')
		if 'result' in locals():
			result = pd.concat([result, df])
			continue
		result=df
	return result

def resample_day(df, col_name='mean'):
	df = df.dropna().resample('D').agg({col_name:['size', 'mean']})
	df = df.droplevel(level=0, axis=1)
	df.loc[df['size']<20, 'mean'] = np.nan
	return (df)

def resample_month(df, col_name='mean'):
	df = df.dropna().resample('M').agg({col_name:['size', 'mean']})
	df = df.droplevel(level=0, axis=1)
	df.loc[df['size']<24, 'mean'] = np.nan
	return (df)

def timeseries_plot(df):
	df.iloc[[11, 20, 21], :] = np.nan
	df.columns=['sizes', 'means']	
	data = df.loc[:'2022-06-01', 'means']
	methods = ['linear', 'quadratic', 'cubic']
	df_gapfilled = pd.DataFrame({m: data.interpolate(method=m) for m in methods})
	df_gapfilled.plot()
	#data.plot()
	plt.grid()
	plt.savefig('gf.png')
	data = data.round(2)
	df_gapfilled = df_gapfilled.round(2)
	data.to_csv('pre_gap_filling.csv')
	df_gapfilled.to_csv('gap_filled.csv')



