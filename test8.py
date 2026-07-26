import streamlit as st
import random
from datetime import date, timedelta

# 페이지 설정
st.set_page_config(layout="wide", page_title="GDX 교육 수강신청")

# CSS 스타일 정의
st.markdown("""
    <style>
    .main .block-container {
        padding-top: 1rem; /* 상단 여백 최소화 */
        padding-bottom: 1rem;
        max-width: 98%; /* 좌우 여백 최소화 */
    }
    .main-container {
        display: flex;
        flex-direction: column;
        height: 98vh; /* 화면 전체 높이 사용 */
        justify-content: flex-start;
        align-items: center;
        overflow-y: hidden; /* 스크롤 방지 */
    }
    .upper-container {
        height: 48%; /* 상단 영역 50% 정도 비율 */
        width: 100%;
        display: grid;
        grid-template-columns: repeat(3, 1fr); /* 3열 */
        grid-template-rows: repeat(4, 1fr); /* 4행 */
        gap: 8px; /* 박스 간 여백 */
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 12px;
        overflow-y: hidden; /* 스크롤 방지 */
    }
    .lower-container {
        height: 48%; /* 하단 영역 50% 정도 비율 */
        width: 100%;
        margin-top: 2%; /* 상단과 여백 */
        display: grid;
        grid-template-columns: repeat(5, 1fr); /* 5열 */
        gap: 15px; /* 박스 간 여백 */
    }
    .badge-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 8px 15px;
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.05);
    }
    .badge-item span {
        font-weight: bold;
        font-size: 1.2rem;
    }
    .svg-badges {
        display: flex;
        gap: 4px;
    }
    /* 하단 버튼 스타일 */
    div.stButton > button {
        width: 100%;
        height: 100%;
        min-height: 80px; /* 박스와 텍스트를 큼직하게 */
        font-size: 20px !important;
        font-weight: bold !important;
        border: 2px solid #005A9C;
        border-radius: 15px;
        background-color: #ffffff;
        color: #005A9C;
        transition: all 0.3s;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        background-color: #005A9C;
        color: #ffffff;
    }
    /* 두 번째 화면 중앙 정렬 및 디자인 */
    .center-content {
        text-align: center;
        margin-top: 15vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .center-content h2 {
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    .center-content p {
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# 사용자 및 데이터 정의
users = ["박지성", "이영표", "류현진", "손흥민", "박찬호"]
if 'current_user' not in st.session_state:
    st.session_state.current_user = random.choice(users) # 매 접속 시 랜덤 사용자 설정
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_module' not in st.session_state:
    st.session_state.selected_module = ''

# 모듈 및 데이터
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

# 배지 레벨 및 색상 매핑
# level_map: "없음" ~ "골드크라운"을 0~5로 매핑
level_map = {"없음": 0, "노랑": 1, "녹색": 2, "검정": 3, "실버크라운": 4, "골드크라운": 5}
# colors: 각 단계별 색상 (노랑, 녹색, 검정, 실버, 골드)
# colors 리스트의 크기는 5개입니다.
colors = ["#FFD700", "#32CD32", "#000000", "#C0C0C0", "#FFD700"]

# 화면 이동 함수
def go_home():
    st.session_state.page = 'home'
    st.session_state.selected_module = ''
    st.rerun()

def go_module(module):
    st.session_state.page = 'module'
    st.session_state.selected_module = module
    st.rerun()

# --- 배지 SVG 생성 함수 (에러 수정 및 디자인 개선) ---
def get_svg_badge(level):
    svgs = ""
    # 항상 5개의 배지 자리를 만듭니다.
    for i in range(5):
        # [에러 수정]: colors 리스트의 인덱스 접근을 안전하게 하도록 수정.
        # colors 리스트의 크기가 5이므로, i는 0-4의 값을 가집니다.
        # colors[i]는 에러가 발생하지 않으며, 만약 unseen typo 등으로 i가 5가 되더라도
        # colors[5 % 5] = colors[0]으로 순환하여 IndexError를 방지합니다.
        color_idx = i % len(colors)
        
        # 누적형 획득 방식 구현
        # 현재 배지 단계(i)가 사용자의 배지 상태 레벨(level)보다 작으면 채워진 배지
        if i < level:
            # 채워진 배지
            fill_color = colors[color_idx]
            stroke_color = colors[color_idx]
            dash = ""
        else:
            # 획득하지 못한 배지 (점선)
            fill_color = "none"
            stroke_color = "#999"
            dash = 'stroke-dasharray="2,2"'
            
        # [디자인 개선]: 디자인 요구사항(누적된 형태)을 더 명확하게 시각화하기 위해 SVG 내부 구조 개선.
        # 기존의 점선 형태를 개선하여 내부가 채워지는 디자인으로 구성했습니다.
        svgs += f'''
        <svg width="28" height="28" viewBox="0 0 100 100" style="margin-left: 2px;">
            # 큰 삼각형 외곽선 및 채우기
            <path d="M50,10 L90,80 L10,80 Z" fill="{fill_color}" stroke="{stroke_color}" stroke-width="4" {dash}/>
            # 내부를 '누적된 단계'로 표현하기 위해 흰색 삼각형을 추가하여 구멍을 뚫는 효과.
            # 획득한 배지일 경우에만 흰색 구멍을 만듭니다.
            <path d="M50,30 L75,70 L25,70 Z" fill="white" stroke="none" />
            # 가장 안쪽의 채워진 삼각형 (색상)
            <path d="M50,45 L60,65 L40,65 Z" fill="{fill_color}" stroke="none" />
        </svg>
        '''
    return svgs
# --------------------------------------------------

# --- 메인 앱 로직 ---
if st.session_state.page == 'home':
    # 첫 번째 화면: 메인 화면 (스크롤 방지)
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    
    # 현재 접속자 표시
    st.markdown(f"### 👤 현재 접속자: **{st.session_state.current_user}**")
    
    # 상단 컨테이너: 배지 현황 (3열 4행, 48% 비율)
    st.markdown("<div class='upper-container'>", unsafe_allow_html=True)
    user_idx = users.index(st.session_state.current_user)
    
    for mod in modules:
        status = data[mod][user_idx]
        lvl = level_map[status]
        # 개별 배지 아이템 HTML
        st.markdown(f"""
        <div class='badge-item'>
            <span>{mod}</span>
            <div class='svg-badges'>{get_svg_badge(lvl)}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True) # upper-container 닫기
    
    # 하단 컨테이너: 모듈 수강신청 박스 (5열, 48% 비율)
    # Streamlit은 버튼 이벤트를 개별적으로 처리하므로, HTML 대신 st.columns를 사용합니다.
    st.markdown("<div class='lower-container'>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i, mod in enumerate(modules):
        with cols[i % 5]:
            # 박스를 클릭하면 해당 모듈의 두 번째 화면으로 이동
            if st.button(mod, key=f"btn_{mod}", use_container_width=True):
                go_module(mod)
    st.markdown("</div>", unsafe_allow_html=True) # lower-container 닫기

    st.markdown("</div>", unsafe_allow_html=True) # main-container 닫기

elif st.session_state.page == 'module':
    # 두 번째 화면: 과정 선택 화면 (정중앙 위치)
    mod = st.session_state.selected_module
    
    # 컨텐츠 정중앙 배치를 위한 컬럼 구성 [1, 2, 1] 비율
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"<div class='center-content'><h2>{mod} 수강신청</h2></div>", unsafe_allow_html=True)
        st.write("")
        
        # --- 수강신청 단계를 처리하는 공통 함수들 ---
        
        def confirm_step(msg, yes_action, no_action=go_home, key_suffix=""):
            """예 vs 아니오 선택 단계를 처리하는 함수"""
            st.markdown(f"<p>{msg}</p>", unsafe_allow_html=True)
            # st.radio는 세로로 표시되므로 사용자 편의를 위해 버튼 형태의 선택지를 권장하나,
            # 요구사항에 따라 st.radio를 사용합니다.
            ans = st.radio("선택하세요", ["선택하세요", "예", "아니오"], key=f"conf_{key_suffix}")
            if ans == "예":
                yes_action()
            elif ans == "아니오":
                no_action()

        def select_type(online_action, offline_action, key_suffix=""):
            """온라인 vs 오프라인 선택 단계를 처리하는 함수"""
            st.markdown("<p>수강 방식을 선택하세요.</p>", unsafe_allow_html=True)
            ans = st.radio("수강 방식", ["선택하세요", "온라인", "오프라인"], key=f"type_{key_suffix}")
            if ans == "온라인":
                online_action()
            elif ans == "오프라인":
                offline_action()

        def select_instructor(instructors, key_suffix=""):
            """오프라인 강사 선택 단계를 처리하는 함수"""
            st.markdown("<p>강사를 선택하세요.</p>", unsafe_allow_html=True)
            inst = st.radio("강사", ["선택하세요"] + instructors, key=f"inst_{key_suffix}")
            if inst != "선택하세요":
                confirm_step("수강신청하시겠습니까?", 
                             lambda: st.success("수강신청이 완료되었습니다. 오프라인 교육은 강사의 안내에 따라 과제를 제출하여 평가에 응하시기 바랍니다."), 
                             key_suffix=f"inst_conf_{key_suffix}")

        def select_date(key_suffix=""):
            """오프라인 날짜 선택 단계를 처리하는 함수"""
            # 오늘부터 일주일 단위로 세 개의 일자 생성
            dates = [(date.today() + timedelta(days=i*7)).strftime("%Y-%m-%d") for i in range(1, 4)]
            st.markdown("<p>신청하고자 하는 날짜를 선택하세요.</p>", unsafe_allow_html=True)
            d = st.radio("날짜", ["선택하세요"] + dates, key=f"date_{key_suffix}")
            if d != "선택하세요":
                confirm_step("수강신청하시겠습니까?", 
                             lambda: st.success(f"[{d}] 수강신청이 완료되었습니다. 오프라인 교육은 강사의 안내에 따라 과제를 제출하여 평가에 응하시기 바랍니다."), 
                             key_suffix=f"date_conf_{key_suffix}")

        def online_course(msg, key_suffix=""):
            """온라인 수강신청 단계를 처리하는 함수"""
            confirm_step(f"{msg} 수강신청 하시겠습니까?", 
                         lambda: st.success("수강신청이 완료되었습니다. 온라인 교육은 강의 종료일로부터 한 달 이내에 두 번의 응시 기회가 부여됩니다."), 
                         key_suffix=f"onl_{key_suffix}")

        # --- 모듈별 수강신청 로직 ---
        if mod == "기술통계":
            # 온라인, 오프라인 중 하나를 선택하도록 해줘.
            select_type(
                lambda: online_course("기술통계 온라인 과정은 휴넷에서 제공되는 통계학 개론 과정의 Chapter 1,2,3 에 해당합니다.", "tech_stat"),
                lambda: select_instructor(["지덱수", "빤히", "기냥"], "tech_stat"),
                "tech_stat"
            )
            
        elif mod == "추론통계":
            # '선행학습으로 '기술통계' 과정이 요구됩니다. 수강신청 하시겠습니까?' 예, 아니오 선택
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

        # --- 하단 구분선 및 이전 화면 버튼 ---
        st.write("---")
        if st.button("⬅️ 이전 화면으로 돌아가기", use_container_width=True):
            go_home()
