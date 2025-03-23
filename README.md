# ShubhSummary

![image](https://github.com/user-attachments/assets/b69e193a-1c78-47a2-b4e8-56572341c8fb)

A powerful, interactive text summarization tool built with Python, Streamlit, and advanced NLP techniques. **ShubhSummary** combines **extractive** and **abstractive** summarization methods, adds sentiment analysis, and wraps it all in a sleek, customizable UI. Perfect for data science portfolios, NLP enthusiasts, or anyone who wants concise insights from text!

- LinkedIn: [shubhamvishwakarma05](https://www.linkedin.com/in/shubhamvishwakarma05/)

## 🌟 Features
![image](https://github.com/user-attachments/assets/21e5f337-369b-400d-862d-9ef441a70fa9)

- **Hybrid Summarization**:
  - **Extractive**: Pulls key sentences using TF-IDF scoring (1-5 sentences, adjustable).
  - **Abstractive**: Generates concise, rephrased summaries with the T5 model (50-200 words, adjustable).
  - **Hybrid Mode**: Combines both for a comprehensive overview.
- **Sentiment Analysis**: Detects the tone (Positive/Negative) of summaries with confidence scores.
- **Interactive UI**: Built with Streamlit, featuring:
  - Customizable settings via sidebar sliders and dropdowns.
  - Light/Dark theme toggle for a personalized look.
  - Collapsible “How to Use” guide for new users.
- **Word Count**: Displays the original text’s word count for context.
- **Styling**: Modern design with a light gray-blue background (or dark mode), green/red buttons, and tooltips.

---

## 🛠️ Tech Stack

- **Python**: Core language (3.8+ compatible).
- **Streamlit**: Interactive web app framework.
- **spaCy**: Text preprocessing and sentence tokenization.
- **Transformers (Hugging Face)**: T5 model for abstractive summarization and sentiment analysis.
- **scikit-learn**: TF-IDF for extractive summarization.
- **NLTK**: Additional text processing support.
- **rouge-score**: Ready for summary evaluation (optional extension).

---

## 📋 Prerequisites

- **Python**: Version 3.8–3.10 recommended (3.11 may have compatibility issues).
- **Virtual Environment**: Optional but recommended for dependency management.
- **Windows Users**: Microsoft Visual C++ Build Tools (for `spacy` compilation)—see [Installation](#installation).

---

## 🚀 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Shubhamvishwakarma05/ShubhSummary.git
   cd ShubhSummary
   ```

2. **Set Up a Virtual Environment** (optional):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Requirements.txt*:
   ```
   streamlit==1.40.1
   spacy==3.7.6
   transformers==4.44.2
   torch==2.4.1
   scikit-learn==1.3.2
   nltk==3.9.1
   rouge-score==0.1.2
   ```

4. **Download spaCy Model**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **Windows-Specific (if needed)**:
   - Install [Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) with “Desktop development with C++” if `spacy` fails to build.

---

## 🖥️ Usage

1. **Run the App**:
   ```bash
   streamlit run summarizer.py
   ```
   - Opens at `http://localhost:8501` in your browser.

2. **How to Use**:
   - **Paste Text**: Enter any text (news, articles, blogs) in the text area.
   - **Adjust Settings** (sidebar):
     - **Summary Mode**: Choose Extractive, Abstractive, or Hybrid.
     - **Extractive Sentences**: Slide between 1-5 sentences.
     - **Abstractive Max Length**: Set 50-200 words.
     - **Theme**: Toggle Light or Dark mode.
   - **Generate**: Click “Generate Summary 🚀” to see results.
   - **Explore Outputs**: Check extractive/abstractive summaries and sentiment scores.

3. **Example Input**:
   ```
   Climate change is one of the most pressing issues facing humanity today. Scientists report that global temperatures have risen by 1.1°C since pre-industrial levels...
   ```
   - **Extractive**: Key sentences about weather events and tipping points.
   - **Abstractive**: “Rising temperatures and extreme weather push for urgent action.”

---

## 🎨 UI Preview

- **Light Mode**: Clean gray-blue background, green buttons.
- **Dark Mode**: Sleek dark theme with red buttons.
- **Sidebar**: Intuitive controls with tooltips.
- **Footer**: Links to my GitHub and LinkedIn for networking.

---

## 🌱 Future Enhancements

- **File Upload**: Summarize `.txt` files directly.
- **ROUGE Scores**: Add evaluation metrics for summary quality.
- **Visuals**: Word clouds or sentiment charts.
- **Deployment**: Host on Streamlit Community Cloud for a live demo.

---

## 🤝 Contributing

Feel free to fork this repo, tweak it, or suggest improvements! Open a pull request or issue on [GitHub](https://github.com/Shubhamvishwakarma05/ShubhSummary).

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Built with love using [Streamlit](https://streamlit.io/), [spaCy](https://spacy.io/), and [Hugging Face Transformers](https://huggingface.co/).
- Thanks to the open-source community for making this possible!

---
