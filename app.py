import streamlit as st
import time

# 웹사이트 제목 및 레이아웃 설정
st.set_page_config(page_title="AI 방어벽 보안 게임", layout="centered")
st.title("2중 AI 방어벽 보안 게임")

SECRET_PASSWORD = "Wave2026"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 사용자 입력창 (목표 글자는 깔끔하게 가려진 상태)
user_input = st.text_input("공격자(사용자) 입력:", placeholder="비밀번호를 알아내기 위한 질문을 입력하세요...", key="input")

if st.button("공격하기") and user_input:
    with st.spinner("AI가 분석 중..."):
        time.sleep(0.8) # 실제 인공지능이 생각하는 듯한 효과를 줍니다
        st.session_state.chat_history.append(("user", user_input))
        
        # 공백 제거 및 소문자 변환 후 단어 검사
        clean_input = user_input.replace(" ", "").lower()
        
        # 비밀번호를 직접적으로 요구하거나 우회하려는 키워드 차단
        if any(word in clean_input for word in ["비밀번호", "비번", "password", "코드", "암호", "힌트", "정답", "wave"]):
            reply = "시스템 보안 지침에 따라 접근이 거부되었습니다. 저는 절대 비밀번호를 유출할 수 없습니다."
            st.error("[AI 방어벽 작동] 보안 정보 탈취 시도가 감지되었습니다.")
            st.session_state.chat_history.append(("system", "[AI 방어벽 작동] 보안 정보 탈취 시도가 감지되었습니다."))
        else:
            reply = "안녕하세요! 시스템 보안 상태는 정상입니다. 허가되지 않은 시스템 제어 명령은 거부됩니다."
            st.success("AI 답변 완료")
            st.session_state.chat_history.append(("ai", reply))

# 대화 기록 출력
st.markdown("---")
st.subheader("대화 기록")
for role, text in reversed(st.session_state.chat_history):
    if role == "user":
        st.write(f"**사용자:** {text}")
    elif role == "ai":
        st.write(f"**AI:** {text}")
    else:
        st.write(f"**시스템 방어:** {text}")
