import streamlit as st
import random
import datetime

st.set_page_config(layout="wide")

if "user" not in st.session_state:
    st.session_state.user = random.choice(["박지성", "이영표", "류현진", "손흥민", "박찬호"])
if "page" not in st.session_state:
    st.session_state.page = "main"
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None
if "step" not in st.session_state:
    st.session_state.step = 0

users = ["박지성", "이영표", "류현진", "손흥민", "박찬호"]
user_idx = users.index(st.session_state.user)

badge_levels = ["없음", "노랑", "녹색", "검정", "실버크라운", "골드크라운"]
badge_colors = {"노랑": "#FFD700", "녹색": "#008000", "검정": "#000000", "실버크라운": "#C0C0C0", "골드크라운": "#B8860B"}

badge_data = {
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

def get_badge_svg(level, current_level):
    if badge_levels.index(level) <= badge_levels.index(current_level) and level != "없음":
        color = badge_colors[level]
        stroke = "none"
        stroke_dasharray = "none"
    else:
        color = "transparent"
        stroke = "#ccc"
        stroke_dasharray = "2,2"

    return f'<svg width="32" height="32" viewBox="0 0 100 100" style="margin-right:6px;"><path d="M 5 15 L 95 15 L 50 95 Z M 50 35 L 75 25 L 50 70 L 25 25 Z" fill-rule="evenodd" fill="{color}" stroke="{stroke}" stroke-dasharray="{stroke_dasharray}" stroke-width="4" /></svg>'

def go_main():
    st.session_state.page = "main"
    st.session_state.selected_module = None
    st.session_state.step = 0
    st.rerun()

def go_module(module_name):
    st.session_state.page = "module"
    st.session_state.selected_module = module_name
    st.session_state.step = 1
    st.rerun()

if st.session_state.page == "main":
    st.markdown(f"<h2>접속자: {st.session_state.user}</h2>", unsafe_allow_html=True)
    
    st.markdown("### 🏆 배지 획득 현황")
    st.markdown("<hr style='margin:0; padding-bottom:15px;'/>", unsafe_allow_html=True)
    
    modules = list(badge_data.keys())
    
    cols = st.columns(3)
    for i, mod in enumerate(modules):
        user_level = badge_data[mod][user_idx]
        with cols[i % 3]:
            svgs = [get_badge_svg(lvl, user_level) for lvl in badge_levels[1:]]
            st.markdown(f"<div style='display:flex; align-items:center; margin-bottom:20px; font-size:28px;'><div style='width:280px; font-weight:bold;'>{mod}</div>{''.join(svgs)}</div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("### 📚 수강 신청 (과정 선택)")
    st.markdown("<hr style='margin:0; padding-bottom:20px;'/>", unsafe_allow_html=True)
    
    box_style = """
    <style>
    div[data-testid="stButton"] > button {
        height: 120px;
        background-color: #f0f2f6; border: 2px solid #d0d4dc; border-radius: 10px;
    }
    div[data-testid="stButton"] > button p {
        font-size: 28px !important; font-weight: bold !important;
        white-space: normal; word-break: keep-all; line-height: 1.3;
    }
    div[data-testid="stButton"] > button:hover {
        background-color: #e0e4eb; border-color: #0056b3;
    }
    div[data-testid="stButton"] > button:hover p {
        color: #0056b3;
    }
    </style>
    """
    st.markdown(box_style, unsafe_allow_html=True)
    
    for i in range(0, len(modules), 3):
        btn_cols = st.columns(3)
        for j in range(3):
            if i + j < len(modules):
                mod = modules[i+j]
                with btn_cols[j]:
                    if st.button(mod, key=f"btn_{mod}", use_container_width=True):
                        go_module(mod)

elif st.session_state.page == "module":
    mod = st.session_state.selected_module
    
    st.markdown("""
    <style>
    .center-container { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 60vh; text-align: center; }
    h1 { font-size: 50px !important; margin-bottom: 40px !important; text-align: center; }
    .big-text { font-size: 32px !important; font-weight: bold; margin-bottom: 50px; text-align: center; line-height: 1.5; }
    div[data-testid="stButton"] > button { height: 80px; margin-bottom: 15px; }
    div[data-testid="stButton"] > button p { font-size: 24px !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<h1>{mod}</h1>", unsafe_allow_html=True)
    st.markdown("<div class='center-container'>", unsafe_allow_html=True)
    
    pre_reqs = {
        "추론통계": "'기술통계'",
        "실험계획법": "'기술통계', '추론통계'",
        "통계적공정관리": "'기술통계', '추론통계'",
        "미니탭리터러시": "'기술통계', '추론통계', '통계적공정관리', '실험계획법'",
        "파이썬리터러시": "'기술통계', '추론통계'",
        "바이브코딩": "'파이썬리터러시'",
        "머신러닝 이론": "'기술통계', '추론통계', '파이썬리터러시'",
        "탐색적데이터분석": "'기술통계', '추론통계', '파이썬리터러시', '바이브코딩'",
        "머신러닝 모델링": "'기술통계', '추론통계', '파이썬리터러시', '바이브코딩', '머신러닝 이론', '탐색적데이터분석'",
        "AI Automation": "'바이브코딩'",
        "시각화": "'기술통계', '바이브코딩'"
    }
    
    if st.session_state.step == 1:
        if mod == "구조적문제해결방법론":
            st.markdown("<div class='big-text'>본 과정은 오프라인 교육만 제공되고 있습니다.<br>수강신청 하시겠습니까?</div>", unsafe_allow_html=True)
        else:
            if mod in pre_reqs:
                st.markdown(f"<div class='big-text'>선행학습으로 {pre_reqs[mod]} 과정이 요구됩니다.<br>수강신청 하시겠습니까?</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='big-text'>수강신청 하시겠습니까?</div>", unsafe_allow_html=True)
                
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("예", use_container_width=True): 
                st.session_state.step = 3 if mod == "구조적문제해결방법론" else 2
                st.rerun()
            if st.button("아니오", use_container_width=True): 
                go_main()

    elif st.session_state.step == 2:
        st.markdown("<div class='big-text'>교육 방식을 선택하세요</div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("온라인", use_container_width=True):
                st.session_state.mode = "online"
                st.session_state.step = 3
                st.rerun()
            if st.button("오프라인", use_container_width=True):
                st.session_state.mode = "offline"
                st.session_state.step = 3
                st.rerun()
            if st.button("이전", use_container_width=True): 
                st.session_state.step = 1
                st.rerun()
            
    elif st.session_state.step == 3:
        if mod == "구조적문제해결방법론":
            st.markdown("<div class='big-text'>강사를 선택하세요</div>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                for ins in ["김영태", "지덱수", "기냥"]:
                    if st.button(ins, use_container_width=True): 
                        st.session_state.step = 4
                        st.rerun()
                if st.button("이전", use_container_width=True): go_main()
                
        elif st.session_state.mode == "offline":
            if mod == "실험계획법":
                st.markdown("<div class='big-text'>실험계획법 오프라인 과정은 현재 개발중에 있습니다.<br>온라인 과정을 이용해 주세요.</div>", unsafe_allow_html=True)
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    if st.button("이전화면으로 돌아가기", use_container_width=True): 
                        st.session_state.step = 2
                        st.rerun()
            elif mod in ["파이썬리터러시", "바이브코딩", "머신러닝 이론", "탐색적데이터분석", "머신러닝 모델링"]:
                st.markdown(f"<div class='big-text'>{mod} 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다.<br>신청하고자 하는 날짜를 선택하세요.</div>", unsafe_allow_html=True)
                dates = [(datetime.date.today() + datetime.timedelta(days=i*7)).strftime("%Y-%m-%d") for i in range(1, 4)]
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    for d in dates:
                        if st.button(d, use_container_width=True):
                            st.session_state.selected_date = d
                            st.session_state.step = 4
                            st.rerun()
                    if st.button("이전", use_container_width=True): 
                        st.session_state.step = 2
                        st.rerun()
            else:
                st.markdown("<div class='big-text'>강사를 선택하세요</div>", unsafe_allow_html=True)
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    for ins in ["지덱수", "빤히", "기냥"]:
                        if st.button(ins, use_container_width=True): 
                            st.session_state.step = 4
                            st.rerun()
                    if st.button("이전", use_container_width=True): 
                        st.session_state.step = 2
                        st.rerun()
                    
        elif st.session_state.mode == "online":
            msgs = {
                "기술통계": "휴넷에서 제공되는 통계학 개론 과정의 Chapter 1, 2, 3",
                "추론통계": "휴넷에서 제공되는 통계학 개론 과정의 Chapter 4, 5, 6",
                "실험계획법": "휴넷에서 제공되는 실험계획법 과정의 Chapter 1~4",
                "통계적공정관리": "휴넷에서 제공되는 SPC 개론 과정의 Chapter 1, 2, 3",
                "미니탭리터러시": "휴넷에서 제공되는 미니탭 개론 과정의 Chapter 1~5",
                "파이썬리터러시": "휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 1~3",
                "바이브코딩": "휴넷에서 제공되는 바이브코딩 마스터 과정",
                "머신러닝 이론": "휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 1, 2, 3",
                "탐색적데이터분석": "휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 4, 5, 6",
                "머신러닝 모델링": "휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 7, 8, 9",
                "AI Automation": "휴넷에서 제공되는 Streamlit 마스터 과정",
                "시각화": "휴넷에서 제공되는 Tableau 마스터 과정"
            }
            st.markdown(f"<div class='big-text'>{mod} 온라인 과정은 {msgs[mod]} 에 해당합니다.<br><br>수강신청 하시겠습니까?</div>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("예", use_container_width=True): 
                    st.session_state.step = 5
                    st.rerun()
                if st.button("아니오", use_container_width=True): 
                    st.session_state.step = 2
                    st.rerun()

    elif st.session_state.step == 4:
        st.markdown("<div class='big-text'>수강신청하시겠습니까?</div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("예", use_container_width=True): 
                st.session_state.step = 6
                st.rerun()
            if st.button("아니오", use_container_width=True): 
                st.session_state.step = 3
                st.rerun()
            
    elif st.session_state.step == 5:
        st.markdown("<div class='big-text'>🎉 수강신청이 완료되었습니다.<br><br>온라인 교육은 강의 종료일로부터 한 달 이내에 두 번의 응시 기회가 부여됩니다.</div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("메인으로 돌아가기", use_container_width=True): go_main()
        
    elif st.session_state.step == 6:
        prefix = f"({st.session_state.selected_date})<br>" if 'selected_date' in st.session_state and mod in ["파이썬리터러시", "바이브코딩", "머신러닝 이론", "탐색적데이터분석", "머신러닝 모델링"] and st.session_state.mode == "offline" else ""
        st.markdown(f"<div class='big-text'>🎉 {prefix}수강신청이 완료되었습니다.<br><br>오프라인 교육은 강사의 안내에 따라 과제를 제출하여 평가에 응하시기 바랍니다.</div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("메인으로 돌아가기", use_container_width=True): go_main()

    st.markdown("</div>", unsafe_allow_html=True)
