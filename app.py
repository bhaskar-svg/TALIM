
import streamlit as st
from PIL import Image

st.set_page_config(page_title="TALIM", layout="wide")

def main():
    col1, col2 = st.columns([1, 5])
    with col1:
        try:
            logo = Image.open("assets/images/logo.png")
            st.image(logo, width=100)
        except:
            st.warning("Logo not found.")
    with col2:
        st.title("Telangana Academy of Land Information and Management (TALIM)")

    st.write("Welcome to the official TALIM portal. Use the sidebar to navigate.")

if __name__ == "__main__":
    main()
