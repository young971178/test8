import streamlit as st
import random
from datetime import date, timedelta

st.set_page_config(layout="wide", page_title="GDX 교육 수강신청")

st.markdown("""
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 95%;
    }
    .badge-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        height: 45vh;
        overflow-y: hidden;
    }
    .badge-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 5px 15px;
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
    }
    .badge-item span {
        font-weight: bold;
        font-size: 1.1rem;
    }
    .svg-badges {
        display: flex;
        gap: 5px;
    }
    .btn-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 15px;
        margin-top: 20px;
        height: 40vh;
    }
    div.stButton > button {
        width: 100%;
        height: 100%;
        min-height: 70px;
        font-size: 18px !important;
        font-weight: bold !important;
        border: 2px solid #005A9C;
        border-radius: 12px;
        background-color: #ffffff;
        color: #005A9C;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: #005A9C;
        color: #ffffff;
    }
    .center-content {
        text-align: center;
        margin-top: 10vh;
    }
    </style>
""", unsafe_allow_html=True)

users = ["박지성", "이영표", "류현진", "손흥민", "박찬호"]
if 'current_user' not in st.session_state:
    st.session_state.current_user = random.choice(users)
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_module' not in st.session_state:
    st.session_state.selected_module = ''

def go_home():
    st.session_state.page = 'home'
    st.session_state.selected_module = ''
    st.rerun()

def go_module(module):
    st.session_state.page = 'module'
    st.session_state.selected_module = module
    st.rerun()

modules = [
    "기술통계", "추론통계", "실험계획법", "통계적공정관리", "구조적문제해결방법론", 
    "미니탭리터러시", "파이썬리터러시", "바이브코딩", "머신러닝 이론", "탐색적데이터분석", 
    "머신러닝 모델링", "AI Automation", "시각화"
]

data = {
    "기술통계": ["녹색", "검정", "녹색", "검정", "골드크라운"],
    "추론통계": ["녹색", "녹색", "검정", "노랑", "실버크라운"],
    "실험계획법": ["녹색", "검정", "녹색", "노랑", "노랑"],
    "통계적공정관리": ["없음", "없음", "검정", "실버크라운", "골드크라운"],
    "구조적문제해결방법론": ["없음", "검정", "녹색", "검정", "검정"],
    "미니탭리터러시": ["검정", "노랑", "노랑", "노랑", "녹색"],
    "파이썬리터러시": ["골드크라운", "검정", "실버크라운", "녹색", "노랑"],
    "바이브코딩": ["노랑", "골드크라운", "실버크라운", "녹색", "노랑"],
    "머신러닝 이론": ["없음", "없음", "노랑", "노랑", "노랑"],
    "탐색적데이터분석": ["없음", "없음", "노랑", "녹색", "녹색"],
    "머신러닝 모델링": ["없음", "노랑", "노랑", "없음", "녹색"],
    "AI Automation": ["녹색", "검정", "녹색", "노랑", "없음"],
    "시각화": ["없음", "노랑", "검정", "골드크라운", "없음"]
}

level_map = {"없음": 0, "노랑": 1, "녹색": 2, "검정": 3, "실버크라운": 4, "골드크라운": 5}
colors = ["#FFD700", "#32CD32", "#000000", "#C0C0C0", "#FFD700"]

def get_svg_badge(level):
    svgs = ""
    for i in range(5):
        if i < level:
            fill_color = colors[i]
            stroke_color = colors[i]
            dash = ""
        else:
            fill_color = "none"
            stroke_color = "#999"
            dash = 'stroke-dasharray="2,2"'
            
        svgs += f'''
        <svg width="24" height="24" viewBox="0 0 100 100" style="margin-left: 2px;">
            <path d="M50,10 L90,80 L10,80 Z" fill="{fill_color}" stroke="{stroke_color}" stroke-width="4" {dash}/>
            <path d="M50,30 L75,70 L25,70 Z" fill="white" stroke="none" />
            <path d="M50,45 L60,65 L40,65 Z" fill="{fill_color}" stroke="none" />
        </svg>
        '''
    return svgs

if st.session_state.page == 'home':
    st.markdown(f"### 👤 현재 접속자: **{st.session_state.current_user}**")
    
    user_idx = users.index(st.session_state.current_user)
    
    badge_html = "<div class='badge-container'>"
    for mod in modules:
        status = data[mod][user_idx]
        lvl = level_map[status]
        badge_html += f"""
        <div class='badge-item'>
            <span>{mod}</span>
            <div class='svg-badges'>{get_svg_badge(lvl)}</div>
        </div>
        """
    badge_html += "</div>"
    st.markdown(badge_html, unsafe_allow_html=True)
    
    st.write("---")
    
    cols = st.columns(5)
    for i, mod in enumerate(modules):
        with cols[i % 5]:
            if st.button(mod, key=f"btn_{mod}", use_container_width=True):
                go_module(mod)

elif st.session_state.page == 'module':
    mod = st.session_state.selected_module
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"<div class='center-content'><h2>{mod} 수강신청</h2></div>", unsafe_allow_html=True)
        st.write("")
        
        def confirm_step(msg, yes_action, no_action=go_home, key_suffix=""):
            ans = st.radio(msg, ["선택하세요", "예", "아니오"], key=f"conf_{key_suffix}")
            if ans == "예":
                yes_action()
            elif ans == "아니오":
                no_action()

        def select_type(online_action, offline_action, key_suffix=""):
            ans = st.radio("수강 방식을 선택하세요.", ["선택하세요", "온라인", "오프라인"], key=f"type_{key_suffix}")
            if ans == "온라인":
                online_action()
            elif ans == "오프라인":
                offline_action()

        def select_instructor(instructors, key_suffix=""):
            inst = st.radio("강사를 선택하세요.", ["선택하세요"] + instructors, key=f"inst_{key_suffix}")
            if inst != "선택하세요":
                confirm_step("수강신청하시겠습니까?", 
                             lambda: st.success("수강신청이 완료되었습니다. 오프라인 교육은 강사의 안내에 따라 과제를 제출하여 평가에 응하시기 바랍니다."), 
                             key_suffix=f"inst_conf_{key_suffix}")

        def select_date(key_suffix=""):
            dates = [(date.today() + timedelta(days=i*7)).strftime("%Y-%m-%d") for i in range(1, 4)]
            d = st.radio("신청하고자 하는 날짜를 선택하세요.", ["선택하세요"] + dates, key=f"date_{key_suffix}")
            if d != "선택하세요":
                confirm_step("수강신청하시겠습니까?", 
                             lambda: st.success(f"[{d}] 수강신청이 완료되었습니다. 오프라인 교육은 강사의 안내에 따라 과제를 제출하여 평가에 응하시기 바랍니다."), 
                             key_suffix=f"date_conf_{key_suffix}")

        def online_course(msg, key_suffix=""):
            confirm_step(f"{msg} 수강신청 하시겠습니까?", 
                         lambda: st.success("수강신청이 완료되었습니다. 온라인 교육은 강의 종료일로부터 한 달 이내에 두 번의 응시 기회가 부여됩니다."), 
                         key_suffix=f"onl_{key_suffix}")

        if mod == "기술통계":
            select_type(
                lambda: online_course("기술통계 온라인 과정은 휴넷에서 제공되는 통계학 개론 과정의 Chapter 1,2,3 에 해당합니다.", "tech_stat"),
                lambda: select_instructor(["지덱수", "빤히", "기냥"], "tech_stat"),
                "tech_stat"
            )
            
        elif mod == "추론통계":
            confirm_step("선행학습으로 '기술통계' 과정이 요구됩니다. 수강신청 하시겠습니까?",
                         lambda: select_type(
                             lambda: online_course("추론통계 온라인 과정은 휴넷에서 제공되는 통계학 개론 과정의 Chapter 4,5,6 에 해당합니다.", "inf_stat"),
                             lambda: select_instructor(["지덱수", "빤히", "기냥"], "inf_stat"),
                             "inf_stat"
                         ), key_suffix="inf_stat_pre")
            
        elif mod == "실험계획법":
            confirm_step("선행학습으로 '기술통계' , '추론통계' 과정이 요구됩니다. 수강신청 하시겠습니까?",
                         lambda: select_type(
                             lambda: online_course("실험계획법 온라인 과정은 휴넷에서 제공되는 실험계획법 과정의 Chapter 1~4 에 해당합니다.", "doe"),
                             lambda: st.info("실험계획법 오프라인 과정은 현재 개발중에 있습니다. 온라인 과정을 이용해 주세요."),
                             "doe"
                         ), key_suffix="doe_pre")
            
        elif mod == "통계적공정관리":
            confirm_step("선행학습으로 '기술통계' , '추론통계' 과정이 요구됩니다. 수강신청 하시겠습니까?",
                         lambda: select_type(
                             lambda: online_course("통계적공정관리 온라인 과정은 휴넷에서 제공되는 SPC 개론 과정의 Chapter 1,2,3 에 해당합니다.", "spc"),
                             lambda: select_instructor(["지덱수", "빤히", "기냥"], "spc"),
                             "spc"
                         ), key_suffix="spc_pre")
            
        elif mod == "구조적문제해결방법론":
            confirm_step("본 과정은 오프라인 교육만 제공되고 있습니다. 수강신청 하시겠습니까?",
                         lambda: select_instructor(["김영태", "지덱수", "기냥"], "psm"),
                         key_suffix="psm_pre")
            
        elif mod == "미니탭리터러시":
            confirm_step("선행학습으로 '기술통계' , '추론통계' , '통계적공정관리', '실험계획법' 과정이 요구됩니다. 수강신청 하시겠습니까?",
                         lambda: select_type(
                             lambda: online_course("미니탭리터러시 온라인 과정은 휴넷에서 제공되는 미니탭 개론 과정의 Chapter 1~5 에 해당합니다.", "minitab"),
                             lambda: select_instructor(["지덱수", "빤히", "기냥"], "minitab"),
                             "minitab"
                         ), key_suffix="minitab_pre")
            
        elif mod == "파이썬리터러시":
            confirm_step("선행학습으로 '기술통계' , '추론통계' 과정이 요구됩니다. 수강신청 하시겠습니까?",
                         lambda: select_type(
                             lambda: online_course("파이썬리터러시 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 1~3 에 해당합니다.", "python"),
                             lambda: (st.info("파이썬리터러시 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다."), select_date("python")),
                             "python"
                         ), key_suffix="python_pre")
            
        elif mod == "바이브코딩":
            confirm_step("선행학습으로 '파이썬리터러시' 과정이 요구됩니다. 수강신청 하시겠습니까?",
                         lambda: select_type(
                             lambda: online_course("바이브코딩 온라인 과정은 휴넷에서 제공되는 바이브코딩 마스터 과정에 해당합니다.", "vibe"),
                             lambda: (st.info("바이브코딩 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다."), select_date("vibe")),
                             "vibe"
                         ), key_suffix="vibe_pre")
            
        elif mod == "머신러닝 이론":
            confirm_step("선행학습으로 '기술통계', '추론통계', '파이썬리터러시' 과정이 요구됩니다. 수강신청 하시겠습니까?",
                         lambda: select_type(
                             lambda: online_course("머신러닝 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 1,2,3에 해당합니다.", "ml_theory"),
                             lambda: (st.info("머신러닝 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다."), select_date("ml_theory")),
                             "ml_theory"
                         ), key_suffix="ml_theory_pre")
            
        elif mod == "탐색적데이터분석":
            confirm_step("선행학습으로 '기술통계', '추론통계', '파이썬리터러시', '바이브코딩' 과정이 요구됩니다. 수강신청 하시겠습니까?",
                         lambda: select_type(
                             lambda: online_course("탐색적데이터분석 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 4,5,6에 해당합니다.", "eda"),
                             lambda: (st.info("탐색적데이터분석 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다."), select_date("eda")),
                             "eda"
                         ), key_suffix="eda_pre")
            
        elif mod == "머신러닝 모델링":
            confirm_step("선행학습으로 '기술통계', '추론통계', '파이썬리터러시', '바이브코딩', '머신러닝 이론', '탐색적데이터분석' 과정이 요구됩니다. 수강신청 하시겠습니까?",
                         lambda: select_type(
                             lambda: online_course("머신러닝모델링 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 7,8,9에 해당합니다.", "ml_model"),
                             lambda: (st.info("머신러닝 모델링 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다."), select_date("ml_model")),
                             "ml_model"
                         ), key_suffix="ml_model_pre")
            
        elif mod == "AI Automation":
            confirm_step("선행학습으로 '바이브코딩' 과정이 요구됩니다. 수강신청 하시겠습니까?",
                         lambda: select_type(
                             lambda: online_course("AI Automation 온라인 과정은 휴넷에서 제공되는 Stramlit 마스터 과정에 해당합니다.", "ai_auto"),
                             lambda: select_instructor(["지덱수", "빤히", "기냥"], "ai_auto"),
                             "ai_auto"
                         ), key_suffix="ai_auto_pre")
            
        elif mod == "시각화":
            confirm_step("선행학습으로 '기술통계', '바이브코딩' 과정이 요구됩니다. 수강신청 하시겠습니까?",
                         lambda: select_type(
                             lambda: online_course("시각화 온라인 과정은 휴넷에서 제공되는 Tableau 마스터 과정에 해당합니다.", "vis"),
                             lambda: select_instructor(["지덱수", "빤히", "기냥"], "vis"),
                             "vis"
                         ), key_suffix="vis_pre")

        st.write("---")
        if st.button("⬅️ 이전 화면으로 돌아가기", use_container_width=True):
            go_home()
