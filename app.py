import streamlit as st
import spacy
import subprocess
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline
import nltk
nltk.download('punkt')

@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="t5-small", framework="pt")

@st.cache_resource
def load_sentiment_analyzer():
    return pipeline("sentiment-analysis")

# Load models with progress feedback
with st.spinner("Loading NLP models..."):
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        st.warning("Downloading spaCy model 'en_core_web_sm'—this might take a sec...")
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"], check=True)
        nlp = spacy.load("en_core_web_sm")
    summarizer = load_summarizer()
    sentiment_analyzer = load_sentiment_analyzer()
st.success("Models loaded successfully!")

# Extractive summarization function
def extractive_summary(text, num_sentences=2):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents if len(sent.text.strip()) > 10]
    if len(sentences) < num_sentences:
        return "Text too short for summary."
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(sentences)
    sentence_scores = np.array(tfidf_matrix.sum(axis=1)).flatten()
    top_indices = sentence_scores.argsort()[-num_sentences:][::-1]
    top_sentences = [sentences[i] for i in sorted(top_indices)]
    return " ".join(top_sentences)

# Abstractive summarization function
def abstractive_summary(text, max_len=200, min_len=50):
    try:
        summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=True, top_k=50)[0]["summary_text"]
        return summary
    except Exception as e:
        return f"Error: {str(e)}"

# Sentiment analysis
def analyze_sentiment(text):
    result = sentiment_analyzer(text)[0]
    return result['label'], result['score']

# Streamlit UI with enhancements
def main():
    st.markdown("""
        <style>
        .stApp {
            background-color: #2c3e50;
            color: #ecf0f1;
        }
        .stButton>button {
            background-color: #e74c3c;
            color: white;
        }
        .stSlider .stSliderLabel {
            color: #ecf0f1;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("✨ ShubhSummary ✨")
    st.markdown("Summarize text effortlessly with advanced NLP techniques. Built by Shubham Vishwakarma.")

    st.sidebar.header("⚙️ Settings")
    mode = st.sidebar.selectbox("Summary Mode", ["Extractive", "Abstractive", "Hybrid"], help="Choose how to summarize: key sentences, rephrased text, or both.")
    num_sentences = st.sidebar.slider("Extractive Sentences", 1, 5, 2, help="Number of sentences for extractive summary.")
    max_len = st.sidebar.slider("Abstractive Max Length", 50, 200, 100, help="Max words for abstractive summary.")

    with st.expander("📖 How to Use ShubhSummary", expanded=False):
        st.markdown("""
        Welcome to **ShubhSummary**! Here’s how to get started:
        - **Step 1**: Paste your text in the box below.
        - **Step 2**: Adjust settings in the sidebar:
          - **Summary Mode**: Pick **Extractive** (key sentences), **Abstractive** (rephrased summary), or **Hybrid** (both).
          - **Extractive Sentences**: Slide to choose how many sentences (1-5) for extractive mode.
          - **Abstractive Max Length**: Set the max length (50-200 words) for abstractive mode.
        - **Step 3**: Click **Generate Summary** to see results.
        - **Features**: 
          - Sentiment analysis shows the tone (Positive/Negative) with confidence scores.
          - Word count of original text for reference.
        - **Tip**: Try short news snippets or long articles to see the magic!
        """)

    st.subheader("📝 Enter Your Text")
    input_text = st.text_area("Paste your text here...", height=200, help="Enter any text—articles, blogs, or notes!")

    if st.button("Generate Summary 🚀"):
        if not input_text.strip():
            st.error("Please enter some text!")
        else:
            with st.spinner("Summarizing your text..."):
                st.write(f"**Original Text**: {len(input_text.split())} words")

                if mode == "Extractive" or mode == "Hybrid":
                    ext_summary = extractive_summary(input_text, num_sentences)
                    st.subheader("📌 Extractive Summary")
                    st.write(ext_summary)
                    label, score = analyze_sentiment(ext_summary)
                    st.write(f"**Sentiment**: {label} (Confidence: {score:.2f})")

                if mode == "Abstractive" or mode == "Hybrid":
                    abs_summary = abstractive_summary(input_text, max_len=max_len)
                    st.subheader("✍️ Abstractive Summary")
                    st.write(abs_summary)
                    label, score = analyze_sentiment(abs_summary)
                    st.write(f"**Sentiment**: {label} (Confidence: {score:.2f})")

    st.markdown("---")
    st.markdown("""
        **Built with ❤️ by Shubham Vishwakarma**  
        - [GitHub](https://github.com/Shubhamvishwakarma05)  
        - [LinkedIn](https://www.linkedin.com/in/shubhamvishwakarma05/)  
        Add ShubhSummary to your data science portfolio—fork it, tweak it, make it yours! 🚀
    """)

    theme = st.sidebar.selectbox("🎨 Theme", ["Dark", "Light"], index=0)
    if theme == "Light":
        st.markdown("""
            <style>
            .stApp {
                background-color: #f0f2f6;
                color: #333333;
            }
            .stButton>button {
                background-color: #4CAF50;
            }
            .stSlider .stSliderLabel {
                color: #2c3e50;
            }
            </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
