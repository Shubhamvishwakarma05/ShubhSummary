### Models Used
1. **Abstractive Summarization: T5 (Small)**  
   - **What**: `t5-small` from Hugging Face’s `transformers` library.
   - **Why**: It’s a lightweight version of the T5 (Text-To-Text Transfer Transformer) model, pre-trained by Google. Perfect for generating concise, rephrased summaries without needing a beefy GPU or tons of memory.
   - **How**: Loaded via `pipeline("summarization", model="t5-small", framework="pt")`. The `pt` means it runs on PyTorch (`torch==2.4.1`), which is why that’s in your `requirements.txt`.
   - **Details**: 
     - Fine-tuned on tasks like summarization (e.g., CNN/DailyMail dataset).
     - Configured with `do_sample=True, top_k=50` for more natural, creative outputs.
     - Max length set via slider (50-200 words), min length at 50 for decent output.

2. **Sentiment Analysis: Default Hugging Face Model**  
   - **What**: The default model in `pipeline("sentiment-analysis")`—typically `distilbert-base-uncased-finetuned-sst-2-english`.
   - **Why**: It’s a distilled BERT model, small and fast, pre-trained on sentiment tasks (positive/negative classification). Comes built-in with `transformers`, so no extra config needed.
   - **How**: Loaded with `pipeline("sentiment-analysis")`. It spits out labels (POSITIVE/NEGATIVE) and confidence scores (e.g., 0.98).
   - **Details**: 
     - Based on DistilBERT, fine-tuned on the SST-2 dataset.
     - Handles short text snippets (like your summaries) well.

3. **Text Preprocessing: spaCy’s `en_core_web_sm`**  
   - **What**: Small English model from `spacy==3.7.6`.
   - **Why**: Used for tokenizing text into sentences for the extractive summarization part (TF-IDF scoring). It’s fast and accurate for English text.
   - **How**: Loaded with `nlp = spacy.load("en_core_web_sm")`.
   - **Details**: Pre-trained on English web data, handles sentence splitting and basic NLP tasks.

### Why Not Others?
- **BART or PEGASUS**: Bigger summarization models, but `t5-small` is lighter (60M parameters vs. 400M+ for BART) and still effective for a portfolio project.
- **Custom Sentiment Models**: The default `distilbert` is plug-and-play and good enough—training your own would overcomplicate things here.
- **Larger spaCy Models**: `en_core_web_md` or `lg` offer more features (e.g., word vectors), but `sm` is sufficient for sentence tokenization and keeps it lean.

### Where It’s Used in Code
- **T5**: In `abstractive_summary()`—generates the rephrased summary.
- **DistilBERT**: In `analyze_sentiment()`—tags sentiment for both extractive and abstractive outputs.
- **spaCy**: In `extractive_summary()`—splits text into sentences for TF-IDF ranking.

### Cool Factor
These models make “ShubhSummary” legit:
- **T5**: Shows you’re using state-of-the-art generative NLP.
- **DistilBERT**: Adds a practical, real-world feature (sentiment).
- **spaCy**: Grounds it in solid text processing.

If you’re curious, you could swap `t5-small` for `t5-base` (bigger, better outputs, but slower) or play with a custom sentiment model—let me know if you want to tweak it! Happy with these, bro? What’s your next question?
