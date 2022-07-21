from streamlit_folium import folium_static
import folium
import json

def desc2():
    
    #json 파일 열기
    with open('../project/files/gyeonggi_place.json','r',encoding='UTF-8') as f:
        datas = json.load(f)
    #print(datas)
        
    # 마커 위치
    maps = folium.Map(location=[37.5602, 126.982], zoom_start=7, tiles= 'cartodbpositron')

    # 마커 추가
    for i in datas:
        try:
            name = i['NM_SM_NM']
            lat = float(i['REFINE_WGS84_LAT'])
            lon = float(i['REFINE_WGS84_LOGT'])
        except Exception as e:
            pass
        folium.Marker([lat, lon], popup=str(name)).add_to(maps)
     
    folium_static(maps)




