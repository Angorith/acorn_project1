import streamlit as st
from pages import project1_1 as p1_1
from pages import project1_2 as p1_2
from pages import project1_3 as p1_3
from pages import project2 as p2
from pages import intro

class MultiPage:
    def __init__(self):
        self.pages = []
    def add_page(self, title, func): 
        
        self.pages.append({
          
                "title": title, 
                "function": func
            })

    def run(self):
        
        page = st.sidebar.selectbox(
            'SELECT BOX', 
            self.pages, 
            format_func=lambda page: page['title']
        )
        page['function']()
        
app = MultiPage()

app.add_page("메인페이지", intro.app)
app.add_page("과제 1-1 프로젝트 환경 구축", p1_1.app)
app.add_page("과제 1-2 DATAFLOW", p1_2.app)
app.add_page("과제 1-3 API, 웹 스크래핑", p1_3.app)
app.add_page("과제 2 시계열 그래프", p2.app)


app.run()


