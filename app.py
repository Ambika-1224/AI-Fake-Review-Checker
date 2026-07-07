import streamlit as st
st.set_page_config(
    page_title="AI Fake Review Checker",
    page_icon="🤖",
    layout="centered"
)

import tempfile
from PIL import Image
from ai_agent import analyze_review, analyze_review_image


st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0B1220 0%, #111827 45%, #1E3A8A 100%);
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

.stTextArea textarea {
    border-radius: 12px;
}

h1 {
    color: #00E5FF;
    text-align: center;
            font-size: 42px;
            font-weight: bold;
}
            p {
    font-size: 18px;
}
          section[data-testid="stSidebar"] {
    font-size: 17px;
}  

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

banner = Image.open("image/banner.png")
st.image(banner, width="stretch")

with st.sidebar:
    st.title("🤖 AI Fake Review Checker")

    st.markdown("### Developer")
    st.write("Ambika")

    st.markdown("### AI Model")
    st.write("Google Gemini 2.5 Flash")

    st.markdown("### Version")
    st.write("v1.0")

    st.markdown("### Features")
    st.write("✅Fake/Genuine Detection")
    st.write("✅Confidence Score")
    st.write("✅Sentiment Analysis")
    st.write("✅AI Reasoning")

st.title("AI-Powered Fake Review Detection")
st.write(
    "Paste a product review below and click **Analyze Review**."
    "Our AI will analyze the review and determine whether it appears genuine or potentially fake."
)

uploaded_file = st.file_uploader(
    "Upload Review Screenshot (Optional)",
    type=["png", "jpg", "jpeg"]
)
st.markdown("---")
st.markdown("### OR")
st.markdown("---")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Screenshot", use_container_width=True)


    
review = st.text_area("✍️Enter your product review here:")

if st.button("🔍Analyze Review"):
    if uploaded_file is None and review.strip() == "":
        st.warning("⚠️ Please enter a review OR upload a screenshot.")
    else:
        st.success("✅ Input received successfully!")

        with st.spinner("🤖 Analyzing review... Please wait."
        
        ):
            if uploaded_file is not None:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                    tmp.write(uploaded_file.getbuffer())
                    image_path = tmp.name
                result = analyze_review_image(image_path)
            else:
                result = analyze_review(review)

        st.success("✅ Analysis Complete!")

        st.markdown("""
        ---
        ### 🤖 AI Analysis Result
        """)

        lines = result.split("\n")

        for line in lines:
            if "Verdict" in line:
                if "Genuine" in line:
                    st.success(line)
                else:
                    st.error(line)
            else:
                st.write(line)

        st.download_button(
            label="📄 Download AI Report",
            data=result,
            file_name="AI_Review_Report.txt",
            mime="text/plain"
        )
st.markdown("---")

st.caption(" AI Fake Review Checker | Developed by Ambika")



