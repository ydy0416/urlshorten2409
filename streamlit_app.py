import streamlit as st

# URL 단축 함수
def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

# Streamlit 애플리케이션 인터페이스
st.title("URL 단축기")
st.write("긴 URL을 입력하고 단축된 URL을 얻으세요.")

# URL 입력 받기
long_url = st.text_input("긴 URL 입력")

if st.button("URL 단축"):
    if long_url:
        try:
            short_url = shorten_url(long_url)
            st.success(f"단축된 URL: {short_url}")
        except Exception as e:
            st.error(f"오류 발생: {str(e)}")
    else:
        st.warning("URL을 입력하세요.")
